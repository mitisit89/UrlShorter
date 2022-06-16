from fastapi import FastAPI

api = FastAPI()



@api.get('/{url_hash}')
async def parsce_url_hash(url_hash:str):
    return {"msg": url_hash}

@api.post('/create-url-hash')
async def create_url_hash():
    pass
