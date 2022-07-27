import datetime

from sqlalchemy import Column, DateTime, Integer, String

from api.settings import DataBase


class UrlsModel(DataBase):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    origin_url = Column(String)
    key_url = Column(String, unique=True, index=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
