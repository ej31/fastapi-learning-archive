import datetime

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Item ID must be positive")
    # 아이템 조회 및 반환 코드
    return {"item_id": item_id, "created_at": datetime.datetime.now()}