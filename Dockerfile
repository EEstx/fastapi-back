FROM python:3.11-slim

WORKDIR /code

# Копируем requirements
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ИЗМЕНЕНО: Копируем код из локальной папки backend в папку app внутри образа
COPY backend/ .
# ИЗМЕНЕНО: Команда запуска теперь ссылается на app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
