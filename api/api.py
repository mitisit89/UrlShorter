
from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from api.handlers import get_origin_url, save_urls
from api.validators import KeyUrlBase, UrlsBase
from api.settings import get_db

api = FastAPI()


@api.get("/{key_url}")
async def parsce_key_url(
    key_url: str, db: Session = Depends(get_db)
) -> RedirectResponse:
    return RedirectResponse(get_origin_url(db=db, key_url=key_url))


@api.post("/save_url", response_model=KeyUrlBase)
async def save_url(url: UrlsBase, db: Session = Depends(get_db)) -> dict[str, str]:
    return save_urls(db=db, url=url)
