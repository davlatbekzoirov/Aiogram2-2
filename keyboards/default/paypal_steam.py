from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


steam = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton("🇦🇷 Argentinas(AR)",callback_data="country:argentina:steam"),

        
	],
	[
        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:steam"),

	],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    ]
])