import base64
import json
import os

import requests
from fastapi import APIRouter
from pydantic import BaseModel

api_router = APIRouter()

class TextClassificationRequest(BaseModel):
    statement: str


@api_router.post("/text/predict")
async def analyzeText(textInput: TextClassificationRequest):
    url = os.getenv("GOOGLE_VERTEX_ENDPOINT")
    statement = base64.b64decode(textInput.statement).decode("utf-8")

    payload = {
            "instances": {
                "mimeType": "text/plain",
                "content": statement
            }
    }

    token= os.getenv("TOKEN")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    return response.json()








