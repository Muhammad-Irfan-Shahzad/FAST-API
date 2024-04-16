from fastapi import APIRouter
from app.router.v1.user_router import router as user_router
from app.router.v1.model_router import router as model_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["user"])

router.include_router(model_router, prefix="/models", tags=["flan"])
