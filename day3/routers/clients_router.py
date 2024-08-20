from typing import Annotated

from fastapi import APIRouter, Query, Path
from pydantic import BaseModel

api_router = APIRouter()


@api_router.get("/")
async def routerRoot():
    return {"message": "Welcome To FastAPI"}


@api_router.get("/clients")
async def getUsers():
    return users


@api_router.get("/clients/{userId}")
async def getUserById(userId: int):
    return users["users"][userId]


@api_router.put("/item/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
        return results


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@api_router.put("/items/{item_id}")
async def update_item(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: str | None = None,
        item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


users = {
    "users": [
        {
            "user_id": 1,
            "first_name": "Andrew",
            "last_name": "John",
            "email": "andrew.john@example.com",
            "username": "ajohn",
            "password_hash": "hashed_password",
            "created_at": "2024-08-15T10:15:00Z",
            "updated_at": "2024-08-15T10:15:00Z"
        },
        {
            "user_id": 2,
            "first_name": "Emily",
            "last_name": "Smith",
            "email": "emily.smith@example.com",
            "username": "esmith",
            "password_hash": "hashed_password",
            "created_at": "2024-08-15T10:30:00Z",
            "updated_at": "2024-08-15T10:30:00Z"
        },
        {
            "user_id": 3,
            "first_name": "Michael",
            "last_name": "Brown",
            "email": "michael.brown@example.com",
            "username": "mbrown",
            "password_hash": "hashed_password",
            "created_at": "2024-08-15T11:00:00Z",
            "updated_at": "2024-08-15T11:00:00Z"
        }
    ]
}
