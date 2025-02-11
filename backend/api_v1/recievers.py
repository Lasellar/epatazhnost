from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Bot
from bot_webhooks.utils import BOT


@receiver(pre_save, sender=Bot)
def send_message_via_bot(sender, instance, **kwargs):
    BOT.send_text(
        chat=instance.chat_id,
        text=f'Отправлено сообщение:\n'
             f'Чат:{instance.chat_id}\n'
             f'{instance.message}'
    )
