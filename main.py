import os
from fastapi import FastAPI, Request
from aiogram import types
from aiogram.types import Update
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from bot import bot, dp
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

WEBHOOK_PATH = "/webhook"

@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = Update.model_validate(update)
    await dp.feed_update(bot, telegram_update)
    return {"ok": True}
