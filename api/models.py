import datetime

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from api.settings import DataBase


class UrlsModel(DataBase):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    origin_url = Column(String(length=200))
    key_url = Column(String, unique=True, index=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)


class UserModel(DataBase):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(length=100), unique=True, nullable=False)
    password = Column(String(length=225), unique=True, nullable=False)



