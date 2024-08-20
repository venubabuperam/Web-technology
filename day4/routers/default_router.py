from fastapi import APIRouter

from day4.routers import users_router, clients_router, classification_router

api_router = APIRouter()

api_router.include_router(users_router.api_router, tags=["User Management"])
api_router.include_router(clients_router.api_router,  tags=["Client Management"])
api_router.include_router(classification_router.api_router,  tags=["Text Classification"])