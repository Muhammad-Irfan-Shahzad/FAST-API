from fastapi import APIRouter, Body, Depends
from app.Model.model import UserSchema, UserLoginSchema
from app.infrastructure.auth_bearer import JWTBearer
from app.infrastructure.auth_handler import signJWT
from app.controllers.index import user_controller

router = APIRouter()

@router.post("/signup", tags=["user"])
def signup(user: UserSchema = Body(...)):
    return user_controller.create_user(user)

@router.post("/login", tags=["user"])
def login(user: UserLoginSchema = Body(...)):
    return user_controller.user_login(user)

@router.get("/current", tags=["user"], dependencies=[Depends(JWTBearer())])
def get_current_user(email: str = Depends(JWTBearer())):
    return user_controller.current_user(email)

