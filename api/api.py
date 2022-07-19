from typing import Iterator

from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

import api.database as database
from api.handlers import get_origin_url, save_urls

database.Base.metadata.create_all(bind=database.engine)
api = FastAPI()


def get_db() -> Iterator:
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api.get("/{key_url}")
async def parsce_key_url(
    key_url: str, db: Session = Depends(get_db)
) -> RedirectResponse:
    return RedirectResponse(get_origin_url(db=db, key_url=key_url))


@api.post("/save_url", response_model=database.KeyUrlBase)
async def save_url(
    url: database.UrlsBase, db: Session = Depends(get_db)) -> dict[str, str]:
    return save_urls(db=db, url=url)
