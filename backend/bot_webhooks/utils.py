import requests
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
MAKS_ID = os.getenv('ME')

TELEGRAM_API = f'https://api.telegram.org/bot{TOKEN}/'


class BOT:
    TOKEN = TOKEN
    MAKS_ID = MAKS_ID
    TELEGRAM_API = TELEGRAM_API
    _link = f'{TELEGRAM_API}sendMessage?'
    _chat_id = '&chat_id='
    _text = '&text='

    @classmethod
    def info(cls, chat, text, *args):
        webhook = (
            f'{cls._link}{cls._chat_id}{cls.MAKS_ID}{cls._text}'
            f'отправлено сообщение:\nчат: {chat}\nтекст: {text}'
        )
        if args:
            webhook += '\nдополнительные аргументы:'
        for arg in args:
            webhook += f'\n{arg}'
        requests.get(webhook)

    @classmethod
    def send_text(cls, chat, text):
        webhook = f'{cls._link}{cls._chat_id}{chat}{cls._text}{text}'
        requests.get(webhook)
        cls.info(chat, text)
        return webhook


# BOT.send_text(MAKS_ID, 'test')
