from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


class Category(BaseModel):
    id: int
    name: str


class Item(BaseModel):
    name: str
    description: str
    category: Category  # 다른 Pydantic 모델을 필드로 사용하여 중첩


@app.post("/items/")
def create_item(item: Item):
    return item
