from sqlalchemy.orm import declared_attr, declarative_base
from sqlalchemy import Column, Integer, String, Float

from db_config import engine
from constants import BACKEND_PREFIX


class Base:
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return f'{BACKEND_PREFIX}{cls.__name__.lower()}'


Base = declarative_base(cls=Base)


class PromoCode(Base):
    name = Column(String(100))
    code = Column(String(16), unique=True)
    discount = Column(Float)
    amount = Column(Integer)

    def __repr__(self):
        return (
            f'Промокод: {self.code} Название: {self.name}, Скидка: '
            f'{self.discount}%, Остаток использований: {self.amount}'
        )


class UserInfo(Base):
    cookie = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    third_name = Column(String)
    telegram = Column(String, unique=True)
    sdek = Column(String)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.cookie}'


Base.metadata.create_all(engine)
