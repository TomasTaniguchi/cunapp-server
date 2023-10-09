from fastapi import FastAPI
from models.script import Script
from fastapi.middleware.cors import CORSMiddleware
from controllers import *


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
async def run_script(script_id: int) -> tuple:
    print(script_id)
    return await script_runner(await get_script(script_id))
