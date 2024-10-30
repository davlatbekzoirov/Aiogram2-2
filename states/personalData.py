from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalDataUz(StatesGroup):
    fullNameUz = State() 
    phoneNumUz = State() 

class PersonalDataRu(StatesGroup):
    fullNameRu = State() 
    phoneNumRu = State() 

class send_forwad(StatesGroup):
    text = State()

class sendAd(StatesGroup):
    text = State()

class verifyDeleteUsers(StatesGroup):
    code = State()

class send_user(StatesGroup):
    id = State()
    habar = State()

class answer(StatesGroup):
    habar = State()
    
class AddPostState(StatesGroup):
    waiting_for_coursename = State()
    waiting_for_text = State()
    waiting_for_image = State()
    
class AddPostStateUz(StatesGroup):
    waiting_for_coursenameUz = State()
    waiting_for_textUz = State()
    waiting_for_imageUz = State()
