from aiogram import executor
from time import sleep
from loader import dp, db,bot,balance,price,paymentchecker
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify,on_shutdown_notify
from utils.set_bot_commands import set_default_commands
from data.config import ADMINS
from aiogram import types

async def on_startup(dispatcher):
    # Birlamchi komandalar (/s tart vssa /help)
    await set_default_commands(dispatcher)

    try:db.create_table_users()
    except Exception as e:pass#print(e)
    try:balance.create_table()
    except Exception as e:pass#print(e)
    try:price.create_table()
    except Exception as e:pass#print(e)
    try:paymentchecker.create_table()
    except Exception as e:pass#print(e)
    
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher):
    await on_shutdown_notify(dispatcher)    


if __name__ == '__main__':
    executor.start_polling(dp,on_startup=on_startup,on_shutdown=on_shutdown)   

