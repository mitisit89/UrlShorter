import datetime
from sqlalchemy import Column, Integer, String, create_engine,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Urls(Base):
    __tablename__ = "urls"

    id = Column(Integer,primary_key=True,index=True)
    origin_url=Column(String)
    shorted_url=Column(String,index=True)
    created=Column(DateTime,datetime.datetime.utcnow())
