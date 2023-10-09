# src/exception_handling_case3.py
from fastapi import FastAPI, HTTPException

from src.exceptions.exception_classes import MyHttpException
from src.exceptions.custom_exception import my_exception_handler, http_exception_handler

app = FastAPI()
app.add_exception_handler(MyHttpException, my_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0:
        raise MyHttpException(message="아이템 아이디는 양수이어야 함")
    elif item_id > 999:
        raise HTTPException(status_code=400, detail="Hey!")
    # 아이템 조회 및 반환 코드
    return {"item_name": f"item : {item_id}"}
