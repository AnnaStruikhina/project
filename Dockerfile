FROM python:3.8-slim

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y \
    fontconfig \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Установка pygame
RUN pip install pygame

# Копирование вашего приложения
WORKDIR /app
COPY app/ .

# Команда запуска
CMD ["python", "play.py"]
