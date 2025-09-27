@echo off
echo 🚀 Запуск деплою Leopard Web Store на Windows...

:: Зупиняємо старий сервер
taskkill /F /IM python.exe 2>nul

:: Оновлюємо код
git pull origin main

:: Встановлюємо залежності
pip install -r requirements.txt

:: Міграції бази даних
python manage.py migrate

:: Збираємо статичні файли
python manage.py collectstatic --noinput

:: Запускаємо сервер
start python manage.py runserver 0.0.0.0:8000

echo ✅ Сервер запущено на http://localhost:8000