from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

from os import getenv
from datetime import datetime


load_dotenv()
TOKEN = getenv('TOKEN')
API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')
ME = getenv('ME')
bot = Client('bot', bot_token=TOKEN, api_hash=API_HASH, api_id=API_ID)


print(datetime.now())
while True:
    try:
        bot.run()
    except Exception as ex:
        print(ex)

