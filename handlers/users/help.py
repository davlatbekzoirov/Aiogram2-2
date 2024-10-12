# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandHelp

# from loader import dp


# @dp.message_handler(CommandHelp())
# async def bot_help(message: types.Message):
#     text = ("Kоманды:",
#             "/start - запуск бота",
#             "/help - помощь")
    
#     await message.answer("\n".join(text))
# from docx import Document
# import asyncio
# import random
# from PyPDF2 import PdfReader

# document = Document()

# async def pdf_to_docx(pdf_path):
#     id = random.randint(1, 1000000)
#     docx_file = f"word/docx{id}.docx"
#     try:
#         pdf = PdfReader(pdf_path)
#         for page in pdf.pages:
#             text = page.extract_text()
#             document.add_paragraph(text)
#         return docx_file
#     except Exception as e:
#         return f"Xatolik: {e}"
 
#     document.save(docx_file)
# async def async_convert(pdf_path):
#     tasklar = []
#     tasklar.append(asyncio.create_task(pdf_to_docx(pdf_path)))
#     return await asyncio.gather(*tasklar)
# print(asyncio.run(async_convert("BQACAgIAAxkBAAILWmWSc3mOg681lKcud3R_vgtvwg9oAALZPAACJgmRSOH7wlYBBhY4NAQ.pdf")))
