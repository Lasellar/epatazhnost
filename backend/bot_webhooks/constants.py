from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
MAKS_ID = os.getenv('ME')

TELEGRAM_API = f'https://api.telegram.org/bot{TOKEN}/'
