import logging
from aiogram.types import CallbackQuery,Message,ParseMode
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from keyboards.default.buttons import buttons,panel_tugma,ortga_to_main,numbers_list_one,numbers_list_two,numbers_list_one_admin,numbers_list_two_admin,ortga_to_panel
from datetime import datetime
from loader import dp,db,bot,balance
from data.config import ADMINS,fivesimnettoken as token
import pytz
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from utils.api import get_balance
from time import sleep
import datetime as dt
import requests
from keyboards.inline.admin_keys import AdminPanel
@dp.callback_query_handler(state='*', text="ortga_to_panel")
async def adminPanelfunc(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer(f"👋🏻 Здравствуйте, {call.from_user.full_name}! Добро пожаловать в панель администратора", reply_markup=AdminPanel)

@dp.callback_query_handler(text="buy_number")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("♦️ Нажмите нужную кнопку!",reply_markup=numbers_list_one)
@dp.callback_query_handler(text="buy_number")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("♦️ Нажмите нужную кнопку!",reply_markup=numbers_list_one)
@dp.callback_query_handler(text="next")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔜 Перенесено на следующую страницу!",reply_markup=numbers_list_two)
@dp.callback_query_handler(text="previus")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся на предыдущую страницу!",reply_markup=numbers_list_one)

@dp.callback_query_handler(text="next_edit")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔜 Перенесено на следующую страницу!",reply_markup=numbers_list_two_admin)
@dp.callback_query_handler(text="previus_edit")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся на предыдущую страницу!",reply_markup=numbers_list_one_admin)
@dp.callback_query_handler(state="*",text="ortga_to_main")
async def stats_users(call:types.CallbackQuery,state:FSMContext):
    await state.finish()
    await call.answer(cache_time=30)
    await call.message.delete()
    name = call.from_user.full_name
    user_id = call.from_user.id
    user_balance = balance.get_balance(user_id=user_id)
    await call.message.answer_photo(
        'https://telegra.ph/file/b8c5c14681deb42eb67c3.jpg',caption=f"""
📛Ваше имя: <i>{name}</i>
💰Ваш баланс: {round(float(user_balance)*100)/100} ₽

🆔Идентификационный номер: <code>{user_id}</code>""",reply_markup=buttons)
@dp.callback_query_handler(text="ortga_to_main")
async def stats_users(call:types.CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    user_id = call.from_user.id
    user_balance = balance.get_balance(user_id=user_id)
    await call.message.answer_photo(
        'https://telegra.ph/file/b8c5c14681deb42eb67c3.jpg',caption=f"""
📛Ваше имя: <i>{name}</i>
💰Ваш баланс: {round(float(user_balance)*100)/100} ₽

🆔Идентификационный номер: <code>{user_id}</code>""",reply_markup=buttons)
@dp.callback_query_handler(state='*',text="ortga_panel")
async def send_ad_to_all(call: types.CallbackQuery,state:FSMContext):
    await state.finish()
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Хорошo вернулся",reply_markup=panel_tugma)
@dp.callback_query_handler(text="ortga_panel")
async def send_ad_to_all(call: types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Хорошo вернулся",reply_markup=panel_tugma)
@dp.callback_query_handler(text="ortga_to_social_one_admin")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся",reply_markup=numbers_list_one_admin)
@dp.callback_query_handler(text="ortga_to_social_two_admin")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся",reply_markup=numbers_list_two_admin)
@dp.callback_query_handler(text="ortga_to_social_one")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся",reply_markup=numbers_list_one)
@dp.callback_query_handler(text="ortga_to_social_two")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся",reply_markup=numbers_list_two)
@dp.callback_query_handler(text="balance")
async def bot_stat(call: types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    bot_start_date = dt.date(2023, 8, 25)
    farq = dt.date.today() - bot_start_date
    user_balance = balance.get_balance(user_id=call.from_user.id)
    await call.message.answer(f"""
<b>📛 Ваше имя:</b> <i>{call.message.chat.first_name}</i>
<b>✊ Ваше имя пользователя:</b> @{call.message.chat.username}
<b>🆔 Ваш идентификатор:</b> <code>{call.message.chat.id}</code>
<b>💰 Ваш баланс:</b> <tg-spoiler>{round(float(user_balance)*100)/100} ₽</tg-spoiler>
➖➖➖➖➖➖➖➖
<b>⏸ Запуск бота:</b>{bot_start_date}
<b>📆 Текущее время:</b>20{dt.datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%y-%m-%d %H:%M')}
🗓 Бот работает <b>{farq.days}</b> дней
""",reply_markup=ortga_to_main)

def dollar_to_rub(amount_in_dollar):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        rub_rate = data['rates']['RUB']
        amount_in_rub = float(amount_in_dollar) * float(rub_rate)
        return amount_in_rub
    else:
        return 0

@dp.callback_query_handler(text="balance_api")
async def data_dls_tools(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    balance = await get_balance() 
    balance = dollar_to_rub(balance.balance)
    await call.message.answer(f"💰 Balans: {balance} ₽",reply_markup=ortga_to_panel)
keyboard_qwz = InlineKeyboardMarkup(row_width=1)
keyboard_qwz.add(InlineKeyboardButton(text="🗒 Правила",callback_data="rules"))
keyboard_qwz.add(InlineKeyboardButton(text="📔 Инструкция",callback_data="instruction"))
keyboard_qwz.add(InlineKeyboardButton(text="🔙 Hазад",callback_data="ortga_to_main"))
keyboard_qwerty = InlineKeyboardMarkup(row_width=1)
keyboard_qwerty.add(InlineKeyboardButton(text="📱 Как купить номер",callback_data="intructionbuy"))
keyboard_qwerty.add(InlineKeyboardButton(text="💵 Как пополнить баланс",callback_data="instructiontopup"))
keyboard_qwerty.add(InlineKeyboardButton(text="🔙 Hазад",callback_data="ortga_to_main"))



@dp.callback_query_handler(text="instruction_rules")
async def data_dls_tools(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужный раздел и нажмите на него!",reply_markup=keyboard_qwz)
@dp.callback_query_handler(text="rules")
async def data_dls_tools(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer("""
<b>Пользовательское соглашение</b>
1. Порядок проведения активации следующий:
- 1.1. Нажать на кнопку "📱 Купить номер", выбрать необходимую страну
- 1.2  Bыбрать необходимый сервис или страна
- 1.3  Нажать на кнопку "💳 Платить", далее у вас появится номер
- 1.4  Дождаться поступления смс и отображения его содержания
- 1.5  Если вам необходимо получить больше одной смс, следует нажать на кнопку "🔄 Обновить"
- 1.6  Если все верно и вы хотите закончить работу с данным сервисом необходимо нажать кнопку "❌ Отменить  заказ", либо активация успешно завершается автоматически по истечении времени (15 минут)
- 1.7  Максимальное время ожидания поступления смс составляет 15 минут, после чего выделение номера завершается.

2. Стоимость активаций списывается согласно прейскуранту (Отображается до покупки номера).
- 2.1 Деньги списываются с баланса по завершению операции (п.1.4,1.5 регламента).

3. Если номер выделен, но не использован (то есть вы не увидели код из смс), вы можете в любой момент oтменить  операцию без какого-либо штрафа. В случае злоупотребления или перебирания номеров в поиске лучшего, будут применены санкции на усмотрение модератора.

4. При использовании данного бота вы даёте согласие на получение рекламных материалов от @Ser4ikShopBot.

5. История операций с номерами хранится в вашем аккаунте и доступна, необходимо нажать на кнопку "📞 Купленные номера". История активаций хранится бессрочно и не подлежит удалению на сервере

6.  Категорически запрещенно использование данного сервиса @Ser4ikShopBot в любых противоправных целях.
- 6.1 Также запрещенно использовать данные номера с последующими целями, нарушающие Уголовный Кодекс Российской Федерации: обман, мошенничество и прочие (УК РФ 138, УК РФ 159, УК РФ 228, УК РФ 272, УК РФ 273, УК РФ 274)
- 6.2 Запрещено использование сервиса для осуществления платных подписок.

7. Мы не несем ответственности за созданные аккаунты, все действия, включая возможные блокировки, осуществляются исключительно на страх и риск конечного пользователя, который приобрел активацию

8. Возврат денежных средств предусмотрен только при подаче заявки на ser4iksup@gmail.com

9. Возврат денежных средств за ошибки пользователей - не предусмотрен
""",reply_markup=ortga_to_main)

@dp.callback_query_handler(text="instruction")
async def data_dls_tools(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужный раздел и нажмите на него!",reply_markup=keyboard_qwerty)
@dp.callback_query_handler(text="intructionbuy")
async def data_dls_tools(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer_video("BAACAgIAAxkBAAEY60Vl7Krq2LrRY1N1JnIKDiT29bwblwACIkcAArAJUUsmLMNBNKEJCjQE",caption="""
<b>‼️ ПОШАГОВАЯ ИНСТРУКЦИЯ ‼️ </b>
Тут можно увидеть, как купить номер в боте, на примере:
(🛎 Telegram —» 🇮🇩 Indonesia)


<i>@Ser4ikShopBot - Cамые качественные виртуальные номера у нас </i>
""",reply_markup=ortga_to_main)
@dp.callback_query_handler(text="instructiontopup")
async def data_dls_tools(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer_video("BAACAgIAAxkBAAEY60Zl7Krq7-ilYm_MTMZ3qKTHYys5zgAC1kIAArAJWUtgrl-KHX_NcTQE",caption="""
<b>‼️ ПОШАГОВАЯ ИНСТРУКЦИЯ ‼️ </b>
Тут можно увидеть, как пополнить баланс в боте.


<i>@Ser4ikShopBot - Cамые качественные виртуальные номера у нас </i>
""",reply_markup=ortga_to_main)