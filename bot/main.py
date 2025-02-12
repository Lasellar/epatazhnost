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
bot = Client('bot', bot_token=TOKEN, api_hash=API_HASH, api_id=API_ID, )
with bot:
    BOT_ID = bot.get_me().id


@bot.on_message(filters.command('start') & ~filters.group & ~filters.service)
async def start_command(_, message: Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=hi
    )


@bot.on_message(filters.command('my_id') & ~filters.group & ~filters.service)
async def get_id(_, message: Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'{message.from_user.first_name}, твой id: '
             f'<code>{message.from_user.id}</code>'
    )


@bot.on_message(~filters.group & ~filters.service)
async def echo(_, message: Message):
    if not message.from_user.is_bot:
        await message.reply(
            f'from_user.id:{message.from_user.id}, '
            f'BOT_ID: {BOT_ID}, '
            f'is_bot: {message.from_user.is_bot}'
        )


while True:
    bot.run()
