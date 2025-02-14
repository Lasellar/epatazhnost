from pyrogram import Client, filters
from pyrogram.types import Message

from utils import check_user
from texts import hi
from constants import TOKEN, API_ID, API_HASH


bot = Client('bot', bot_token=TOKEN, api_hash=API_HASH, api_id=API_ID)
with bot:
    BOT_ID = bot.get_me().id


@bot.on_message(filters.command('start') & ~filters.group & ~filters.service)
async def start_command(_, message: Message):
    await check_user(message)
    await bot.send_message(
        chat_id=message.chat.id,
        text=hi
    )


@bot.on_message(filters.command('my_id') & ~filters.group & ~filters.service)
async def get_id(_, message: Message):
    await check_user(message)
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'{message.from_user.first_name}, твой id: '
             f'<code>{message.from_user.id}</code>\n'
             f'Можешь просто нажать на него, и он скопируется'
    )


@bot.on_message(~filters.group & ~filters.service)
async def echo(_, message: Message):
    if not message.from_user.is_bot:
        await check_user(message)
        await message.reply(f'BOT_ID: {BOT_ID}, echo')


while True:
    print('Бот запущен')
    bot.run()
