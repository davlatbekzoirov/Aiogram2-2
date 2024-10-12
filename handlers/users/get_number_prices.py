from aiogram import Bot, Dispatcher, executor, types
from time import sleep
from keyboards.default.buttons import ortga_to_main
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp,db,bot,balance,price
import requests
from keyboards.default.buttons import buttons
from data.config import fivesimnettoken as token
from utils.get_number import get_price,get_phone,get_sms,get_country,finish_order,get__country
from loader import soldnumbers
import asyncio
@dp.callback_query_handler(text='soldnumbers')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    key = InlineKeyboardMarkup(row_width=3)
    if int(soldnumbers.count_users(user_id=call.from_user.id) // 5) == soldnumbers.count_users(call.from_user.id) / 5:
        users_count = soldnumbers.count_users(user_id=call.from_user.id) // 5
    else:
        users_count = soldnumbers.count_users(user_id=call.from_user.id) // 5 + 1
    all_users = soldnumbers.get_numbers(user_id=call.from_user.id)
    for i in range(0,5):
        try:
            key.add(InlineKeyboardButton(all_users[i],callback_data=f"number:{all_users[i]}"))
        except:pass
    if users_count > 1:
        next_ = 2
    else:
        next_ = "no"
    if users_count == 0:
        users_count = 1
    key.add(InlineKeyboardButton("⬅️ Предыдущий",callback_data=f"psold:no"))
    key.insert(InlineKeyboardButton(f"1/{users_count}",callback_data=f"page_count"))
    key.insert(InlineKeyboardButton("➡️ Вперед",callback_data=f"nsold:{next_}"))

    key.add(InlineKeyboardButton("🔙 Назад",callback_data=f"back_main"))
    await call.message.answer("☎️ Ваши купленные номера!",reply_markup=key)


@dp.callback_query_handler(state="*", text_contains ='nsold:')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    next_ = call.data.replace("nsold:","")
    if next_ == "no":
        await call.answer("➡️ Не могу двигаться вперед")
        return
    current = int(next_)
    key = InlineKeyboardMarkup(row_width=3)
    if int(soldnumbers.count_users(call.from_user.id) // 5) == soldnumbers.count_users(call.from_user.id) / 5:
        users_count = soldnumbers.count_users(call.from_user.id) // 5
    else:
        users_count = soldnumbers.count_users(call.from_user.id) // 5 + 1 

    all_users = soldnumbers.get_numbers(user_id=call.from_user.id)

    for i in range(int(next_) * 5 - 5,int(next_) * 5):
        try:key.add(InlineKeyboardButton(all_users[i],callback_data=f"number:{all_users[i]}"))
        except:pass
    if users_count <= int(current):
        next_ = "no"
    else:
        next_ = int(current) + 1
    if int(current-1) >= 1:
        previus_ = current - 1
    else: 
        previus_ = "no"
    key.add(InlineKeyboardButton("⬅️ Предыдущий",callback_data=f"psold:{previus_}"))
    key.insert(InlineKeyboardButton(f"{current}/{users_count}",callback_data=f"page_count"))
    key.insert(InlineKeyboardButton("➡️ Вперед",callback_data=f"nsold:{next_}"))

    key.add(InlineKeyboardButton("🔙 Назад",callback_data=f"back_main"))
    try:
        await call.message.edit_text("☎️ Ваши купленные номера!",reply_markup=key)
    except:
        pass

@dp.callback_query_handler(state="*", text_contains ='psold:')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    previus_ = call.data.replace("psold:","")

    if previus_ == "no":
        await call.answer("🔙 Не могу двигаться назад")
        return
    current = int(previus_)
    key = InlineKeyboardMarkup(row_width=3)
    if int(soldnumbers.count_users(call.from_user.id) // 5) == soldnumbers.count_users(call.from_user.id) / 5:
        users_count = soldnumbers.count_users(call.from_user.id) // 5
    else:
        users_count = soldnumbers.count_users(call.from_user.id) // 5 + 1
    all_users = soldnumbers.get_numbers(user_id=call.from_user.id)
    for i in range(int(previus_) * 5 - 5,int(previus_) * 5):
        try:key.add(InlineKeyboardButton(all_users[i],callback_data=f"number:{all_users[i]}"))
        except:pass
    if users_count <= int(current):
        next_ = "no"
    else:
        next_ = current + 1
    if int(current-1) >= 1:
        previus_ = int(current) - 1

    else:
        previus_ = "no"
    key.add(InlineKeyboardButton("⬅️ Предыдущий",callback_data=f"psold:{previus_}"))
    key.insert(InlineKeyboardButton(f"{current}/{users_count}",callback_data=f"page_count"))
    key.insert(InlineKeyboardButton("➡️ Вперед",callback_data=f"nsold:{next_}"))

    key.add(InlineKeyboardButton("🔙 Назад",callback_data=f"back_main"))
    try:await call.message.edit_text("☎️ Ваши купленные номера!",reply_markup=key)
    except:pass
@dp.callback_query_handler(state="*", text_contains ='number:')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    user_id = call.data.replace("number:","")
    data =  soldnumbers.get_number(user_id)[0]
    user = call.from_user.id
    data_1 = data[2].split(":")
    country = get__country(data_1[0])
    product = data_1[1]
    sms_code = data_1[2]
    phone_number = data[3]
    number_price = price.get_price(f'{country}:{product}')



    user_balance = balance.get_balance(user_id=call.from_user.id)
    btn = InlineKeyboardMarkup()
    btn.add(InlineKeyboardButton(text="🔙 Назад", callback_data=f'back_main'))

    await call.message.edit_text(f"""
<b>📌Ваш купленный номер

🌐 Сервис: </b>{product.capitalize()} <b>
🔄 Страна: </b>{country.capitalize()} <b>
💸 Сумма: </b>{number_price} ₽ <b>
📩 Входящие смс: </b><code>{sms_code}</code><b>
📲 Номер телефона: </b><code>{phone_number}</code><b>

💰 Текущий баланс: </b>{round(float(user_balance)*100)/100}
""", reply_markup=btn)





    
@dp.callback_query_handler(lambda c: c.data.startswith('country:'))
async def return_number(call: types.CallbackQuery):
    call_data = call.data
    buttons = call.message.reply_markup.inline_keyboard[0]  #[0].text
    for button in buttons:
        button.callback_data == call_data
        button_text = button.text
        break
    print(button_text)
    await call.message.delete()
    datas = call.data.split(':')
    country = datas[1]
    product = datas[2]
    number_price = price.get_price(f'{country}:{product}')
    user_balance = balance.get_balance(user_id=call.from_user.id)
    remain = await get_price(api_token=token,service_=product,country=get_country(country))
    # print(product,country,get_country(country))
    get_number = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("💳 Платить",callback_data=f"pay:{country}:{product}"),
        InlineKeyboardButton("🔝 Пополнить баланс",callback_data="top_balance")

    ],
    [
        InlineKeyboardButton("🔙 Hазад", callback_data=f"back:{product}")
    ]
])
    product = product.capitalize()
    country = country.capitalize()
    if product == "Whatsapp":product="WhatsApp"
    elif product == "Tiktok":product="Tik Tok"
    if country == "Usa":country = country.upper()
    await call.message.answer(f"""
<b>📌 Вы выбрали

🌐 Сервис:</b> {product}<b>
🔄 Страна:</b> {country}<b>
💸 Сумма:</b> {number_price} ₽<b>
⛔️ Oсталось:</b> {remain}<b>

💰 Баланс:</b> {round(float(user_balance)*100)/100} ₽
""",reply_markup=get_number)



