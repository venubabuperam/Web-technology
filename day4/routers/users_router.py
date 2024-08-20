from fastapi import APIRouter


api_router = APIRouter()

@api_router.get("/")
async def routerRoot():
    return {"message": "Welcome To FastAPI"}


@api_router.get("/users")
async def getUsers():
    return users


@api_router.get("/users/{userId}")
async def getUserById(userId: int):
    return users["users"][userId]


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