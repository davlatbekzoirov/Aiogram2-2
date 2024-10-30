# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart, Command
# from states.test import TestStates
# from loader import *
# from aiogram.dispatcher import FSMContext
# from keyboards.inline.test import *
# import tracemalloc
# import asyncio, sys, logging
# from PIL import Image, ImageDraw, ImageFont
# from io import BytesIO
#
# tracemalloc.start()
#
# def get_all_correct_answers(user_answers):
#     correct_answers = {
#         1: "gvido_van_rosum",
#         2: "interpretatsion_til",
#         3: "generator",
#         4: "yozish_va_oqish",
#         5: "zero",
#         6: "tfse",
#         7: "five",
#         8: "abracadabra",
#         9: "xatolik_kelib_chiqadi",
#         10: "tf",
#         11: "xatolik_kelib_chiqadi1"
#     }
#
#     score = 0
#     for question_id, user_answer in user_answers.items():
#         if correct_answers.get(question_id) == user_answer:
#             score += 1
#
#     return score
#
#
# async def sertificat(full_name):
#     img = Image.open("sertifikat.png")
#     draw = ImageDraw.Draw(img)
#     txt = full_name
#     fnt = ImageFont.truetype("roboto2.ttf", 80)
#     draw.text((1000-len(txt)*20, 600), txt, font=fnt, fill=(0, 0, 0))
#
#     description = """
#     2024-yil 5-martdan 7-martga qadar "SUSYS-ACADEMY" ma'suliyati cheklangan jamiyati
#     "SIFAT" O'quv markazi tomonidan Navoiy shahrida tashkil etilgan "Elektron hukumat"
#     tizimini joriy etish bo' yicha o'quv kursini tamomladi
#     """
#     fnt2 = ImageFont.truetype("roboto2.ttf", 40)
#     draw.text((200, 800), description, font=fnt2, fill=(0, 0, 0))
#     buffer = BytesIO()
#     img.save(buffer, format='PNG')
#     buffer.seek(0)
#     return buffer
#
# @dp.message_handler(Command('test'), state=None)
# async def enter_test(message: types.Message):
#     await message.answer("""Kayfiyatlar qalay ;)
# Xo'sh, hozir siz bor yo'g'i 11 dona test ishlaysiz, lekin shuning o'zi yetarli bo'ladi. Demak, testni boshlashdan avval tanishib olsak. Ism va familiyangizni Ism Familiya shaklida yozib jo'nating. Masalan:
# Eshmatjon Toshmatov
#
# Iltimos, ma'lumotni to'g'ri kiriting, ism va familiyangiz sertifikatingizga yoziladi.
# """)
#     await TestStates.fullname.set()
#
# @dp.message_handler(state=TestStates.fullname)
# async def answer_fullname(message: types.Message, state: FSMContext):
#     await state.update_data(full_name=message.text)
#     question_id = 1
#     correct_answer_data = await ans.get_user_answers(question_id)
#     correct_answer = correct_answer_data[0] if correct_answer_data else None
#     msg = "1-savol\nPython asoschisi?"
#     await message.answer(msg, reply_markup=question1)
#     await TestStates.next()
#
# @dp.callback_query_handler(lambda query: query.data in ['linus_torvalds', 'bill_geyts', 'steven_houking', 'gvido_van_rosum'], state=TestStates.QUESTION_1)
# async def answer_question1(call: types.CallbackQuery, state: FSMContext):
#     user_answer = call.data
#     question_id = 1
#     correct_answer_data = await ans.get_user_answers(question_id)
#     correct_answer = correct_answer_data[0] if correct_answer_data else None
#     if user_answer == correct_answer:
#         score_data = await state.get_data()
#         score = score_data.get('score', 0)
#         score += 1
#         await state.update_data(score=score)
#     await call.message.delete()
#     msg = "2-savol\nPython bu -"
#     await call.message.answer(msg, reply_markup=question2)
#     await TestStates.next()
#
#
# @dp.callback_query_handler(lambda query: query.data in ['interpretatsion_til', 'kompliyatsion_til', 'ilon'], state=TestStates.QUESTION_2)
# async def answer_question2(call: types.CallbackQuery, state: FSMContext):
#     question_id = 3
#     user_answer = call.data
#     correct_answer_data = await ans.get_user_answers(question_id)
#     correct_answer = correct_answer_data[0] if correct_answer_data else None
#     if user_answer == correct_answer:
#         score_data = await state.get_data()
#         score = score_data.get('score', 0)
#         score += 1
#         await state.update_data(score=score)
#     await call.message.delete()
#     msg = "3-savol\nyield qanday tur hosil qilishda qo'llaniladi?"
#     await call.message.answer(msg, reply_markup=question3)
#     await TestStates.next()
#
# @dp.callback_query_handler(lambda query: query.data in ['sikl', 'generator', 'iterator', 'string'], state=TestStates.QUESTION_3)
# async def answer_question3(call: types.CallbackQuery, state: FSMContext):
#     question_id = 4
#     user_answer = call.data
#     correct_answer_data = await ans.get_user_answers(question_id)
#     correct_answer = correct_answer_data[0] if correct_answer_data else None
#     if user_answer == correct_answer:
#         score_data = await state.get_data()
#         score = score_data.get('score', 0)
#         score += 1
#         await state.update_data(score=score)
#     await call.message.delete()
#     msg = """4-savol\nfayl ochishda "w" rejimidan qanday maqsadda foydalaniladi?"""
#     await call.message.answer(msg, reply_markup=question4)
#     await TestStates.next()
#
# @dp.callback_query_handler(lambda query: query.data in ['oqish', 'yozish', 'yozish_va_oqish', 'bunday_rejim_yoq'], state=TestStates.QUESTION_4)
# async def answer_question4(call: types.CallbackQuery, state: FSMContext):
#     question_id = 5
#     user_answer = call.data
#     correct_answer_data = await ans.get_user_answers(question_id)
#     correct_answer = correct_answer_data[0] if correct_answer_data else None
#     if user_answer == correct_answer:
#         score_data = await state.get_data()
#         score = score_data.get('score', 0)
#         score += 1
#         await state.update_data(score=score)
#     await call.message.delete()
#     msg = """5-savol
# quyidagi ifodadan keyin "a" ning qiymati qanday bo'ladi:
# a = [1, 2][1 > 2]"""
#     await call.message.answer(msg, reply_markup=question5)
#     await TestStates.next()
#
# @dp.callback_query_handler(lambda query: query.data in ['dastur_xatolik_beradi', 'zero', 'first', 'second'], state=TestStates.QUESTION_5)
# async def answer_question5(call: types.CallbackQuery, state: FSMContext):
#     question_id = 6
#     user_answer = call.data
#     correct_answer_data = await ans.get_user_answers(question_id)
#     correct_answer = correct_answer_data[0] if correct_answer_data else None
#     if user_answer == correct_answer:
#         score_data = await state.get_data()
#         score = score_data.get('score', 0)
#         score += 1
#         await state.update_data(score=score)
#     await call.message.delete()
#     msg = """6-savol
# dastur natijasi qanday:
#
# silly_list=[i for i in range(2,9,2) if i%2]
# print(silly_list)"""
#     await call.message.answer(msg, reply_markup=question6)
#     await TestStates.next()
#
# @dp.callback_query_handler(lambda query: query.data in ['tfs', 'tfsn', 'tfse', 'bosh'], state=TestStates.QUESTION_6)
# async def answer_question6(call: types.CallbackQuery, state: FSMContext):
#     question_id = 7
#     user_answer = call.data
#     correct_answer_data = await ans.get_user_answers(question_id)
#     correct_answer = correct_answer_data[0] if correct_answer_data else None
#     if user_answer == correct_answer:
#         score_data = await state.get_data()
#         score = score_data.get('score', 0)
#         score += 1
#         await state.update_data(score=score)
#     await call.message.delete()
#     msg = "7-savol\nquyidagi dastur nechta qiymat chop etadi?"
#     msg +="""\nprint([x**2 for x in range(1, 11)])"""
#     await call.message.answer(msg, reply_markup=question7)
#     await TestStates.next()
#
# @dp.callback_query_handler(lambda query: query.data in ['five', 'one', 'ten1', 'question7'], state=TestStates.QUESTION_7)
# async def answer_question7(call: types.CallbackQuery, state: FSMContext):
#     question_id = 8
#     user_answer = call.data
#     correct_answer_data = await ans.get_user_answers(question_id)
#     correct_answer = correct_answer_data[0] if correct_answer_data else None
#     if user_answer == correct_answer:
#         score_data = await state.get_data()
#         score = score_data.get('score', 0)
#         score += 1
#         await state.update_data(score=score)
#     await call.message.delete()
#     msg = """8-savol
# dastur natijasi qanday?
#
# print("{1}{0}{1}".format("cad","abra"))"""
#     await call.message.answer(msg, reply_markup=question8)
#     await TestStates.next()
#
# @dp.callback_query_handler(lambda query: query.data in ['cadabracad', 'dastur_xato_tuzilgan', 'cadcad', 'abracadabra'], state=TestStates.QUESTION_8)
# async def answer_question8(call: types.CallbackQuery, state: FSMContext):
#     question_id = 9
#     user_answer = call.data
#     correct_answer_data = await ans.get_user_answers(question_id)
#     correct_answer = correct_answer_data[0] if correct_answer_data else None
#     if user_answer == correct_answer:
#         score_data = await state.get_data()
#         score = score_data.get('score', 0)
#         score += 1
#         await state.update_data(score=score)
#     await call.message.delete()
#     msg = """9-savol
# dastur natijasi qanday?
#
# def return_integer() -> int:
#   return "1"
#
# print(return_integer() + "2")"""
#     await call.message.answer(msg, reply_markup=question9)
#     await TestStates.next()
#
# @dp.callback_query_handler(lambda query: query.data in ['t', 'o', 'xatolik_kelib_chiqadi', 'tt'], state=TestStates.QUESTION_9)
# async def answer_question9(call: types.CallbackQuery, state: FSMContext):
#     question_id = 10
#     user_answer = call.data
#     correct_answer_data = await ans.get_user_answers(question_id)
#     correct_answer = correct_answer_data[0] if correct_answer_data else None
#     if user_answer == correct_answer:
#         score_data = await state.get_data()
#         score = score_data.get('score', 0)
#         score += 1
#         await state.update_data(score=score)
#     await call.message.delete()
#     msg = """10-savol
# dastur nechta son chop etadi?
#
# nums = list(range(10))
# nums2 = list(range(15))
# nums.extend(nums2)
# print(set(nums))"""
#     await call.message.answer(msg, reply_markup=question10)
#     await TestStates.next()
#
# @dp.callback_query_handler(lambda query: query.data in ['ten', 'tf', 'of', 'question10'], state=TestStates.QUESTION_10)
# async def answer_question10(call: types.CallbackQuery, state: FSMContext):
#     question_id = 11
#     user_answer = call.data
#     correct_answer_data = await ans.get_user_answers(question_id)
#     correct_answer = correct_answer_data[0] if correct_answer_data else None
#     if user_answer == correct_answer:
#         score_data = await state.get_data()
#         score = score_data.get('score', 0)
#         score += 1
#         await state.update_data(score=score)
#     await call.message.delete()
#     msg = """11-savol
# dastur natijasi qanday?
#
# a,*b,c=1,2,3,4,5
# print(b)"""
#     await call.message.answer(msg, reply_markup=question11)
#     await TestStates.next()
#
#
# @dp.callback_query_handler(lambda query: query.data in ['two', 'xatolik_kelib_chiqadi1', 'ttf', 'ttf1'], state=TestStates.QUESTION_11)
# async def answer_question11(call: types.CallbackQuery, state: FSMContext):
#     user_id = call.from_user.id
#     user_answer = call.data
#     question_id = 11
#     user_answers_data = await ans.get_user_answers(user_id)
#     user_answers_dict = {qa[0]: qa[1] for qa in user_answers_data}
#     correct_answers = get_all_correct_answers(user_answers_dict)
#     correct_answer = correct_answers.get(question_id)
#     if user_answer == correct_answer:
#         score_data = await state.get_data()
#         score = score_data.get('score', 0)
#         score += 1
#         await state.update_data(score=score)
#
#     score = get_all_correct_answers(user_answers)
#
#     user_answers_data = await ans.get_user_answers(user_id)
#     user_answers_dict = {qa[0]: qa[1] for qa in user_answers_data}
#
#     result_message = "You have completed the test. Here is the breakdown of your performance:\n\n"
#     for q_id, correct_ans in correct_answers.items():
#         result_message += f"Question {q_id}: "
#         if q_id in user_answers_dict:
#             user_ans = user_answers_dict[q_id]
#             if user_ans == correct_ans:
#                 result_message += "Correct\n"
#             else:
#                 result_message += f"Incorrect\nYour answer: {user_ans}\nCorrect answer: {correct_ans}\n"
#         else:
#             result_message += f"Question was not answered\nCorrect answer: {correct_ans}\n"
#
#     result_message += f"\nYour score: {score}/{len(correct_answers)}"
#
#     await call.message.delete()
#     await call.message.answer(result_message)
#
#     # Finish the state
#     await state.finish()
