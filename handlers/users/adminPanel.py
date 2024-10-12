from aiogram.types import Message, CallbackQuery, ContentTypes, InputFile, ChatType
from aiogram.dispatcher import FSMContext
import aiogram
from datetime import datetime
import pytz
import asyncio
import xlsxwriter as xl
import os
from data.config import ADMINS
from keyboards.inline.admin_keys import AdminPanel, SendAd_Type, GoToAdminPanel, backDelete, DeleteUsers, BaseType, \
    answer_admin, back_user
from states.states import send_forwad, sendAd, verifyDeleteUsers, send_user, answer
from loader import dp, db, bot, channels, banuser
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dp.message_handler(state='*', text="/admin", user_id=ADMINS)
async def adminPanelfunc(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(f"👋🏻 Здравствуйте, {message.from_user.full_name}! Добро пожаловать в панель администратора", reply_markup=AdminPanel)

@dp.callback_query_handler(state="*", text='GoToAdminPanel')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"👋🏻 Здравствуйте, {call.from_user.full_name}! Добро пожаловать в панель администратора", reply_markup=AdminPanel)

@dp.callback_query_handler(state="*", text='admin:block')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    key = InlineKeyboardMarkup(row_width=3)
    if int(banuser.count_users() // 5) == banuser.count_users() / 5:
        users_count = banuser.count_users() // 5
    else:
        users_count = banuser.count_users() // 5 + 1
    all_users = banuser.get_ban_users()
    for i in range(0,5):
        
        try:
            data = await bot.get_chat(all_users[i])
            fullname = data.fullname
            key.add(InlineKeyboardButton(fullname,callback_data=f"user:{all_users[i]}"))
        except:
            try:
                key.add(InlineKeyboardButton(all_users[i],callback_data=f"user:{all_users[i]}"))
            except:
                pass
    if users_count > 1:
        next_ = 2
    else:
        next_ = "no"
    if users_count == 0:
        users_count = 1
    key.add(InlineKeyboardButton("⬅️ Предыдущий",callback_data=f"previus:no"))
    key.insert(InlineKeyboardButton(f"1/{users_count}",callback_data=f"page_count"))
    key.insert(InlineKeyboardButton("➡️ Вперед",callback_data=f"next:{next_}"))

    key.add(InlineKeyboardButton("➕ Добавлять",callback_data=f"admin:add_block_user"))
    key.add(InlineKeyboardButton("🔙 Назад",callback_data=f"GoToAdminPanel"))
    await call.message.edit_text("Вы можете настроить эти кнопки!",reply_markup=key)
@dp.callback_query_handler(state="*", text_contains ='admin:add_block_user')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"🚫Введите идентификатор пользователя, которого хотите заблокировать: ",reply_markup=GoToAdminPanel)
    await state.set_state("new_block_user")

@dp.message_handler(state="new_block_user")
async def GoAdminPanelf(message: Message, state: FSMContext):
    await state.finish()
    channel = message.text
    try:
        msg = await bot.send_message(chat_id=channel,text=".")
        await msg.delete()
    except:
        await message.answer("<b>❌Данного пользователя нет в боте или идентификатор введен неверно</b>\n\n\n<i>🔁 Попробуйте ввести идентификатор еще раз:</i>",reply_markup=GoToAdminPanel)
        await state.set_state("new_block_user")
    else:
        if not(banuser.check_user(channel)):
            banuser.ban_user(channel)
            await message.answer("<b>✅Пользователь забанен.</b>\n\n\n<i>👥Этот пользователь больше не может использовать бота.</i>")
            await message.answer(f"👋🏻 Здравствуйте, {message.from_user.full_name}! Добро пожаловать в панель администратора!",reply_markup=AdminPanel)
            await state.finish()
        else:
            await message.answer("<b>✅Этот пользователь уже забанен!</b>")
            await message.answer(f"👋🏻 Здравствуйте, {message.from_user.full_name}! Добро пожаловать в панель администратора!",reply_markup=AdminPanel)
            await state.finish()

