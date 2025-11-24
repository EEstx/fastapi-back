from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app import models, schemas, security, database
router = APIRouter(tags=["Auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/register")
async def register(user: schemas.UserCreate, db: AsyncSession = Depends(database.get_db)):
    hashed_pw = security.get_password_hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user)
    except:
        raise HTTPException(status_code=400, detail="Username already exists")
    return {"msg": "User created"}

@router.post("/login", response_model=schemas.Token)
async def login(
    user_data: schemas.UserLogin,  # <--- Меняем здесь на Pydantic модель (JSON)
    db: AsyncSession = Depends(database.get_db)
):
    # Обращаемся теперь к user_data, а не к form_data
    result = await db.execute(select(models.User).where(models.User.username == user_data.username))
    user = result.scalars().first()
    
    if not user or not security.verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = security.create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
# Функция зависимости для защиты других роутов
async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(database.get_db)):
    # Здесь должна быть декодировка JWT и проверка пользователя
    return token 