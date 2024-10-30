from aiogram import executor
from loader import *
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    try:await db.create_table_users()
    except Exception as err:print(err)
    try:await ans.create_table_user_answers()
    except Exception as err:print(err)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
