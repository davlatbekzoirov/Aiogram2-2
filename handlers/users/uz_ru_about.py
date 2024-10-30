from aiogram.types import CallbackQuery, Message
from loader import *
from keyboards.inline.uz_ru import *
from keyboards.inline.coursesUzRu import *
from keyboards.inline.callback_data import menu_cdUz
import sqlite3
from typing import Union
from loader import add_postUz

@dp.message_handler(text="🇺🇿 O'zbek tili")
async def show_menu(call: CallbackQuery):
    await list_categories(call)


async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    # Keyboardni chaqiramiz
    markup = await categories_keyboard()

    # Agar foydalanuvchidan Message kelsa Keyboardni yuboramiz
    if isinstance(message, Message):
        await message.answer("Kurs tanlang", reply_markup=markup)

    # Agar foydalanuvchidan Callback kelsa Callback natbibi o'zgartiramiz
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)

async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)

    # Xabar matnini o'zgartiramiz va keyboardni yuboramiz
    await callback.message.edit_reply_markup(markup)

async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)

    await callback.message.edit_text(text="Mahsulot tanlang", reply_markup=markup)


# async def show_item(callback: CallbackQuery, category, item_id):
#     markup = item_keyboard(category, item_id)

#     item = await add_postUz.get_product(item_id)
#     photo_id = item["photo"]

#     # if item["photo"]:
#     #     text = f"{item['photo']} {item['productname']}</a>\n\n"
#     # else:
#     #     text = f"{item['productname']}\n\n"

#     text = f"{item['description']}"

#     # text = f"{item['textUz']}"
#     # await callback.message.edit_text(text=text, reply_markup=markup)

#     await callback.message.answer_photo(photo_id, caption=text, reply_markup=markup)

#     # await callback.message.edit_text(text=text, reply_markup=markup)
# @dp.callback_query_handler(menu_cdUz.filter())
# async def navigate(call: CallbackQuery, callback_data: dict):
#     current_level = callback_data.get("level")

#     category = callback_data.get("category")

#     item_id = int(callback_data.get("item_id"))

#     levels = {
#         "0": list_categories,  
#         "1": show_item, 
#     }

#     current_level_function = levels[current_level]

#     await current_level_function(
#         call, category=category, item_id=item_id
#     )
    
async def show_item(callback: CallbackQuery, category, subcategory, item_id):
    markup = item_keyboard(category, subcategory, item_id)

    # Mahsulot haqida ma'lumotni bazadan olamiz
    item = await db.get_product(item_id)

    if item["photo"]:
        text = f"<a href=\"{item['photo']}\">{item['productname']}</a>\n\n"
    else:
        text = f"{item['productname']}\n\n"
    text += f"Narxi: {item['price']}$\n{item['description']}"

    await callback.message.edit_text(text=text, reply_markup=markup)


