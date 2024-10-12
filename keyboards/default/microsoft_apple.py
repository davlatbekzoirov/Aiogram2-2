from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
microsoft = InlineKeyboardMarkup(inline_keyboard=[
    [
    	InlineKeyboardButton(text="🇰🇬 Kyrgyzstan(KG)",callback_data="country:kyrgyzstan:microsoft"),
    	InlineKeyboardButton(text="🇻🇳 Vietnam(VN)",callback_data="country:Vietnam:microsoft")

    ],
    [
    	InlineKeyboardButton(text="🇪🇪 Estonia(EE)",callback_data="country:estonia:microsoft"),
    	InlineKeyboardButton(text="🇨🇦 Canada(CA)",callback_data="country:canada:microsoft")

    ],
    [
    	InlineKeyboardButton(text="🇮🇳 India(IN)",callback_data="country:india:microsoft"),
    	InlineKeyboardButton(text="🇮🇩 Indonesia(ID)",callback_data="country:indonesia:microsoft")

    ],
    [
    	InlineKeyboardButton(text="🇳🇱 Netetherlands(NL)",callback_data="country:netherlands:microsoft"),
    	InlineKeyboardButton(text="🇷🇺 Russian Federation(RU)",callback_data="country:russia:microsoft")

    ],
    [
    	InlineKeyboardButton(text="🇧🇷 Brazil(BR)",callback_data="country:brazil:microsoft"),
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")

    ]
])

apple = InlineKeyboardMarkup(inline_keyboard=[
    [
    	InlineKeyboardButton(text="🇰🇭 Cambodia(KH)",callback_data="country:combodia:apple"),

    ],
    [
    	InlineKeyboardButton(text="🇮🇳 India(IN)",callback_data="country:india:apple"),

    ],
    [
        InlineKeyboardButton(text="🇻🇳 Vietnam(VN)",callback_data="country:Vietnam:apple")

    ],
    [
        InlineKeyboardButton(text="🇷🇺 Russian Federation(RU)",callback_data="country:russia:apple")

    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")

    ]
])