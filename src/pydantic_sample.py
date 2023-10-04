import datetime
from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str


class Item(BaseModel):
    name: str
    description: str
    category: Category  # 다른 Pydantic 모델을 필드로 사용하여 중첩


app = FastAPI()


@app.post("/items")
async def post_item(item: Item):
    if item.name is None:
        raise HTTPException(status_code=400, detail="이름이 없어요")
    # elif item.description is None:
    #     raise HTTPException(status_code=400, detail="설명이 없어요")

    return {"name": item.name, "description": item.description,
            "created_at": datetime.datetime.now()}
