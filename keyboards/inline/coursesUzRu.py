from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import itemUz, menu_cdUz
from handlers.users.adminPanel import add_postUz
from loader import add_postUz

def make_callback_data(level, category="0", subcategory="0", item_id="0"):
    return menu_cdUz.new(
        level=level, category=category, subcategory=subcategory, item_id=item_id
    )

# UZ - RU
# KURSLARNING RO'YXATI
# KURS XAQIDA > KURSGA YOZILISH, BOSH MENU, ORTGA

def categories_keyboard():
    CURRENT_LEVEL = 0

    markup = InlineKeyboardMarkup(row_width=1)

    categories = add_postUz.get_categories()
    for category in categories:
        number_of_items = add_postUz.count_products(category["category_code"])
        button_text = f"{category['category_name']}"

        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1, category=category["category_code"]
        )

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text="🏘 Boshga qaytish", callback_data="cancel"
        ),
        InlineKeyboardButton(
            text="📍 Bizning manzil", callback_data="mylocationUz"
        )
    )
    return markup

async def subcategories_keyboard(category):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=1)

    subcategories = await add_postUz.get_subcategories(category)
    for subcategory in subcategories:
        number_of_items = await add_postUz.count_products(
            category_code=category, subcategory_code=subcategory["subcategory_code"]
        )

        button_text = f"{subcategory['subcategory_name']}"

        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1,
            category=category,
            subcategory=subcategory["subcategory_code"],
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga", callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
        )
    )
    return markup

async def items_keyboard(category, subcategory):
    CURRENT_LEVEL = 2

    markup = InlineKeyboardMarkup(row_width=1)

    items = await add_postUz.get_products(category, subcategory)
    for item in items:
        button_text = f"{item['productname']} - ${item['price']}"

        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1,
            category=category,
            subcategory=subcategory,
            item_id=item["id"],
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1, category=category
            ),
        )
    )
    return markup


def item_keyboard(category, item_id):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(
        InlineKeyboardButton(
            text="💻 Kursga yozilish", callback_data="kursuz"
        ),
        InlineKeyboardButton(
            text="🔙 Ortga",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1, category=category
            ),
        ),
        InlineKeyboardButton(
           text="🏘 Boshga qaytish", callback_data="cancel"
        ),
    )
    return markup