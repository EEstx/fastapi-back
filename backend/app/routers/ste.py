from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List
from app import models, schemas, database
from app.routers.auth import get_current_user

router = APIRouter(tags=["STE Management"])

# 1. Загрузка сырых данных
@router.post("/ste/", response_model=schemas.STEResponse)
async def create_ste(ste: schemas.STECreate, db: AsyncSession = Depends(database.get_db), user=Depends(get_current_user)):
    new_ste = models.STE(**ste.dict())
    db.add(new_ste)
    await db.commit()
    await db.refresh(new_ste)
    return new_ste

# 2. Запуск алгоритма группировки (Пример логики)
@router.post("/group/process")
async def process_grouping(db: AsyncSession = Depends(database.get_db), user=Depends(get_current_user)):
    """
    Примитивный алгоритм: группирует товары с одинаковым 'category' внутри features.
    В реальности здесь будет ваш ML/Algorithm код.
    """
    # Получаем товары без группы
    result = await db.execute(select(models.STE).where(models.STE.group_id == None))
    stes = result.scalars().all()
    
    groups_map = {} # key: category_name, value: list of stes

    for ste in stes:
        # Предположим, что в features есть ключ 'category'
        category = ste.features.get("category", "Uncategorized")
        if category not in groups_map:
            groups_map[category] = []
        groups_map[category].append(ste)
    
    # Создаем группы в БД
    created_groups = []
    for cat_name, items in groups_map.items():
        new_group = models.Group(name=f"Group: {cat_name}", common_features={"category": cat_name})
        db.add(new_group)
        await db.flush() # чтобы получить ID
        
        for item in items:
            item.group_id = new_group.id
        
        created_groups.append(new_group.name)

    await db.commit()
    return {"message": "Grouping complete", "groups_created": created_groups}

# 3. Получение результатов (Групп)
@router.get("/groups/", response_model=List[schemas.GroupResponse])
async def get_groups(db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.Group).options(selectinload(models.Group.items)))
    return result.scalars().all()

# 4. Ручное редактирование связей (Перемещение товара в другую группу)
@router.put("/ste/{ste_id}/move/{group_id}")
async def move_ste(ste_id: int, group_id: int, db: AsyncSession = Depends(database.get_db), user=Depends(get_current_user)):
    ste = await db.get(models.STE, ste_id)
    group = await db.get(models.Group, group_id)
    
    if not ste or not group:
        raise HTTPException(status_code=404, detail="STE or Group not found")
    
    ste.group_id = group_id
    await db.commit()
    return {"message": "STE moved successfully"}

@router.get("/{ste_id}", response_model=schemas.STEResponse)
async def get_ste(ste_id: int, db: AsyncSession = Depends(database.get_db)):
    """
    Получение информации о товаре (STE) по его ID.
    Используется для страницы карточки товара.
    """
    # Запрашиваем товар по ID
    result = await db.execute(select(models.STE).where(models.STE.id == ste_id))
    ste = result.scalars().first()
    
    if not ste:
        raise HTTPException(status_code=404, detail="STE not found")
    
    return ste