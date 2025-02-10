from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

from texts import hi

from os import getenv


load_dotenv()
TOKEN = getenv('TOKEN')
API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')
ME = getenv('ME')
BOT_ID = getenv('BOT_ID')
bot = Client('bot', bot_token=TOKEN, api_hash=API_HASH, api_id=API_ID)


@bot.on_message(filters.command('start') & ~filters.group & ~filters.service)
async def start_command(_, message: Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=hi
    )


@bot.on_message(~filters.group & ~filters.service)
async def echo(_, message: Message):
    if message.from_user.id != BOT_ID:
        await message.reply('почему??')


while True:
    bot.run()
