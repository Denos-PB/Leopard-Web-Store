# Тимчасовий Dockerfile для Leopard-Web-Store
FROM python:3.12-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо requirements.txt і встановлюємо залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код проєкту
COPY . .

# Застосовуємо міграції (для тестів/деплою)
RUN python manage.py migrate --noinput

# Збираємо статику (для продакшену)
RUN python manage.py collectstatic --noinput

# Запускаємо сервер через Gunicorn (для продакшену)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Leopard_Web_Store.wsgi:application"]