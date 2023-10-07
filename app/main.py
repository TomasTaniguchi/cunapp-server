from fastapi import FastAPI
from models.script import Script
from controllers import *


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Cuña-desu"}


@app.get("/scripts/")
async def get_scripts():
    return await get_all_scripts()


@app.put("/run/{script_id}")
async def create_item(script_id: int) -> Script:
    return await script_runner(await get_script(script_id))
