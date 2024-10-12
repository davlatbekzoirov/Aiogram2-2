from aiogram import Bot, Dispatcher, executor, types 
from time import sleep
from loader import dp,db,bot,paymentchecker,balance
from aiogram.dispatcher import FSMContext
from keyboards.default.buttons import buttons,ortga_to_main
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from data import config as cfg
from uuid import uuid4
from time import sleep
from keyboards.default.buttons import buttons
from AaioAPI import AsyncAaioAPI
import asyncio

async def new_payment(amount,lang="ru",currency='RUB',desc='📩 @Ser4ikShopBot Payment'):
    client = AsyncAaioAPI('YzU5MDcyZjgtNzRmYi00ZmZkLTk3ZTUtNDg3NjBmNTcwZDY2OjBpMG15N3h0X3BtVFlmaGxlM2JIOTBPYndSVG5BS3ds', '5614b691cc1a9d9085e983c6944e89bf', '78b89468-7c57-45c8-8c66-0d33e8a2fdc5')
    order_id = str(uuid4())
    URLPayment = await client.create_payment(order_id, amount, lang, currency, desc)
    return [URLPayment,order_id] 

async def check_payment(order_id):
    client = AsyncAaioAPI('YzU5MDcyZjgtNzRmYi00ZmZkLTk3ZTUtNDg3NjBmNTcwZDY2OjBpMG15N3h0X3BtVFlmaGxlM2JIOTBPYndSVG5BS3ds', '5614b691cc1a9d9085e983c6944e89bf', '78b89468-7c57-45c8-8c66-0d33e8a2fdc5')
    if await client.is_expired(order_id):                
        return "Expired"
    elif await client.is_success(order_id):              
        return "OK"
    else:                                  
        return "NotPaid"
        




@dp.callback_query_handler(text="top_balance")
async def get_price(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("""
🤔 На какую сумму вы хотите пополнить свой счет?(RUB)\n
""",reply_markup=ortga_to_main)
    await state.set_state("amount")
@dp.message_handler(state="amount")
async def get_price(message:types.Message,state:FSMContext):
    user_id = message.from_user.id
    try:
        summa = float(message.text)
    except:
        summa = False


    if summa: 
        if summa<10:
            await message.answer('➖ Минимальная сумма депозита 10 рубль.',reply_markup=ortga_to_main)
            await state.set_state('amount')
            return
        await state.finish()
        payment_details = await new_payment(amount=summa)
        bill_id = payment_details[1]
        URL = payment_details[0]
        paymentchecker.save_payment(bill_id=bill_id, amount=message.text, user_id=message.from_user.id)
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton('💳 Оплатить',url=URL))
        keyboard.add(InlineKeyboardButton('✅ Я oплатил',callback_data=f"payment_id:{bill_id}"))
        keyboard.add(InlineKeyboardButton('🔙 Hазад',callback_data=f"ortga_to_main"))

        await message.answer(f"""
Оплату можно произвести ниже, нажав кнопку: «Оплатить» 
или же нажав на: 
<a href='{URL}'>«Ссылка для оплаты»</a>
Какие либо другие вопросы по платежу?
Обращайтесь😄: @CAHACAP

""",reply_markup=keyboard)   

    
    else:
        back =  InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🔙 Hазад", callback_data="back_home")        
    ]]
)
        await message.answer("😉 Пожалуйста, введите точное число:",reply_markup=back)
