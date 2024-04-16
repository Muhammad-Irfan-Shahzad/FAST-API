from fastapi import FastAPI, Body
from app.Model.model import UserSchema, UserLoginSchema
from app.controllers.v2.user_controller import UserController

app = FastAPI()
user_controller = UserController()

@app.post("/signup", tags=["user"])
def signup(user: UserSchema = Body(...)):
    return user_controller.create_user(user)

@app.post("/login", tags=["user"])
def login(user: UserLoginSchema = Body(...)):
    return user_controller.user_login(user)

@app.get("/current", tags=["user"])
def current_user(email: str):
    return user_controller.current_user(email)

@app.post("/model", tags=["user"])
def run_model(text: str):
    return user_controller.model_result(text)
