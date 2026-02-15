import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Bot ishlayapti 🚀")

@dp.message(F.text)
async def echo_handler(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")
