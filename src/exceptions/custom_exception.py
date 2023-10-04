# src/exceptions/custom_exception.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

from src.exceptions.exception_classes import MyHttpException


async def my_exception_handler(request: Request, exc: MyHttpException):
    return JSONResponse(
        status_code=418,
        content={"message": f"[오류] {exc.message}"},
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=400,
        content={"message": f"잘못된요청입나다! {exc.detail}"}
    )
