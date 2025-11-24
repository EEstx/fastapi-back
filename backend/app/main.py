from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routers import auth, ste
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="STE Grouping Service")

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Или ["*"] для разрешения всех (небезопасно для продакшена)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # Теперь Base.metadata точно знает про User и создаст таблицу
        await conn.run_sync(Base.metadata.create_all)
        
# Создаем таблицы при старте (Для продакшена лучше использовать Alembic)
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(auth.router)
app.include_router(ste.router)

@app.get("/")
def root():
    return {"message": "Service is running"}