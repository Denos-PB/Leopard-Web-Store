#!/bin/bash
echo "🚀 Запуск деплою Leopard Web Store на Linux..."

# Зупиняємо старий сервер
pkill -f "python manage.py runserver" || true

# Оновлюємо код
git pull origin main

# Встановлюємо залежності
pip install -r requirements.txt

# Міграції бази даних
python manage.py migrate

# Збираємо статичні файли
python manage.py collectstatic --noinput

# Запускаємо сервер у фоновому режимі
nohup python manage.py runserver 0.0.0.0:8000 > server.log 2>&1 &

echo "✅ Сервер запущено на http://localhost:8000"
echo "📋 Логи: tail -f server.log"