from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, ste

app = FastAPI(title="STE Grouping Service")

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