from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
import psycopg2

from src.search_memory import SearchMemory

singletons = {}

@asynccontextmanager
async def lifespan(_):
    singletons["search_memory"] = SearchMemory()
    yield
    singletons["search_memory"] = None

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    print(singletons["search_memory"].test)



    print("qwe")
    return {"Hello": "qwe World"}