@dp.callback_query_handler(lambda c: c.data.startswith('pay:'))
async def return_number(call: types.CallbackQuery):
    await call.message.delete()
    user_id = call.from_user.id
    datas = call.data.split(':')
    country = datas[1]
    product = datas[2]
    number_price = price.get_price(f'{country}:{product}')
    number_price = str(number_price).replace(",",".")
    user_balance = balance.get_balance(user_id=call.from_user.id) 
    if float(user_balance)<float(number_price):
        await call.message.answer("❌ Недостаточно денег на балансе",reply_markup=ortga_to_main)
        return
    remain = await get_price(api_token=token,service_=product,country=get_country(country))
    number = await get_phone(api_token=token,country=get_country(country),service=product)
    if number=="NoAvailableNumber":await call.message.answer("❌ На данный момент для этой услуги нет номера",reply_markup=ortga_to_main);return
    if number=="NotEnoughFunds":await call.message.answer("❌Произошла ошибка! Обратитесь к администратору @CAHACAP , он решит эту проблему ✅",reply_markup=ortga_to_main);return
    
    if number:
        buttons = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('🔄 Обновить',callback_data=f"sms_phone_id:{number.operation_id}:{number.number}:{number_price}"),

        ],
        [
            InlineKeyboardButton('❌ Отменить заказ',callback_data=f"cancel_phone_id:{number.operation_id}:{number.number}:{number_price}"),

        ],
        [
            InlineKeyboardButton('🔙 Назад',callback_data=f"back_main_no_delete")
        ]

    ])
        balance.minus_balance(user_id=user_id,amount=float(number_price))
        await call.message.answer(f"<b>📲 Baш номер</b> - <code>{number.number}</code>\n<b>🫵 Ваш смс-код:</b> ❌Hичего\n<b>⏳ Для того чтобы его активировать у вас есть:</b> 15:00",reply_markup=buttons)
        await asyncio.sleep(720)
        sms_code = await get_sms(api_token=token, operation_id=number.operation_id)
        await call.message.answer(f"""📩 Ваш заказ на номер {number.number} находится в 3 минутах от истечения срока действия
🤞 Если вы не получили SMS-код, поторопитесь!""")
        if sms_code.message:
            await call.message.answer(
                f"<b>📲 Baш номер</b> - <code>{number.number}</code>\n<b>🫵 Ваш смс-код:</b> <code>{sms_code.message}</code> \n<b>⏳ Для того чтобы его активировать у вас есть:</b> 03:00",
                reply_markup=buttons)

        else:
            await call.message.answer(
                f"<b>📲 Baш номер</b> - <code>{number.number}</code>\n<b>🫵 Ваш смс-код:</b> ❌Hичего \n<b>⏳ Для того чтобы его активировать у вас есть:</b> 03:00",
                reply_markup=buttons)
        await asyncio.sleep(175)
        sms_code = await get_sms(api_token=token, operation_id=number.operation_id)

        if sms_code.message:
            await call.message.answer(f"""<b>📱 Срок действия вашего заказа на номер <code>{number.number} </code> истек<b>
            <b>♦️ Последний sms-код: </b> <code>{sms_code.message}</code>""")
        else:
            await call.message.answer(f"""
📱 Срок действия вашего заказа на номер {number.number} истек
📩 Вам вернули номер, так как sms-код на номер не был получен.
♦️ Сумма денег, возвращенных на ваш счет, составляет {number_price} рубля""")
            balance.update_balance(user_id=user_id, amount=float(number_price))



    else:

        await call.message.answer('❌На данный момент такого номера не осталось.',reply_markup=ortga_to_main)
        
