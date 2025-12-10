import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from flask import Flask
from threading import Thread

# ================== FLASK ДЛЯ UPTIMEROBOT ==================
app = Flask('')

@app.route('/')
def home():
    return "Бот жив и работает! 🚀"

def run_flask():
    """Запускает Flask в отдельном потоке"""
    app.run(host='0.0.0.0', port=8080)

# ================== ТЕЛЕГРАМ БОТ ==================
BOT_TOKEN = os.environ.get("BOT_TOKEN")  # Используй переменную окружения!
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я живу на Replit 24/7!")

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Вы сказали: {message.text}")

async def run_bot():
    """Запускает Telegram бота"""
    print("🤖 Telegram бот запускается...")
    await dp.start_polling(bot)

def main():
    """Главная функция"""
    # 1. Запускаем Flask (для UptimeRobot)
    print("🌐 Запускаю Flask-сервер...")
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # 2. Запускаем Telegram бота
    asyncio.run(run_bot())

if __name__ == "__main__":
    main()