@dp.callback_query_handler(state="*",text="back_home")
async def stats_users(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    name = call.from_user.full_name
    user_id = call.from_user.id
    user_balance = balance.get_balance(user_id=user_id)
    await call.message.answer_photo(
        'https://telegra.ph/file/b8c5c14681deb42eb67c3.jpg',caption=f"""
📛Ваше имя: <i>{name}</i>
💰Ваш баланс: {round(float(user_balance)*100)/100} ₽

🆔Идентификационный номер: <code>{user_id}</code>""",reply_markup=buttons)
@dp.callback_query_handler(text_contains="payment_id:")
async def get_price(call:types.CallbackQuery,state:FSMContext):

    await state.finish()
    bill_id = call.data.replace('payment_id:','')
    data = paymentchecker.get_payment(bill_id)
    result = await check_payment(order_id=bill_id)
    if result=="OK":balance.update_balance(data[0],int(data[-1]));await call.message.delete();await call.message.answer(chat_id=data[0],text=f"✅Успешно!😄Ваш запрос на платеж одобрен, и на ваш счет добавлено {int(data[-1])} ₽ .",reply_markup=ortga_to_main)
    elif result=="NotPaid":await call.answer("""❌Пожалуйста, нажмите эту кнопку после оплаты!\n🧑🏻‍💻Если это ошибка, обратитесь в нашу Техническую поддержку.""")
    elif result=="Expired":await call.answer("""💥Устаревшая ссылка. Свяжитесь со службой технической поддержки.""")   
#     await call.message.answer("🖼 Пожалуйста, отправьте фотографию чека:",reply_markup=ortga_to_main)
#     await state.update_data({"bill_id":bill_id})
#     await state.set_state("get_photo")


# @dp.message_handler(content_types=['photo'],state="get_photo")
# async def get_price(message:types.Message,state:FSMContext):
#     await message.answer("✅Отправленный вами чек получен.\n👮🏻‍♂️Наши администраторы ответят в течение 24 часов.\n📇Чек будет проверен и деньги будут вам вручены!",reply_markup=ortga_to_main)
#     data = await state.get_data()
#     bill_id = data.get("bill_id")
#     payment_data = paymentchecker.get_payment(bill_id)
#     photo = message.photo[-1]
#     buttons = InlineKeyboardMarkup()

#     buttons.add(InlineKeyboardButton('✅ Подтверждать',callback_data=f"verify:{bill_id}"))
#     buttons.add(InlineKeyboardButton('❌ Oтменить',callback_data=f"ignore:{bill_id}"))
#     await bot.send_photo(chat_id="-1002063183443",photo=photo.file_id,caption=f"""
# #На_ожидание #On_request ❓
# 📱Поступил новый запрос!
# 👤Имя пользователя: {message.from_user.get_mention()}
# 👌🏻Username пользователя: {message.from_user.username}
# 💳Сумма, на которую хотeл пополнить счет: {paymentchecker.get_payment(bill_id=bill_id)[-1]}
# ➖ ➖ ➖ ➖ ➖
# ❓Пользователь еще не верифицирован!
# """,reply_markup=buttons)
#     await state.finish()

# @dp.callback_query_handler(text_contains="verify:")
# async def get_price(call:types.CallbackQuery,state:FSMContext):
#     bill_id = call.data.replace('verify:','')
#     data = paymentchecker.get_payment(bill_id)
#     balance.update_balance(data[0],int(data[-1]))
#     await bot.send_message(chat_id=data[0],text=f"✅Ваш запрос на платеж одобрен, и на ваш счет добавлено {int(data[-1])} ₽ .",reply_markup=ortga_to_main)
#     button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("👉🏻Пропустить",callback_data="ok")]])
#     user = await bot.get_chat(data[0])
#     await call.message.edit_caption(f"""
# #Подтвержденный #Confirmed ✅
# 📱Запрос подтвержден!
# 👤Имя пользователя: {user.get_mention()}
# 👌🏻Имя пользователя: {user.username}
# 💳 Сумма, которую вы хотите пополнить: {paymentchecker.get_payment(bill_id=bill_id)[-1]}
# ➖ ➖ ➖ ➖ ➖
# ✅Пользователь уже верифицирован
# """,reply_markup=button)
# @dp.callback_query_handler(text_contains="ignore:")
# async def get_price(call:types.CallbackQuery,state:FSMContext):
#     bill_id = call.data.replace('ignore:','')
#     data = paymentchecker.get_payment(bill_id)
#     button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("👉🏻Пропустить",callback_data="ok")]])
#     user = await bot.get_chat(data[0])
#     await call.message.edit_caption(f"""
# #HeПодтвержденный #Unconfirmed #Ignored ❌
# 📱Запрос Heподтвержден!
# 👤Имя пользователя: {user.get_mention()}
# 👌🏻Имя пользователя: {user.username}
# 💳 Сумма, которую вы хотите пополнить: {paymentchecker.get_payment(bill_id=bill_id)[-1]}
# ➖ ➖ ➖ ➖ ➖
# ❌Пользователь Heверифицирован(ignored)
# """,reply_markup=button)