@dp.callback_query_handler(state="*", text_contains ='next:')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    next_ = call.data.replace("next:","")
    

    if next_ == "no":
        await call.answer("▶️ Не могу двигаться вперед")
        return
    current = int(next_)

    key = InlineKeyboardMarkup(row_width=3)
    if int(banuser.count_users() // 5) == banuser.count_users() / 5:
        users_count = banuser.count_users() // 5
    else:
        users_count = banuser.count_users() // 5 + 1 

    all_users = banuser.get_ban_users()

    for i in range(int(next_) * 5 - 5,int(next_) * 5):
    
        try:
            data = await bot.get_chat(all_users[i])
            fullname = data.fullname
            key.add(InlineKeyboardButton(fullname,callback_data=f"user:{all_users[i]}"))
        except:
            try:

                key.add(InlineKeyboardButton(all_users[i],callback_data=f"user:{all_users[i]}"))
            except:
                pass
    if users_count <= int(current):
        next_ = "no"
    else:
        next_ = int(current) + 1
    if int(current-1) >= 1:
        previus_ = current - 1
    else: 
        previus_ = "no"
    key.add(InlineKeyboardButton("⬅️ Предыдущий",callback_data=f"previus:{previus_}"))
    key.insert(InlineKeyboardButton(f"{current}/{users_count}",callback_data=f"page_count"))
    key.insert(InlineKeyboardButton("➡️ Вперед",callback_data=f"next:{next_}"))

    key.add(InlineKeyboardButton("➕ Добавлять",callback_data=f"admin:add_block_user"))
    key.add(InlineKeyboardButton("🔙 Назад",callback_data=f"GoToAdminPanel"))
    await call.message.edit_text("Вы можете настроить эти кнопки!",reply_markup=key)

@dp.callback_query_handler(state="*", text_contains ='previus:')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    previus_ = call.data.replace("previus:","")

    if previus_ == "no":
        await call.answer("🔙 Не могу двигаться назад")
        return
    current = int(previus_)
    key = InlineKeyboardMarkup(row_width=3)
    if int(banuser.count_users() // 5) == banuser.count_users() / 5:
        users_count = banuser.count_users() // 5
    else:
        users_count = banuser.count_users() // 5 + 1
    all_users = banuser.get_ban_users()
    for i in range(int(previus_) * 5 - 5,int(previus_) * 5):
        
        try:
            data = await bot.get_chat(all_users[i])
            key.add(InlineKeyboardButton(data.fullname,callback_data=f"user:{all_users[i]}"))
        except Exception as e:
            print(e)
            key.add(InlineKeyboardButton(all_users[i],callback_data=f"user:{all_users[i]}"))
    if users_count <= int(current):
        next_ = "no"
    else:
        next_ = current + 1
    if int(current-1) >= 1:
        previus_ = int(current) - 1

    else:
        previus_ = "no"
    key.add(InlineKeyboardButton("⬅️ Предыдущий",callback_data=f"previus:{previus_}"))
    key.insert(InlineKeyboardButton(f"{current}/{users_count}",callback_data=f"page_count"))
    key.insert(InlineKeyboardButton("➡️ Вперед",callback_data=f"next:{next_}"))

    key.add(InlineKeyboardButton("➕ Добавлять",callback_data=f"admin:add_block_user"))
    key.add(InlineKeyboardButton("🔙 Назад",callback_data=f"GoToAdminPanel"))
    await call.message.edit_text("Вы можете настроить эти кнопки!",reply_markup=key)

@dp.callback_query_handler(state="*", text_contains ='user:')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    user_id = call.data.replace("user:","")
    data = await bot.get_chat(user_id)
    name = data.title
    bio = data.bio
    username = data.username
    id = data.id
    try: 
        txt = await bot.send_message(chat_id=id,text=".")
        await txt.delete()
        bot_blocked = "✅Пользователь на данный момент не заблокировал бота"
    except:
        bot_blocked = "❌Пользователь в данный момент заблокировал бота"

    btn = InlineKeyboardMarkup()
    btn.add(InlineKeyboardButton("➖ Удалить из списка",callback_data=f"del_ban:{user_id}"))
    btn.add(InlineKeyboardButton(text="🔙 Назад", callback_data=f'GoToAdminPanel'))

    await call.message.edit_text(f"""
<b>‼️ Информация об этом пользователе</b>
    <b>├───📛Имя пользователя:</b> {data.full_name} 
    <b>├───🔗Имя пользователя:</b> @{username}
    <b>├───🆔Идентификатор пользователя:</b> <code>{id}</code>
    <b>└───☣️Биография пользователя:</b> {bio} 
➖➖➖➖➖➖➖➖➖➖➖
<b>{bot_blocked}</b>
""", reply_markup=btn)
@dp.callback_query_handler(state="*", text_contains ='del_ban:')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    user_id = call.data.replace("del_ban:","")
    if banuser.del_user(user_id):
        await call.message.edit_text(f"""
<b>✅Пользователь успешно удален из списка.</b>


<i>🥱Теперь этот пользователь имеет право использовать бота!</i>""",reply_markup=GoToAdminPanel)
    else:
        await call.message.edit_text(f"""
<b>❌Пользователь не был успешно удален из списка.</b>


<i>🥱Похоже, какой-то администратор удалил пользователя из списка до вас</i>""",reply_markup=GoToAdminPanel)

    
@dp.callback_query_handler(state="*", text_contains ='del_channel:')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    chan_id = call.data.replace("del_channel:","")
    if channels.del_channel(chan_id):
        await call.message.edit_text(f"""
<b>✅Канал успешно удален.</b>


<i>🥱 Теперь для использования бота пользователям не нужно подписываться на этот канал.</i>""",reply_markup=GoToAdminPanel)
    else:
        await call.message.edit_text(f"""
<b>❌Канал не был успешно удален.</b>


<i>🥱Кажется, какой-то администратор удалил канал до вас</i>""",reply_markup=GoToAdminPanel)

@dp.callback_query_handler(state="*", text_contains ='admin:add_channel')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"💫Введите имя пользователя канала, на который хотите подписаться: ",reply_markup=GoToAdminPanel)
    await state.set_state("new_channel")

@dp.message_handler(state="new_channel")
async def GoAdminPanelf(message: Message, state: FSMContext):
    await state.finish()
    channel = message.text
    try:
        msg = await bot.send_message(chat_id=channel,text=".")
        await msg.delete()
    except:
        await message.answer("<b>❌Бот не является администратором на канале или пользователь канала введен неверно!</b>\n\n\n<i>👮🏻‍♂️ Сделайте бота админом на канале и снова введите логин:</i>",reply_markup=GoToAdminPanel)
        await state.set_state("new_channel")
    else:
        try:
            channels.save_channel(channel)
        except:
            await message.answer("✅Этот канал уже доступен по обязательной подписке.")
            await message.answer(f"👋🏻 Здравствуйте, {message.from_user.full_name}! Добро пожаловать в панель администратора!",reply_markup=AdminPanel)
            await state.finish()
        else:
            await message.answer("<b>✅Канал добавлен в обязательную подписку.</b>\n\n\n<i>👥Теперь всем пользователям необходимо подписаться на канал, чтобы использовать бота</i>")
            await message.answer(f"👋🏻 Здравствуйте, {message.from_user.full_name}! Добро пожаловать в панель администратора!",reply_markup=AdminPanel)
            await state.finish()


@dp.callback_query_handler(state="*", text_contains ='channel:')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    chan_id = call.data.replace("channel:","")
    data = await bot.get_chat(chan_id)
    name = data.title
    bio = data.description
    username = data.username
    members_count = await bot.get_chat_members_count(chat_id=chan_id)
    invite_link = data.invite_link
    id = data.id
    time = channels.get_time_channel(username=chan_id).split(" ")
    btn = InlineKeyboardMarkup()
    btn.add(InlineKeyboardButton("➖ Удалить из списка",callback_data=f"del_channel:{chan_id}"))
    btn.add(InlineKeyboardButton(text="🔙 Ortga", callback_data=f'GoToAdminPanel'))

    await call.message.edit_text(f"""
<b>‼️Информация об этом канале</b>
    <b>├───📛Название канала:</b> {name} 
    <b>├───🔗Пользователь канала:</b> @{username}
    <b>├───👥Количество участников:</b> {members_count}
    <b>├───🆔Идентификатор канала:</b> <code>{id}</code>
    <b>└───☣️Описание канала:</b> {bio} 
➖➖➖➖➖➖➖➖➖➖➖
<b>💥Этот канал добавлен в обязательную подписку:
    ├───📅 Дата:</b> {time[0]}<b>
    └───⏰ Время: </b>{time[1]}
""", reply_markup=btn)

@dp.callback_query_handler(state="*", text='admin:channels')
async def GoAdminPanelf(call: CallbackQuery, state: FSMContext):
    await state.finish()
    btn = InlineKeyboardMarkup(row_width=1)
    l_channels = channels.get_channels()
    for channel in l_channels:
        data = await bot.get_chat(channel)
        title = data.title
        btn.add(InlineKeyboardButton(f"{title}",callback_data=f"channel:{channel}"))
    btn.add(InlineKeyboardButton("➕ Добавлять",callback_data=f"admin:add_channel"))
    btn.add(InlineKeyboardButton("🔙 Назад",callback_data=f"GoToAdminPanel"))
    await call.message.edit_text("Вы можете настроить эти кнопки!", reply_markup=btn)

@dp.callback_query_handler(state='*', text='user_back')
async def user_backfunc(call: CallbackQuery, state: FSMContext):
    await state.finish()


@dp.callback_query_handler(state='*', text='admin:send_ad')
async def send_ad(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer("Выберите тип сообщения для отправки пользователям", reply_markup=SendAd_Type)


@dp.callback_query_handler(state='*', text='forward_habar')
async def forward_habar(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text("<b>📣 Вы можете отправить переадресацию</b>", reply_markup=GoToAdminPanel)
    await send_forwad.text.set()


@dp.message_handler(state=send_forwad.text, content_types=ContentTypes.ANY)
async def text_forward(message: Message, state: FSMContext):
    await state.finish()
    users = db.select_all_users()
    x = 0
    y = 0
    start = datetime.now(pytz.timezone('Asia/Tashkent'))
    i = await message.answer("🔰 Объявление отправляется, подождите...")
    for user in users:
        try:
            await bot.forward_message(chat_id=user[0],
                                      from_chat_id=message.from_user.id,
                                      message_id=message.message_id)
            x += 1
        except:
            y += 1
        await asyncio.sleep(0.05)
    finish = datetime.now(pytz.timezone('Asia/Tashkent'))
    farq = finish - start
    await message.answer(f"<b>📣 Реклама отправлена</b>\n\n"
                         f"✅ Принял: {x} ta\n"
                         f"❌ Не удалось отправить: {y}\n\n"
                         f"<b>⏰ Начал:</b> {start.strftime('%H:%M:%S')}\n"
                         f"<b>⏰ Завершенный:</b> {finish.strftime('%H:%M:%S')}\n\n"
                         f"<b>🕓 Общее затраченное время:</b> {farq.seconds} секунды", reply_markup=GoToAdminPanel)


@dp.callback_query_handler(state='*', text='oddiy_habar')
async def oddiy_habar(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text("""
<b>📣 Вы можете отправить объявление</b>


<b>🔑Ключевые слова:</b> <i>
    ⏰Время: {{time}} заменяет сообщение временем, когда это сообщение дошло до пользователя (пример: 18:39).
    📅Дата: {{date}} заменяет сообщение на дату, когда это сообщение было отправлено пользователю (пример: 25.11.2023).
    📛Имя: {{name}} заменит это сообщение именем пользователя.
    🔗Mention: {{mention}} заменяет это сообщение ссылкой на пользователя.
    🖇Имя пользователя: {{username}} заменяет это сообщение именем пользователя.
    🆔 Идентификатор: {{id}} заменит это сообщение идентификатором пользователя.
    👥Пользователи: {{users}} заменит это сообщение количеством пользователей в базе данных.
</i>
""", reply_markup=GoToAdminPanel)
    await sendAd.text.set()


@dp.message_handler(state=sendAd.text, content_types=ContentTypes.ANY)
async def rek_text(message: Message, state: FSMContext):
    await state.finish()
    users = db.select_all_users()
    x = 0
    y = 0
    start = datetime.now(pytz.timezone('Asia/Tashkent'))
    i = await message.answer("🔰 Объявление отправляется, подождите...")
    skip = InlineKeyboardMarkup().add(InlineKeyboardButton("❌", callback_data="skip"))
    count = str(db.count_users())
    for user in users:
        try:
            user_data  = await bot.get_chat(user[0])
            time = datetime.now(pytz.timezone('Asia/Tashkent'))
            ad = message.html_text
            ad = ad.replace("{{time}}",str(time.strftime('%H:%M:%S')))
            ad = ad.replace("{{date}}",str(time.date()))
            ad = ad.replace("{{name}}",str(user_data.full_name))
            ad = ad.replace("{{mention}}",str(user_data.get_mention()))
            ad = ad.replace("{{username}}",str(user_data.username))
            ad = ad.replace("{{id}}",str(user_data.id))
            ad = ad.replace("{{users}}",count[0])
            msg = await bot.send_message(chat_id=user[0],text=ad)
            x += 1
        except Exception as e:
            print(e)
            y += 1
        await asyncio.sleep(0.05)
    finish = datetime.now(pytz.timezone('Asia/Tashkent'))
    farq = finish - start
    await message.answer(f"<b>📣 Реклама отправлена</b>\n\n"
                         f"✅ Принял: {x} ta\n"
                         f"❌ Не удалось отправить: {y} ta\n\n"
                         f"<b>⏰ Начал:</b> {start.strftime('%H:%M:%S')}\n"
                         f"<b>⏰ Завершенный:</b> {finish.strftime('%H:%M:%S')}\n\n"
                         f"<b>🕓 Общее затраченное время:</b> {farq.seconds} soniya", reply_markup=GoToAdminPanel)


@dp.callback_query_handler(state="*", text='admin:bot_stat')
async def bot_stat(call: CallbackQuery, state: FSMContext):
    await state.finish()
    count = db.count_users()[0]
    users = db.select_all_users()
    x = 0
    y = 0
    for user in users:
        try:
            await bot.get_chat(user[0])
            x += 1
        except:
            y += 1
    await call.answer(f"✅ Aktiv: {x}\n"
                      f"❌ Bloklangan: {y}\n"
                      f"➖➖➖➖➖➖\n"
                      f"Umumiy: {count} ", show_alert=True)


@dp.callback_query_handler(state='*', text='admin:delete_users')
async def delete_users(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text("<b>✅ Подтверждение</b>\n\n"
                                 "Введите код подтверждения, чтобы удалить пользователей бота", reply_markup=GoToAdminPanel)
    await verifyDeleteUsers.code.set()


@dp.message_handler(state=verifyDeleteUsers.code)
async def verifyCode(message: Message):
    if message.text == "8FSD778FSJ":
        await message.answer("Код правильный. Теперь вы можете удалять пользователей, нажав кнопку ниже.", reply_markup=DeleteUsers)
    else:
        await message.answer("Код неправильный. Попробуйте еще раз или отмените", reply_markup=backDelete)
        await verifyDeleteUsers.code.set()


@dp.callback_query_handler(state='*', text='delete:verify')
async def deleteVerify(call: CallbackQuery, state: FSMContext):
    await state.finish()
    db.delete_users()
    textm = await call.message.edit_text("✅ Пользователи бота удалены")
    await asyncio.sleep(2)
    await textm.edit_text(f"👋🏻 Здравствуйте, {call.from_user.full_name}! Добро пожаловать в панель администратора", reply_markup=AdminPanel)


@dp.callback_query_handler(state='*', text='admin:base')
async def base(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text("В каком типе вы хотите загрузить базу", reply_markup=BaseType)


@dp.callback_query_handler(state='*', text='database')
async def database(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    doc = InputFile('data/main.db')
    await call.message.answer_document(document=doc, caption="<b>main.db</b>\n"
                                                             "База загружена")
    await call.message.answer(f"👋🏻 Здравствуйте, {call.from_user.full_name}! Добро пожаловать в панель администратора", reply_markup=AdminPanel)


@dp.callback_query_handler(state='*', text='excel')
async def excel(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    users = db.select_all_users()
    workbook = xl.Workbook("users.xlsx")
    bold_format = workbook.add_format({'bold': True})
    worksheet = workbook.add_worksheet("Users")
    worksheet.write('A1', 'ID', bold_format)
    worksheet.write('B1', 'Имя', bold_format)
    worksheet.write('C1', 'Имя пользователя', bold_format)
    rowIndex = 2
    for user in users:
        tg_id = user[0]
        fullname = user[1]
        username = user[2]

        worksheet.write('A' + str(rowIndex), tg_id)
        worksheet.write('B' + str(rowIndex), fullname)
        worksheet.write('C' + str(rowIndex), f"@{username}")

        rowIndex += 1
    workbook.close()
    file = InputFile(path_or_bytesio="users.xlsx")
    await call.message.answer_document(document=file, caption="<b>users.xlsx</b>\n"
                                                              "в формате Excel")
    os.remove(path="users.xlsx")
    await call.message.answer(f"👋🏻 Здравствуйте, {call.from_user.full_name}! Добро пожаловать в панель администратора", reply_markup=AdminPanel)


@dp.callback_query_handler(state='*', text='admin:send_user')
async def send_user_func(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text("<b>🆔 ID</b>\n\n"
                                 "Введите свой идентификатор пользователя", reply_markup=backDelete)
    await send_user.id.set()


@dp.message_handler(state=send_user.id)
async def id(message: Message, state: FSMContext):
    await state.update_data(id=message.text)

    await message.answer(f"<b>📝 СООБЩЕНИЕ</b>\n\n"
                         f"[<code>{message.text}</code>] Отправьте сообщение, которое хотите отправить на ID",
                         reply_markup=backDelete)
    await send_user.habar.set()


@dp.message_handler(state=send_user.habar)
async def habar(message: Message, state: FSMContext):
    await state.update_data(habar=message.text)

    data = await state.get_data()
    id = data.get('id')
    habar = data.get('habar')
    status = bool
    try:
        await bot.send_message(chat_id=id, text=f"#admin_message\n"
                                                f"Админ отправил вам сообщение\n\n"
                                                f"<b>📝 СООБЩЕНИЕ:</b> {habar}\n\n"
                                                f"‼️ Если вы хотите написать ответ администратору, нажмите кнопку ниже👇", reply_markup=answer_admin)
        status = True
    except aiogram.exceptions.ChatNotFound:
        status = False
        await message.answer(f"<b>❌ ID не найден</b>\n\n"
                             f"[<code>{id}</code>] Идентификатор не найден\n"
                             f"Или этого пользователя нет в боте\n\n"
                             f"<i>Отправить другой идентификатор</i>", reply_markup=GoToAdminPanel)
        await send_user.id.set()
    except:
        status = False
        await message.answer(f"<b>❌ Неизвестная ошибка</b>\n\n"
                             f"Что-то пошло не так\n\n"
                             f"<i>Отправить другой идентификатор</i>", reply_markup=GoToAdminPanel)
        await send_user.id.set()
    if status:
        await message.answer(f"<b>✅ Отправлено</b>\n\n"
                             f"ИДЕНТИФИКАТОР: [<code>{id}</code>]\n"
                             f"Сообщение: {habar}\n\n"
                             f"Ваше сообщение было отправлено успешно")
        await state.finish()
        await message.answer(f"👋🏻 Здравствуйте, {message.from_user.full_name}! Добро пожаловать в панель администратора", reply_markup=AdminPanel)


@dp.callback_query_handler(state='*', text='answer_admin')
async def answeradmin(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"<b>📝 СООБЩЕНИЕ</b>\n\n"
                                 f"Введите сообщение, которое хотите написать администратору", reply_markup=back_user)
    await answer.habar.set()


@dp.message_handler(state=answer.habar)
async def adminhabar(message: Message, state: FSMContext):
    await state.finish()
    status = bool
    try:
        status = True
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=f"🆕 Новое сообщение!\n"
                                                       f"🙍🏻‍♂️ ИМЯ: {message.from_user.get_mention()}\n"
                                                       f"⏺ Имя пользователя: @{message.from_user.username}\n"
                                                       f"🆔 Идентификатор: [<code>{message.from_user.id}</code>]\n\n"
                                                       f"📄 Сообщение: {message.text}")
    except:
        status = False
    if status:
        await message.answer(f"<b>✅ Отправлено</b>\n\n"
                             f"Сообщение: {message.text}\n\n"
                             f"Ваше сообщение было отправлено успешно")
    else:
        await message.answer("<b>❌ Ошибка</b>\n\n"
                             "Что-то пошло не так", reply_markup=back_user)
