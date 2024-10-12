from environs import Env
env = Env()
env.read_env()
BOT_TOKEN = env.str("BOT_TOKEN")  
ADMINS = env.list("ADMINS") 
IP = env.str("ip")  
CHANELS=['@saffffffsaffas']
fivesimnettoken = env.str('SIM_NET_API_TOKEN')