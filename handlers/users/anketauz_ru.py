from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import *
import sqlite3
from data.config import ADMINS
from states.personalData import *
from keyboards.inline.uz_ru import *
import re
from keyboards.default.contacturu import *



@dp.callback_query_handler(text="kursuz")
async def enter_test(call: CallbackQuery):
    await call.message.answer("To'liq ismingizni kiriting")
    await PersonalDataUz.fullNameUz.set()

@dp.message_handler(state=PersonalDataUz.fullNameUz)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullnameUz = message.text
    await state.update_data({"name": fullnameUz})
    await message.answer("Telefon raqam kiriting", reply_markup=contactuz)
    await PersonalDataUz.next()

def validate_phone_number(phone_number):
    pattern = r'^\+998\d{9}$'
    return re.match(pattern, phone_number) is not None

@dp.message_handler(content_types=types.ContentType.CONTACT, state=PersonalDataUz.phoneNumUz)
async def contacts(message: types.Message, state: FSMContext):
    contact = message.contact
    phone_number = contact.phone_number

    if validate_phone_number(phone_number):
        await state.update_data({"phone": phone_number})

        dataUz = await state.get_data()
        nameUz = dataUz.get("name")
        phoneUz = dataUz.get("phone")

        msg = "<i>Quyidai ma'lumotlar qabul qilindi:</i>\n"
        msg += f"<b>Ismingiz - {nameUz}</b>\n"
        msg += f"<b>Telefon: - {phoneUz}</b>"

        await message.answer(msg, reply_markup=ReplyKeyboardRemove())
        await bot.send_message(chat_id='-1002077533723', text=f"""
Kursga yangi ro'yxatdan o'tgan o'quvchi:
Ismi- {nameUz}
Telefoni - {phoneUz}""")
        try:db.add_user(id=message.from_user.id,name=nameUz, password=phoneUz)
        except sqlite3.IntegrityError as err:pass

        await state.finish()
        msg = f"<b>Sizning ma'lumotlaringiz adminga etib bordi, tez orada aloqaga chiqamiz </b>"
        await message.delete()
        await message.answer(msg, reply_markup=canceluz)
    else:
        await message.answer("b>Iltimos raqamingizni yuboring❌</b>")


@dp.callback_query_handler(text="kursru", state=None)
async def enter_test(call: CallbackQuery):
    await call.message.answer("Введите свое полное имя")
    await PersonalDataRu.fullNameRu.set()

@dp.message_handler(state=PersonalDataRu.fullNameRu)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullnameRu = message.text
    await state.update_data({"name": fullnameRu})
    await message.answer("Введите номер телефона", reply_markup=contactru)
    await PersonalDataRu.next()

def validate_phone_number(phone_number):
    pattern = r'^\+998\d{9}$'
    return re.match(pattern, phone_number) is not None

@dp.message_handler(content_types=types.ContentType.CONTACT, state=PersonalDataRu.phoneNumRu)
async def contacts(message: types.Message, state: FSMContext):
    contactRu = message.contact
    phone_numberRu = contactRu.phone_number

    if validate_phone_number(phone_numberRu):
        await state.update_data({"phone": phone_numberRu})

        dataRu = await state.get_data()
        nameRu = dataRu.get("name")
        phoneRu = dataRu.get("phone")

        msg = "<i>Была получена следующая информация:</i>\n"
        msg += f"<b>Вас зовут {nameRu}</b>\n"
        msg += f"<b>Телефон: - {phoneRu}</b>"

        await message.answer(msg, reply_markup=ReplyKeyboardRemove())
        await bot.send_message(chat_id='-1002077533723', text=f"""
Студент, недавно зарегистрировавшийся на курс:
Имя- {nameRu}
Номмер- {phoneRu}""")
        try:dbru.add_user(id=message.from_user.id,name=nameRu, password=phoneRu)
        except sqlite3.IntegrityError as err:pass

        await state.finish()
        msg = f"<b>Ваша информация дошла до администратора, мы скоро свяжемся с вами.</b>"
        await message.delete()
        await message.answer(msg, reply_markup=cancelru)
    else:
        await message.answer("<b>Вы не отправили номер телефона❌</b>")