import uvicorn
from api.api import api


def main():
    return api


if __name__ == "__main__":
    uvicorn.run("main:api")
