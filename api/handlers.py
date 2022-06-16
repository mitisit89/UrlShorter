from functools import lru_cache
from secrets import choice
from string import ascii_letters, digits

from sqlalchemy.orm import Session

from api.database import UrlsBase, UrlsModel


@lru_cache
def key_url_gen() -> str:
    return "".join(choice(ascii_letters + digits) for _ in range(8))


def get_origin_url(db: Session, shorted_url: str):
    return db.query(UrlsModel)


def save_urls(db: Session, url: UrlsBase) -> None:
    key_url = key_url_gen()
    db_urls = UrlsModel(origin_url=url.origin_url, key_url=key_url)
    db.add(db_urls)
    db.commit
    return None
