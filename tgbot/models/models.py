from gino import Gino
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON, DATETIME)
from sqlalchemy import sql, and_, ForeignKey

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    full_name = Column(String(100))
    username = Column(String(50))
    reg_date = Column(TIMESTAMP)
    email = Column(String(50), default=None)
    phone = Column(String(50), default=None)
    queue: sql.Select


class ShopItems(db.Model):
    __tablename__ = 'shop_items'
    query: sql.Select

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('shop_categories.id'))
    name = Column(String(1000))
    price = Column(Integer)
    size = Column(String(100))
    photo = Column(String(250))
    message_id = Column(Integer)


class ShopCategories(db.Model):
    __tablename__ = 'shop_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    query: sql.Select




