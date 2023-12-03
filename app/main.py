from fastapi import FastAPI
from models.script import Script
from fastapi.middleware.cors import CORSMiddleware
from controllers import *
from typing import Tuple
from directory_first_time_scanner import *
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello there Cuña-desu"}


@app.get("/scripts/")
async def get_scripts():
    return await get_all_scripts()


@app.put("/run/{script_id}")
async def run_script(script_id: str):
    print(script_id)
    return await script_runner(await get_script(script_id))

#MOCK_DATA = script_loader(script_generator, ls('../scripts'))