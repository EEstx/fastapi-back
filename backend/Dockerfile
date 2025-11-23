FROM python:3.11-slim

# Устанавливаем рабочую директорию НЕ /app, а нейтральную, например /code
WORKDIR /code

# Копируем requirements.txt и устанавливаем зависимости
# (Предполагаем, что requirements.txt лежит в корне проекта рядом с папкой app)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Самый важный момент: копируем ВСЁ содержимое проекта (включая папку app) в /code
COPY . .

# Теперь внутри контейнера структура будет такой: /code/app/main.py

# Команда запуска должна вызывать модуль как пакет (app.main)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]