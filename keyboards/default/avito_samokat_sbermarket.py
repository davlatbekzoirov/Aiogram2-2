from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
avito = InlineKeyboardMarkup(inline_keyboard=[
    [
    	InlineKeyboardButton("🇷🇺 Russia Federation(RU)",callback_data="country:russia:avito"),

        

    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    ]
])
sbermarket = InlineKeyboardMarkup(inline_keyboard=[
    [
    	InlineKeyboardButton("🇷🇺 Russia Federation(RU)",callback_data="country:russia:sbermarket"),

        
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])