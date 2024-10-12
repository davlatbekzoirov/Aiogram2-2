from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
vkontakte = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton("🇰🇿 Kazakhstan(KZ)",callback_data="country:kazakhstan:vkontakte"),
		InlineKeyboardButton("🇮🇳 India(IN)",callback_data="country:india:vkontakte"),
	],
	[
		InlineKeyboardButton("🇳🇱 Netherlands(NL)",callback_data="country:netherlands:vkontakte"),
		InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:vkontakte"),
	],
	[
		InlineKeyboardButton("🇪🇪 Estonia(EE)",callback_data="country:estonia:vkontakte"),
		InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="country:kyrgyzstan:vkontakte"),
	],
	[
		InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="country:brazil:vkontakte"),
	],
	[
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
	],
])

tiktok = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="country:indonesia:tiktok"),
		InlineKeyboardButton("🇻🇳 Vietnam(VN)",callback_data="country:vietnam:tiktok")
	],
	[
		InlineKeyboardButton("🇮🇳 India(IN)",callback_data="country:india:tiktok"),

	],
	[
        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:tiktok"),

        ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])