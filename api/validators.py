from pydantic import BaseModel


class UrlsBase(BaseModel):
    origin_url: str

    class Config:
        orm_mode = True


class KeyUrlBase(BaseModel):
    key_url: str


class GenUrlBase(BaseModel):
    gen_url: str
