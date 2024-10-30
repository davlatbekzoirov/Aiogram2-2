from typing import Union
from aiogram import types
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from keyboards.inline.menu_keyboards import *
from keyboards.default.start_keyboard import menu
from loader import dp, db


# Bosh menyu matni uchun handler
@dp.message_handler(text="Bosh menyu")
async def show_menu(message: types.Message):
    await list_categories(message)


async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    markup = await categories_keyboard()
    if isinstance(message, Message):
        await message.answer("Bo'lim tanlang", reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)
    await callback.message.edit_reply_markup(markup)


async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)

    await callback.message.edit_text(text="Kursni tanlang", reply_markup=markup)


async def show_item(callback: CallbackQuery, category, subcategory, item_id):
    markup = item_keyboard(category, subcategory, item_id)
    item = await db.get_product(item_id)

    if item["photo"]:
        text = f"<a href=\"{item['photo']}\">{item['productname']}</a>\n\n"
    else:
        text = f"{item['productname']}\n\n"
    text += f"Narxi: {item['price']}$\n{item['description']}"

    await callback.message.edit_text(text=text, reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    current_level = callback_data.get("level")
    category = callback_data.get("category")
    subcategory = callback_data.get("subcategory")
    item_id = int(callback_data.get("item_id"))

    levels = {
        "0": list_categories, 
        "1": list_subcategories,  
        "2": list_items,  
        "3": show_item, 
    }

    current_level_function = levels[current_level]

    await current_level_function(
        call, category=category, subcategory=subcategory, item_id=item_id
    )

@dp.callback_query_handler(text='cancel')
async def navigate(call: CallbackQuery):
    name = call.message.from_user.full_name
    user_id =call.message.from_user.id
    call.message.delete()
    photo_id = "AgACAgIAAxkBAAIJ2WXxzr8gV-sXJHHV5ke8Edg6bpwVAAKn1zEbBuWRSw2mx-Dc45NoAQADAgADeQADNAQ"
    msg = f"✋<b>Assalomu alaykum </b>{name},<i>Microsoft Academyning botiga xush kelibsiz</i>\n"
    msg += f"✋<b>Привет, </b>{name}!<i>Добро пожаловать в бот Microsoft Academy</i>"
    await call.message.answer_photo(photo_id, caption=msg, reply_markup=menu)