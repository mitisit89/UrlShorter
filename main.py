from api import api
import uvicorn


def main():
    return api


if __name__ == "__main__":
    uvicorn.run("main:api")
