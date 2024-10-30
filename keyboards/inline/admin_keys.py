from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import bot

AdminPanel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📣 Отправить объявление", callback_data='admin:send_ad'),
            InlineKeyboardButton(text="🗄 Загрузка базы", callback_data='admin:base'),

        ],
        [
            InlineKeyboardButton(text="❌ Удаление пользователей", callback_data='admin:delete_users'),
            InlineKeyboardButton(text="🚫 Блокировка", callback_data='admin:block'),

        ],
        [
            InlineKeyboardButton(text="📢 Настройка канала",callback_data="admin:channels")

        ],
        [
            InlineKeyboardButton(text="👤 Отправьте сообщение пользователю", callback_data='admin:send_user'),
        ],
        [
            InlineKeyboardButton(text="👤 Пользовательские настройки",callback_data='users_settings'),

        ],
        [
            InlineKeyboardButton(text="➕Добавить пост 🇷🇺",callback_data='add_posts_ru'),
        ],
        [
            InlineKeyboardButton(text="➕Добавить пост 🇺🇿",callback_data='add_posts_uz'),
        ]
    ],
)

GoToAdminPanel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Вернуться в панель администратора", callback_data='GoToAdminPanel')
        ]
    ]
)

SendAd_Type = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📋 Простые новости", callback_data='oddiy_habar'),
            InlineKeyboardButton(text="↪️ Переслать сообщение", callback_data='forward_habar')
        ],
        [
            InlineKeyboardButton(text="◀️ Вернуться в панель администратора", callback_data='GoToAdminPanel')
        ]
    ],
)


backDelete = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚫 Отмена", callback_data='GoToAdminPanel')
        ]
    ]
)

DeleteUsers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Подтверждение", callback_data='delete:verify'),
            InlineKeyboardButton(text="❌ Отмена", callback_data='GoToAdminPanel')
        ]
    ]
)

BaseType = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⚙️ База данных", callback_data='database'),
            InlineKeyboardButton(text="📑 Эксель", callback_data='excel')
        ],
        [
            InlineKeyboardButton(text="◀️ Назад", callback_data="GoToAdminPanel")
        ]
    ]
)

answer_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👮‍♂️ Ответ администратору", callback_data="answer_admin")
        ]
    ]
)

back_user = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Назад", callback_data='user_back')
        ]
    ]
)




