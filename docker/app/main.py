from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from user import *
from ganglia import *
from ipmi import *
from slurm import *
from out import *

app = FastAPI()

origins = [
    "http://localhost:8080",
    "https://www.supreme-k.org/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str
    password: str

@app.get("/")
def read_root():
    return {"SC22": "backend test"}


@app.get("/backend/api")
def read_root():
    return {"SC22": "backend"}

# 로그인 엔드포인트
@app.post("/backend/api/login")
async def create_item(user: User):
    result = login(user)
    return result

# @app.get("/backend/api/ganglia/{item_id}")
# def read_item(item_id: str):
#     if item_id == "line":
#         line = get_line()
#         return line
#     if item_id == "bar":
#         bar = get_bar()
#         return bar
#     return {}


# @app.get("/backend/api/ipmi/{item_id}")
# def read_item(item_id: str, type: Union[str, None] = None, host: Union[str, None] = None, state: Union[str, None] = None):
#     if item_id == "power":
#         power = get_power(type)
#         return power
#     if item_id == "power-update":
#         data = set_power(host, state)
#         return data
#     return {"power": "error"}


@app.get("/backend/api/slurm/{item_id}")
def read_item(item_id: str, type: Union[str, None] = None):
    if item_id == "nodes":
        slurm_json = get_nodes(type)
        return slurm_json

    # if item_id == "squeue":
    #     slurm_json = get_squeue()
    #     return slurm_json

    if item_id == "runtime":
        slurm_json = get_runtime()
        return slurm_json

    # if item_id == "job-history":
    #     slurm_json = get_job_history(type)
    #     return slurm_json


# @app.get("/backend/api/out/{item_id}")
# def read_item(item_id: str, dir: str, file: str):

#     if item_id == "read":
#         out_json = read_file(dir, file)
#         return out_json


# @app.get("/backend/api/out")
# def read_root():
#     out_json = get_file()
#     return out_json