@dp.callback_query_handler(lambda c: c.data.startswith('sms_phone_id:'))
async def return_number(call: types.CallbackQuery):
    user_id = call.from_user.id
    number = call.data.split(':')
    sms_code = await get_sms(api_token=token,operation_id=number[1])
    product = sms_code.service
    country = sms_code.country
    time_left = int(sms_code.time_left)
    sms_code = sms_code.message
    minutes = time_left // 60 
    seconds = time_left - minutes * 60
    time_min = ""
    time_sec = ""
    if minutes < 10:time_min="0" + str(minutes)
    else:time_min = minutes
    if seconds < 10:time_sec="0" + str(seconds)
    else:time_sec = seconds



    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('🔄 Обновить',callback_data=f"sms_phone_id:{number[1]}:{number[2]}:{number[3]}"),

        ],
        [
            InlineKeyboardButton('❌ Отменить заказ',callback_data=f"cancel_phone_id:{number[1]}:{number[2]}:{number[3]}"),

        ],
        [
            InlineKeyboardButton('🔙 Назад',callback_data=f"back_main_no_delete")
        ]

    ])
    all_data = f"{country}:{product}:{sms_code}"

    if sms_code:
        await call.message.delete()
        await call.message.answer(f'<b>📲 Baш номер</b> - <code>{number[2]}</code>\n<b>🫵 Ваш смс-код:</b> <code>{sms_code}</code>\n<b>⏳ Для того чтобы его активировать у вас есть:</b> {time_min}:{time_sec}',reply_markup=buttons)  
        soldnumbers.save_number(user_id=call.from_user.id,data=f"{all_data}",number=number[2])
    else:
        
        await call.message.delete()
        await call.message.answer(f'<b>📲 Baш номер</b> - <code>{number[2]}</code>\n<b>🫵 Ваш смс-код:</b> ❌Hичего\n<b>⏳ Для того чтобы его активировать у вас есть:</b> {time_min}:{time_sec}',reply_markup=buttons)
        msg = await call.answer("❌СМС-код еще не пришел!")
            # await call.answer("Err: 1358840")
