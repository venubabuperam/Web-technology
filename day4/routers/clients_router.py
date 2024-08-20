from typing import Annotated

from fastapi import APIRouter, Query, Path, Depends
from pydantic import BaseModel, Field

from day4.requests.Items import Item
from day4.services.items_svc import ItemsSVC

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





@api_router.put("/items/{item_id}")
async def update_item(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: str | None = None,
        item: Item | None = None,
        svc: ItemsSVC = Depends(ItemsSVC)
):
    svc.updateItem(q, item_id, item)

@api_router.delete("/items/{item_id}")
async def update_item(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: str | None = None,
        item: Item | None = None,
        svc: ItemsSVC = Depends(ItemsSVC)
):
    svc.deleteItem(q, item_id, item)


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
