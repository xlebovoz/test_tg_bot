import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Токен из переменных окружения Fly.io
BOT_TOKEN = "8556114718:AAEJ_Ye0NRvrwFhLoptteVQ2mJW_zcuX1Vs"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я живу на Fly.io!")

# Ответ на любое сообщение
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Вы сказали: {message.text}")

# Запуск (важно для Fly.io!)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())