from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Message
from bot_webhooks.utils import BOT


@receiver(pre_save, sender=Message)
def send_message_via_bot(sender, instance, **kwargs):
    if ',' in instance.chat_id:
        chats = instance.chat_id.split(', ')
        for chat in chats:
            BOT.send_text(
                chat=chat,
                text=instance.message
            )
    BOT.send_text(
        chat=instance.chat_id,
        text=instance.message
    )