@dp.callback_query_handler(lambda c: c.data.startswith('cancel_phone_id:'))
async def return_number(call: types.CallbackQuery):
    await call.message.delete() 
    user_id = call.from_user.id
    number = call.data.split(':')
    
    
    sms_code = await get_sms(api_token=token,operation_id=number[1])
    time_left = int(sms_code.time_left)
    minutes = time_left // 60 
    seconds = time_left - minutes * 60
    time_min = ""
    time_sec = ""
    if minutes < 10:time_min="0" + str(minutes)
    else:time_min = minutes
    if seconds < 10:time_sec="0" + str(seconds)
    else:time_sec = seconds

    sms_code = sms_code.message

    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [ 
            InlineKeyboardButton('🔄 Обновить',callback_data=f"sms_phone_id:{number[1]}:{number[2]}:{number[3]}"),

        ],
        [
            InlineKeyboardButton('❌ Отменить заказ',callback_data=f"cancel_phone_id:{number[1]}:{number[2]}:{number[3]}"),

        ],
        [
            InlineKeyboardButton('🔙 Назад',callback_data=f"back_main_no_delete")
        ]

    ])
    result = await finish_order(token,operation_id=number[1])
    if result == "OK":
        if sms_code:
            await call.message.answer("❌ Этот заказ не предложит отмене!",reply_markup=ortga_to_main)
            await call.message.answer(f'📲 Baш номер - <code>{number[2]}</code>\n🫵 Ваш смс-код: <code>{sms_code}</code>\n<b>⏳ Для того чтобы его активировать у вас есть:</b> {time_min}:{time_sec}',reply_markup=buttons)
        
        else:
            await call.message.answer(f"✅Успешно! Вы отменили заказ и на ваш баланс вернули {number[3]} ₽!😄",reply_markup=ortga_to_main)
            balance.update_balance(user_id=user_id,amount=number[3])            
    if result == "CantFinishError" or result == "TryAgainLater":
        await call.message.answer("""❌Для того чтобы oтменить заказ, вы должны подождать 2 минуты, после этого, вы сможете oтменить заказ.
♻️Повторите попытку через некоторое время😕""")    
        if sms_code:
            await call.message.answer(f'📲 Baш номер - <code>{number[2]}</code>\n🫵 Ваш смс-код: <code>{sms_code}</code>\n<b>⏳ Для того чтобы его активировать у вас есть:</b> {time_min}:{time_sec}',reply_markup=buttons)
        else:
            await call.message.answer(f'📲 Baш номер - <code>{number[2]}</code>\n🫵 Ваш смс-код: ❌Hичего\n<b>⏳ Для того чтобы его активировать у вас есть:</b> {time_min}:{time_sec}',reply_markup=buttons)
    if result == "WrongOperationError":
        await call.message.answer("❌ Этот заказ не предложит отмене и теперь вы не можете получить смс-код с этим номером!",reply_markup=ortga_to_main)
@dp.callback_query_handler(text="back_main")
async def back_main_home(call:types.CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    user_id = call.from_user.id
    user_balance = balance.get_balance(user_id=user_id)
    await call.message.answer_photo(
        'https://telegra.ph/file/b8c5c14681deb42eb67c3.jpg',caption=f"""
📛Ваше имя: <i>{name}</i>
💰Ваш баланс: {round(float(user_balance)*100)/100} ₽

🆔Идентификационный номер: <code>{user_id}</code>""",reply_markup=buttons)
@dp.callback_query_handler(state="*",text="back_main_no_delete")
async def stats_users(call:types.CallbackQuery,state:FSMContext):
    name = call.from_user.full_name
    user_id = call.from_user.id
    user_balance = balance.get_balance(user_id=user_id)
    await call.message.answer_photo(
        'https://telegra.ph/file/b8c5c14681deb42eb67c3.jpg',caption=f"""
📛Ваше имя: <i>{name}</i>
💰Ваш баланс: {round(float(user_balance)*100)/100} ₽

🆔Идентификационный номер: <code>{user_id}</code>""",reply_markup=buttons)
