from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

from texts import hi

from os import getenv
from datetime import datetime


load_dotenv()
TOKEN = getenv('TOKEN')
API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')
ME = getenv('ME')
bot = Client('bot', bot_token=TOKEN, api_hash=API_HASH, api_id=API_ID)


@bot.on_message(~filters.group)
async def echo(client_object, message: Message):
    await message.reply(f'[{datetime.now()}] {message.text}')


@bot.on_message(filters.command('start') & ~filters.group)
async def start_command(client_object, message: Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=hi
    )


while True:
    try:
        bot.run()
    except Exception as ex:
        print(ex)
