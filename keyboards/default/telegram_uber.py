from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
telegram = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇿🇦 South Africa(ZA)",callback_data="country:africa:telegram"),
        InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="country:kyrgyzstan:telegram")

      
    ],
    [
        InlineKeyboardButton("🇹🇷 Turkey(TR)",callback_data="country:turkey:telegram"),
        InlineKeyboardButton("🇦🇷 Argentina(AR)",callback_data="country:argentina:telegram")

      
    ],
    [
        InlineKeyboardButton("🇮🇳 India(IN)",callback_data="country:india:telegram"),
        InlineKeyboardButton("🇻🇳 Vietnam(VN)",callback_data="country:Vietnam:telegram")

      
    ],
    [
        InlineKeyboardButton("🇹🇭 Thailand(TH)",callback_data="country:thailand:telegram"),
        InlineKeyboardButton("🇲🇾 Malaysia(MY)",callback_data="country:malaysia:telegram")

      
    ],
    [
        InlineKeyboardButton("🇨🇬 Congo(CG)",callback_data="country:congo:telegram"),
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="country:brazil:telegram")

      
    ],
    [
        InlineKeyboardButton("🇺🇦 Ukraine(UA)",callback_data="country:ukraine:telegram"),
        InlineKeyboardButton("🇪🇬 Egypt(EG)",callback_data="country:egypt:telegram")

      
    ],
    [
        InlineKeyboardButton("🇵🇭 Philippens(PH)",callback_data="country:philippens:telegram"),
        InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="country:indonesia:telegram")

      
    ],
    [
        InlineKeyboardButton("🇰🇿 Kazakhstan(KZ)",callback_data="country:kazakhstan:telegram"),
        InlineKeyboardButton("🇨🇦 Canada(CA)",callback_data="country:canada:telegram")

      
    ],
    [
        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:telegram"),
        InlineKeyboardButton("🇷🇴 Romania(RO)",callback_data="country:romania:telegram")

      
    ],
    [
        
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="country:usa:telegram"),
        InlineKeyboardButton("🇭🇰 Hong Kong(HK)",callback_data="country:hongkong:telegram")

      
    ],

    [
        InlineKeyboardButton("🇵🇰 Pakistan(PK)",callback_data="country:pakistan:telegram")

      
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])

uber = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text="🇩🇪 Germany(DE)",callback_data="country:germany:uber"),
	],
    [
        InlineKeyboardButton(text="🇷🇺 Russia(RU)",callback_data="country:russia:uber"),

    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]


])

