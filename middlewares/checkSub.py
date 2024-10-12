import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from loader import channels
from utils.misc import subscription
from loader import botstate,db, banuser,bot
import datetime
import sqlite3

class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self,update:types.Update,data:dict):
        if update.message:
            user = update.message.from_user.id
            text = "No"
        elif update.callback_query:           
            if not(update.callback_query.data.startswith("payment_id:")):await update.callback_query.answer(cache_time=60)
            if update.callback_query.data =="check_subs":await update.callback_query.message.delete()
            user = update.callback_query.from_user.id
            text = update.callback_query.data
        else:
            return


        if banuser.check_user(user) and not(text.startswith("sorry_ban")):
            btn = InlineKeyboardMarkup(row_width=1)
            btn.add(InlineKeyboardButton(text=f"👮‍♂️Админ и такой опрометчивый больной",url=f"https://t.me/clone_account"))
            if text == "No":
                await update.message.answer("<b>❌Вы заблокированы в боте!</b>\n\n\n<i>👇🏻Вы можете извиниться перед администратором и разблокироваться, нажав кнопку ниже!</i>",reply_markup=btn)
            else:
                await update.callback_query.message.answer("<b>❌Вы заблокированы в боте!</b>\n\n\n<i>👇🏻Вы можете извиниться перед администратором и разблокироваться, нажав кнопку ниже!</i>",reply_markup=btn)
            raise CancelHandler()

        buttons = InlineKeyboardMarkup(row_width=1)
        final_status = True 
        CHANNELS = channels.get_channels()
        for channel in CHANNELS:
            status = await subscription.check(user_id=user, channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if not status:
                invite_link = await channel.export_invite_link()
                buttons.add(InlineKeyboardButton(text=f"{channel.title}",url=f"{invite_link}"))
        if not final_status:

            buttons.add(InlineKeyboardButton(text="✅ Я подписался/ась",callback_data="check_subs"))
            if update.message:await update.message.answer('⚠️ Чтобы пользоваться ботом, подпишитесь на канал ниже:',reply_markup=buttons)
            else:await update.callback_query.message.answer('⚠️ Чтобы пользоваться ботом, подпишитесь на канал ниже:',reply_markup=buttons)
            raise CancelHandler()
        

