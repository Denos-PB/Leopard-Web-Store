#!/usr/bin/env python3
"""
Універсальний скрипт деплою для Leopard Web Store
Працює на Windows, Linux та macOS
"""

import os
import sys
import subprocess
import platform


def run_command(command, description):
    """Виконати команду з перевіркою помилок"""
    print(f"🚀 {description}...")
    try:
        if platform.system() == "Windows":
            result = subprocess.run(command, shell=True, check=True, text=True)
        else:
            result = subprocess.run(command, shell=True, check=True, text=True)
        print(f"✅ {description} успішно!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Помилка під час {description}: {e}")
        return False


def main():
    print("🎯 Універсальний деплой Leopard Web Store")
    print(f"📋 ОС: {platform.system()} {platform.release()}")

    # Визначаємо шляхи в залежності від ОС
    project_dir = os.path.dirname(os.path.abspath(__file__))
    manage_py_path = os.path.join(project_dir, "Leopard_Web_Store", "manage.py")

    if not os.path.exists(manage_py_path):
        print(f"❌ Файл {manage_py_path} не знайдено!")
        print("📁 Доступні файли:")
        for root, dirs, files in os.walk(project_dir):
            level = root.replace(project_dir, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f'{indent}{os.path.basename(root)}/')
            subindent = ' ' * 2 * (level + 1)
            for file in files[:5]:  # Показуємо тільки перші 5 файлів
                print(f'{subindent}{file}')
        return False

    # Зупиняємо старий сервер
    if platform.system() == "Windows":
        run_command("taskkill /F /IM python.exe 2>nul", "Зупинка старого сервера (Windows)")
    else:
        run_command("pkill -f 'python manage.py runserver' || true", "Зупинка старого сервера (Linux/macOS)")

    # Оновлюємо код
    run_command("git pull origin main", "Оновлення коду з Git")

    # Встановлюємо залежності
    run_command("pip install -r requirements.txt", "Встановлення залежностей")

    # Виконуємо міграції
    os.chdir(os.path.join(project_dir, "Leopard_Web_Store"))
    run_command("python manage.py migrate", "Застосування міграцій бази даних")

    # Збираємо статичні файли
    run_command("python manage.py collectstatic --noinput", "Збір статичних файлів")

    # Запускаємо сервер
    if platform.system() == "Windows":
        run_command("start python manage.py runserver 0.0.0.0:8000", "Запуск сервера (Windows)")
    else:
        run_command("nohup python manage.py runserver 0.0.0.0:8000 > server.log 2>&1 &", "Запуск сервера (Linux/macOS)")

    print("\n🎉 Деплой успішний!")
    print("🌐 Сервер доступний за адресами:")
    print("   - Локально: http://localhost:8000")
    print("   - В мережі: http://192.168.1.46:8000")
    print("   - Зовнішня IP: http://176.111.185.147:8000")

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)