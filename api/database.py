import datetime

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class UrlsModel(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    origin_url = Column(String)
    key_url = Column(String, unique=True, index=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)


class UrlsBase(BaseModel):
    origin_url: str

    class Config:
        orm_mode = True


class KeyUrlBase(BaseModel):
    key_url: str
