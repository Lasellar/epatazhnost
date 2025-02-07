import requests
from .constants import TOKEN, MAKS_ID, TELEGRAM_API


class SendMessage:
    def __init__(self):
        self.TOKEN = TOKEN
        self.MAKS_ID = MAKS_ID
        self.TELEGRAM_API = TELEGRAM_API
        self.chat_id = '&chat_id='
        self.text = '&text='

    def get_link(self):
        return f'{TELEGRAM_API}sendMessage?'

    def info(self, chat, text, *args):
        webhook = (
            f'{self.get_link()}{self.chat_id}{self.MAKS_ID}{self.text}'
            f'отправлено сообщение:\nчат: {chat}\nтекст: {text}'
        )
        if args:
            webhook += '\nдополнительные аргументы:'
        for arg in args:
            webhook += f'\n{arg}'
        requests.get(webhook)

    def send_text(self, chat, text):
        webhook = f'{self.get_link()}{self.chat_id}{chat}{self.text}{text}'
        self.info(chat, text)
        return requests.get(webhook)


# info = SendMessage().send_text(MAKS_ID, 'test')
