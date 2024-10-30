import logging
from aiogram import Dispatcher
from data.config import ADMINS

async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(chat_id='-1002077533723',text="✅Bot ishga tushdi")

async def on_shutdown_notify(dp: Dispatcher):
   await dp.bot.send_message(chat_id='-1002077533723', text="❌Bot to'xtatildi")
