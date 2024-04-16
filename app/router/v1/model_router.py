from fastapi import APIRouter, Body, Depends
from app.Model.model import UserSchema, UserLoginSchema
from app.controllers.index import user_controller
from app.infrastructure.auth_bearer import JWTBearer
from app.infrastructure.auth_handler import signJWT
router = APIRouter()

@router.post("/model", tags=["flan"], dependencies=[Depends(JWTBearer())])
def run_model(text: str):
    return user_controller.model_result(text)
