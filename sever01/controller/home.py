from fastapi import APIRouter, Form
from model import users
from typing import Annotated
from pydantic import BaseModel

controller = APIRouter(
    prefix="",
    tags=[],
    responses={404:{"description":"not found"}}
)

class User(BaseModel):
    id : str
    pwd : str

@controller.get("/")
def root():
    print("sever01 start!!")
    return {"name": "AI"}

@controller.get("/data")
def data(d1, d2):
    return {"d1": d1, "d2": d2}

@controller.get("/db")
def db():
    return {"users" : users.findALL()}

@controller.get("/id")
def userId(id):
    return {"users" : users.findone(id)}

@controller.get("/login")
def login(id, pwd):
    return {"user" : users.login(id, pwd)}

@controller.post("/login")
def login(id: Annotated[str, Form(...)], pwd: Annotated[str, Form(...)]):
    return {"user" : users.login(id, pwd)}

@controller.post("/login2")
def login(user : User):
    return {"user" : users.login(user.id, user.pwd)}
