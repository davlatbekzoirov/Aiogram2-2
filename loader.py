from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.sqlite import *
from utils.db_api.sqlitestart import *
from utils.db_api.sqliteRu import *
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(path_to_db="main.db")
dbru = DatabaseRu(path_to_db="mainru.db")
dbstart = DatabaseStart(path_to_db="start.db")
# channels = Channel("data/channels.db")
# banuser = BanUser("data/banuser.db")
add_post = Add_post("data/add_post.db")
add_postUz = Add_post_Uz("UzPost.db")