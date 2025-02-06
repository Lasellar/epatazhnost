from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
MAKS_ID = os.getenv('MAKS_ID')

TELEGRAM_API = f'https://api.telegram.org/bot{TOKEN}/'
