from aiogram import executor
from loader import *
import middlewares, filters, handlers
from utils.notify_admins import *
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

    try:db.create_table_users()
    except Exception as e:pass#print(e)
    try:dbru.create_table_users()
    except Exception as e:pass#print(e)
    try:dbstart.create_table_usersStart()
    except Exception as e:pass#print(e)
    try:add_post.create_table()
    except Exception as e:pass#print(e)
    try:add_postUz.create_tableUz()
    except Exception as e:pass#print(e)
    
    await on_startup_notify(dispatcher)

async def on_shutdown(dispatcher):
    await on_shutdown_notify(dispatcher)   

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
