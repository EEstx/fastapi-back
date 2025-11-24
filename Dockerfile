FROM python:3.11-slim

WORKDIR /code

# 1. Копируем requirements.txt из папки backend (или уберите 'backend/', если он в корне)
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Копируем папку backend внутрь контейнера
COPY backend/ ./backend/

# Теперь структура внутри: /code/backend/main.py

# Запуск: обращаемся к модулю backend.main
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
