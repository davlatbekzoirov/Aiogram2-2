from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from .translitirate import to_cyrillic, to_latin
from loader import dp, bot
from tracemalloc import BaseFilter
from typing import Union
from aiogram.types import Message


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name} Lotin krill botiga xush kelibsiz\nIltimos menga krillcha yoki lotincha so'z yuboring men uni almashtirib beraman 🔄")

class ContentTypesFilter(BaseFilter):
    def __init__(self, content_types: Union[str, list]):
        self.content_types = content_types
    async def __call__(self, message: Message) -> bool:
        if isinstance(self.content_types, str):
            print(message)
            return message.content_type == self.content_types
        else:
            return message.content_type in self.content_types

@dp.message_handler(ContentTypesFilter(content_types=['text']))
async def translit(message: types.Message):
    text = message.text
    response = to_cyrillic(text) if text.isascii() else to_latin(text)
    await message.answer(response)