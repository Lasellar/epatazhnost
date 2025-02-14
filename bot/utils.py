from pyrogram.types import Message

from models import UserInfo
from db_config import session


async def is_user_in_db(message: Message) -> bool:
    return True if session.query(UserInfo).filter_by(
        telegram=message.from_user.id).first() else False


async def create_user_object(message: Message) -> UserInfo:
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    telegram = message.from_user.id
    user = UserInfo(
        first_name=first_name, last_name=last_name,
        telegram=telegram,
    )
    return user


async def check_user(message: Message) -> None:
    if not await is_user_in_db(message):
        user = await create_user_object(message)
        session.add(user)
        session.commit()
