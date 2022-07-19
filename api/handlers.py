from functools import lru_cache
from secrets import choice
from string import ascii_letters, digits
from pydantic import HttpUrl

from sqlalchemy.orm import Session

from api.database import UrlsBase, UrlsModel


@lru_cache
def generate_key_url() -> str:
    return "".join(choice(ascii_letters + digits) for _ in range(8))


def get_origin_url(db: Session, key_url: str) -> HttpUrl:

    return db.query(UrlsModel).filter(UrlsModel.key_url == key_url).first().origin_url


def save_urls(db: Session, url: UrlsBase) -> dict[str, str]:
    key_url: str = generate_key_url()
    db_urls = UrlsModel(origin_url=url.origin_url, key_url=key_url)
    db.add(db_urls)
    db.commit()
    db.refresh(db_urls)
    return dict(key_url=key_url)
