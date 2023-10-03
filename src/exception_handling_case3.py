# src/exception_handling_case3.py
from fastapi import FastAPI

from src.exceptions.exception_classes import MyHttpException
from src.exceptions.custom_exception import my_exception_handler

app = FastAPI()
app.add_exception_handler(MyHttpException, my_exception_handler)


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0:
        raise MyHttpException(message="아이템 아이디는 양수이어야 함")
    # 아이템 조회 및 반환 코드
    return {"item_name": f"item : {item_id}"}
