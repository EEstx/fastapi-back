# Используем Node.js
FROM node:22-alpine

# Рабочая директория
WORKDIR /app

# Копируем package.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем остальной код
COPY . .

# Открываем порт (Vite по умолчанию использует 5173)
EXPOSE 5173

# Запускаем в режиме разработки с флагом --host, чтобы был доступ извне контейнера
CMD ["npm", "run", "dev", "--", "--host"]