# src/exceptions/custom_exception.py
from fastapi import Request
from fastapi.responses import JSONResponse

from src.exceptions.exception_classes import MyHttpException


async def my_exception_handler(request: Request, exc: MyHttpException):
    return JSONResponse(
        status_code=418,
        content={"message": f"[오류] {exc.message}"},
    )
