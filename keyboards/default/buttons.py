from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("📱 Купить номер",callback_data="buy_number"),
        InlineKeyboardButton("🔝 Пополнить баланс",callback_data="top_balance"),

    ],
    [
        InlineKeyboardButton("📞 Купленные номера",callback_data="soldnumbers"),

        InlineKeyboardButton("💰 Мой баланс",callback_data="balance")
    ],
    [
        InlineKeyboardButton("🗒 Правила | Инструкция",callback_data="instruction_rules"),

    ]
])




ortga_to_panel =  InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_panel")        
    ]]
)
ortga_to_main =  InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_main")        
    ]]
)

panel_tugma = InlineKeyboardMarkup(
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
        InlineKeyboardButton(text="💰 Цены на номера",callback_data="number_prices"),

        InlineKeyboardButton(text="💰 Balans API ",callback_data="balance_api"),

        ],
        [
            InlineKeyboardButton(text="📢 Настройка канала",callback_data="admin:channels")

        ],
        [
            InlineKeyboardButton(text="👤 Отправьте сообщение пользователю", callback_data='admin:send_user'),
        ],
        [
        InlineKeyboardButton(text="👤 Пользовательские настройки",callback_data='users_settings'),

        ]
    ],
)



numbers_list_one = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🛎 Instagram",callback_data="instagram"),
        InlineKeyboardButton(text="🛎 Facebook",callback_data="facebook")
    ],
    [
        InlineKeyboardButton(text="🛎 Ebay",callback_data="ebay"),
        InlineKeyboardButton(text="🛎 Tinder",callback_data="tinder")

    ],
    [
        InlineKeyboardButton(text="🛎 Telegram",callback_data="telegram"),
        InlineKeyboardButton(text="🛎 Uber",callback_data="uber")
    ],
    [
        InlineKeyboardButton(text="🛎 Twitter",callback_data="twitter"),
        InlineKeyboardButton(text="🛎 WhatsApp",callback_data="whatsup")
    ],
    [
        InlineKeyboardButton(text="🛎 Vkontakte",callback_data="vkontakte"),
        InlineKeyboardButton(text="🛎 Tik Tok",callback_data="tiktok")
    ],

    [
        InlineKeyboardButton(text="🔜 Следующий",callback_data="next"),
    ],[

        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_main") 
]
])

numbers_list_two = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🛎 Yandex",callback_data="yandex"),
        InlineKeyboardButton(text="🛎 Google",callback_data="gmail"),

    ],
    [  
        InlineKeyboardButton(text="🛎 Amazon",callback_data="amazon"),
        InlineKeyboardButton(text="🛎 Discord",callback_data="discord")
    ],
    [
        InlineKeyboardButton(text="🛎 Microsoft",callback_data="microsoft"),
        InlineKeyboardButton(text="🛎 Apple",callback_data="apple")
    ],
    [
        InlineKeyboardButton(text="🛎 Avito",callback_data="avito"),
        InlineKeyboardButton(text="🛎 Steam",callback_data="steam")
        
    ],
    [
        InlineKeyboardButton(text="🛎 SberMarket",callback_data="sbermarket"),
 
    ],
    [
        InlineKeyboardButton(text="🔙 Предыдущий",callback_data="previus"),

    ],
    
    [

        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_main")  

    ]
])


numbers_list_one_admin = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🛎 Instagram",callback_data="instagram_edit"),
        InlineKeyboardButton(text="🛎 Facebook",callback_data="facebook_edit")
    ],
    [
        InlineKeyboardButton(text="🛎 Ebay",callback_data="ebay_edit"),
        InlineKeyboardButton(text="🛎 Tinder",callback_data="tinder_edit")

    ],
    [
        InlineKeyboardButton(text="🛎 Telegram",callback_data="telegram_edit"),
        InlineKeyboardButton(text="🛎 Uber",callback_data="uber_edit")
    ],
    [
        InlineKeyboardButton(text="🛎 Twitter",callback_data="twitter_edit"),
        InlineKeyboardButton(text="🛎 WhatsApp",callback_data="whatsup_edit")
    ],
    [
        InlineKeyboardButton(text="🛎 Vkontakte",callback_data="vkontakte_edit"),
        InlineKeyboardButton(text="🛎 Tik Tok",callback_data="tiktok_edit")
    ],
    [
        InlineKeyboardButton(text="🔜 Следующий",callback_data="next_edit"),
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_panel") 

    ]
])

numbers_list_two_admin = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🛎 Yandex",callback_data="yandex_edit"),
        InlineKeyboardButton(text="🛎 Google",callback_data="gmail_edit"),

    ], 
    [
        InlineKeyboardButton(text="🛎 Amazon",callback_data="amazon_edit"),
        InlineKeyboardButton(text="🛎 Discord",callback_data="discord_edit")
    ],
    [
        InlineKeyboardButton(text="🛎 Microsoft",callback_data="microsoft_edit"),
        InlineKeyboardButton(text="🛎 Apple",callback_data="apple_edit")
    ],
    [
        InlineKeyboardButton(text="🛎 Avito",callback_data="avito_edit"),
        InlineKeyboardButton(text="🛎 Steam",callback_data="steam_edit")
    
    ],
    [
        InlineKeyboardButton(text="🛎 SberMarket",callback_data="sbermarket_edit"),
 
    ],
    [
        InlineKeyboardButton(text="🔙 Предыдущий",callback_data="previus_edit"),

    ],

[
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_panel")  
]
])


