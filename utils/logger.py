import logging
import os
from datetime import date


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
logging_dir = os.path.join(parent_dir, "logs") 

if not os.path.exists(logging_dir):
    os.makedirs(logging_dir)

logging_path = os.path.join(logging_dir, f'{date.today().strftime("%d-%m-%Y")}.log') 
handler = logging.FileHandler(logging_path)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt="%H:%M:%S")
handler.setFormatter(formatter)
logger.addHandler(handler)