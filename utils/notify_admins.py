import logging
from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(chat_id='-1002077533723',text="✅Бот запущен")

async def on_shutdown_notify(dp: Dispatcher):
   await dp.bot.send_message(chat_id='-1002077533723', text="❌Бот выключен")