# Yuqoridagi barcha funksiyalar uchun yagona handler
@dp.callback_query_handler(menu_cdUz.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Handlerga kelgan Callback query
    :param callback_data: Tugma bosilganda kelgan ma'lumotlar
    """

    # Foydalanuvchi so'ragan Level (qavat)
    current_level = callback_data.get("level")

    # Foydalanuvchi so'ragan Kategoriya
    category = callback_data.get("category")

    # Ost-kategoriya (har doim ham bo'lavermaydi)
    subcategory = callback_data.get("subcategory")

    # Mahsulot ID raqami (har doim ham bo'lavermaydi)
    item_id = int(callback_data.get("item_id"))

    # Har bir Level (qavatga) mos funksiyalarni yozib chiqamiz
    levels = {
        "0": list_categories,  # Kategoriyalarni qaytaramiz
        "1": list_subcategories,  # Ost-kategoriyalarni qaytaramiz
        "2": list_items,  # Mahsulotlarni qaytaramiz
        "3": show_item,  # Mahsulotni ko'rsatamiz
    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[current_level]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    await current_level_function(
        call, category=category, subcategory=subcategory, item_id=item_id
    )


# @dp.callback_query_handler(text="uz", state="*")
# async def buy_courses(call: CallbackQuery):
#     await call.message.delete()
    # keyboard = InlineKeyboardMarkup(row_width=1)
    # keyboard.add(InlineKeyboardButton(text=f"{add_postUz.get_course_details()}"))
    # buttons = types.InlineKeyboardMarkup()
    # data = add_postUz.get_add_postUz()
    # if not data:
    #     return None
    # for search_coursename in data:
    #     buttons.append(types.InlineKeyboardButton(text=search_coursename, callback_data=f"courseUz_{search_coursename}"))
    # await call.message.answer("Kurs tanlang:", reply_markup=coursesMenuuz)
    # return buttons
# @dp.callback_query_handler(course_callbackUz.filter(item_name="pythonuz"))
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     photo_id = "AgACAgIAAxkBAAIK2mXzCr3ioCVulDyPRM3-j30vUOdxAAJb2DEbwluZSx0hf2NdNSftAQADAgADeQADNAQ"
#     msg = f"Siz Python Dasturlash Asoslari Kursini tanladingiz."
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=backuz_python)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="pythonuz_about")
# async def cancel_buying(call: CallbackQuery):
#     photo_id = "AgACAgIAAxkBAAIK2mXzCr3ioCVulDyPRM3-j30vUOdxAAJb2DEbwluZSx0hf2NdNSftAQADAgADeQADNAQ"
#     msg = f"Python yuqori darajadagi, umumiy maqsadli dasturlash tili boʻlib, dinamik kuchli matn terish va avtomatik xotira boshqaruviga ega boʻlib, ishlab chiquvchilar unumdorligini, kodni oʻqish va kod sifatini hamda dasturlarni koʻchirish qobiliyatini yaxshilashga qaratilgan."
#     await call.message.delete()
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=canceluz)

# @dp.callback_query_handler(text="back_python_uz")
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Kurs tanlang:", reply_markup=coursesMenuuz)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(course_callbackUz.filter(item_name="djangouz"))
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     photo_id = "AgACAgIAAxkBAAILBWXzDXnowV54r2zZaUldk-ufvOPAAAJ22DEbwluZS6mwZRZimzxOAQADAgADeQADNAQ"
#     msg = f"Siz Django Web Dasturlash Kursini tanladingiz."
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=backuz_django)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="djangouz_about")
# async def cancel_buying(call: CallbackQuery):
#     photo_id = "AgACAgIAAxkBAAILBWXzDXnowV54r2zZaUldk-ufvOPAAAJ22DEbwluZS6mwZRZimzxOAQADAgADeQADNAQ"
#     msg = f"Django - bu MVC dizayn naqshidan foydalangan holda Python-da yozilgan bepul veb-ilovalar ramkasi. Loyiha Django Software Foundation tomonidan qo'llab-quvvatlanadi. Django veb-sayti o'zlashtirilishi va ulanishi tavsiya etilgan bir yoki bir nechta ilovalardan iborat."
#     await call.message.delete()
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=canceluz)

# @dp.callback_query_handler(text="back_django_uz")
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Kurs tanlang:", reply_markup=coursesMenuuz)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(course_callbackUz.filter(item_name="telegramuz"))
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     photo_id = "AgACAgIAAxkBAAILB2XzDfG8NkeCjCp-kb8LCSjyUAt5AAJ52DEbwluZS6GlOX568KY5AQADAgADeAADNAQ"
#     msg = f"Siz Mukammal Telegram Bot Kursini tanladingiz."
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=backuz_telegram)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="telegramuz_about")
# async def cancel_buying(call: CallbackQuery):
#     photo_id = "AgACAgIAAxkBAAILB2XzDfG8NkeCjCp-kb8LCSjyUAt5AAJ52DEbwluZS6GlOX568KY5AQADAgADeAADNAQ"
#     msg = f"Telegram – matn, ovozli va video xabarlar, shuningdek, ko‘plab formatdagi stikerlar, fotosuratlar va fayllarni almashish funksiyalariga ega bo‘lgan o‘zaro platformali lahzali xabar almashish tizimi."
#     await call.message.delete()
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=canceluz)

# @dp.callback_query_handler(text="back_telegram_uz")
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Kurs tanlang:", reply_markup=coursesMenuuz)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(course_callbackUz.filter(item_name="algorithmuz"))
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     photo_id = "AgACAgIAAxkBAAILCWXzDknnk1hgFGY5y-vQEvyiDGZaAAJ62DEbwluZSyALlp-OqYfLAQADAgADeQADNAQ"
#     msg = f"Siz Ma'lumotlar Tuzilmasi va Algoritmlar Kursini tanladingiz."
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=backuz_algorithm)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="algorithmuz_about")
# async def cancel_buying(call: CallbackQuery):
#     photo_id = "AgACAgIAAxkBAAILCWXzDknnk1hgFGY5y-vQEvyiDGZaAAJ62DEbwluZSyALlp-OqYfLAQADAgADeQADNAQ"
#     msg = f"Algoritm - bu ma'lum bir toifadagi muammolarni hal qilish uchun aniq belgilangan qoidalar to'plami yoki aniq bir masalani hal qilish uchun ijrochining harakatlari tartibini tavsiflovchi ko'rsatmalar to'plami."
#     await call.message.delete()
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=canceluz)

# @dp.callback_query_handler(text="back_algorith_uz")
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Kurs tanlang:", reply_markup=coursesMenuuz)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="cancel")
# async def cancel_buying(call: CallbackQuery):
#     photo_id = "AgACAgIAAxkBAAIJ2WXxzr8gV-sXJHHV5ke8Edg6bpwVAAKn1zEbBuWRSw2mx-Dc45NoAQADAgADeQADNAQ"
#     msg = f"✋<b>Assalomu alaykum </b>{call.message.from_user.full_name},<i>Microsoft Academyning botiga xush kelibsiz</i>\n"
#     msg += f"✋<b>Привет, </b>{call.message.from_user.full_name}!<i>Добро пожаловать в бот Microsoft Academy</i>"
#     await call.message.delete()
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=UzRu)


@dp.callback_query_handler(text="ru")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выбрать курс:", reply_markup=coursesMenuru)
    await call.answer(cache_time=60)

# @dp.callback_query_handler(course_callbackRu.filter(item_name="pythonru"))
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     photo_id = "AgACAgIAAxkBAAIK2mXzCr3ioCVulDyPRM3-j30vUOdxAAJb2DEbwluZSx0hf2NdNSftAQADAgADeQADNAQ"
#     msg = f"Вы выбрали курс «Основы программирования на Python»."
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=backru_python)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(course_callbackRu.filter(item_name="djangoru"))
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     photo_id = "AgACAgIAAxkBAAILBWXzDXnowV54r2zZaUldk-ufvOPAAAJ22DEbwluZS6mwZRZimzxOAQADAgADeQADNAQ"
#     msg = f"Вы выбрали курс «Веб-программирование на Django»."
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=backru_django)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(course_callbackRu.filter(item_name="telegramru"))
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     photo_id = "AgACAgIAAxkBAAILB2XzDfG8NkeCjCp-kb8LCSjyUAt5AAJ52DEbwluZS6GlOX568KY5AQADAgADeAADNAQ"
#     msg = "Вы выбрали курс «Идеальный Telegram-бот»."
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=backru_telegram)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(course_callbackRu.filter(item_name="algorithmru"))
# async def buying_course(call: CallbackQuery):
#     await call.message.delete()
#     photo_id = "AgACAgIAAxkBAAILCWXzDknnk1hgFGY5y-vQEvyiDGZaAAJ62DEbwluZSyALlp-OqYfLAQADAgADeQADNAQ"
#     msg = "Вы выбрали курс «Математический анализ и алгоритмы»."
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=backru_algorithm)
#     await call.answer(cache_time=60)  

# @dp.callback_query_handler(text="pythonru_about")
# async def cancel_buying(call: CallbackQuery):
#     photo_id = "AgACAgIAAxkBAAIK2mXzCr3ioCVulDyPRM3-j30vUOdxAAJb2DEbwluZSx0hf2NdNSftAQADAgADeQADNAQ"
#     msg = f"Python — это высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, предназначенный для повышения производительности разработчиков, читаемости и качества кода, а также переносимости программ."
#     await call.message.delete()
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=cancelru)

# @dp.callback_query_handler(text="djangoru_about")
# async def cancel_buying(call: CallbackQuery):
#     photo_id = "AgACAgIAAxkBAAILBWXzDXnowV54r2zZaUldk-ufvOPAAAJ22DEbwluZS6mwZRZimzxOAQADAgADeQADNAQ"
#     msg = f"Django — это бесплатная платформа веб-приложений, написанная на Python с использованием шаблона проектирования MVC. Проект поддерживается Django Software Foundation. Веб-сайт Django состоит из одного или нескольких приложений, которые рекомендуется освоить и подключить."
#     await call.message.delete()
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=cancelru)

# @dp.callback_query_handler(text="telegramru_about")
# async def cancel_buying(call: CallbackQuery):
#     photo_id = "AgACAgIAAxkBAAILB2XzDfG8NkeCjCp-kb8LCSjyUAt5AAJ52DEbwluZS6GlOX568KY5AQADAgADeAADNAQ"
#     msg = f"Telegram — кроссплатформенная система обмена мгновенными сообщениями с возможностью обмена текстовыми, голосовыми и видеосообщениями, а также стикерами, фотографиями и файлами во многих форматах."
#     await call.message.delete()
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=cancelru)

# @dp.callback_query_handler(text="algorithmru_about")
# async def cancel_buying(call: CallbackQuery):
#     photo_id = "AgACAgIAAxkBAAILCWXzDknnk1hgFGY5y-vQEvyiDGZaAAJ62DEbwluZSyALlp-OqYfLAQADAgADeQADNAQ"
#     msg = f"Алгоритм — это набор четко определенных правил решения определенной категории задач или набор инструкций, описывающих порядок действий исполнителя для решения конкретной проблемы."
#     await call.message.delete()
#     await call.message.answer_photo(photo_id, caption=msg, reply_markup=cancelru)

# @dp.callback_query_handler(text="back_python_ru")
# async def buy_courses(call: CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Выбрать курс:", reply_markup=coursesMenuru)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="back_django_ru")
# async def buy_courses(call: CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Выбрать курс:", reply_markup=coursesMenuru)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="back_telegram_ru")
# async def buy_courses(call: CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Выбрать курс:", reply_markup=coursesMenuru)
#     await call.answer(cache_time=60)

# @dp.callback_query_handler(text="back_algorith_ru")
# async def buy_courses(call: CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Выбрать курс:", reply_markup=coursesMenuru)
#     await call.answer(cache_time=60)