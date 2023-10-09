from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": f"Oops! {exc.detail}"
        }
    )


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Item ID must be positive")
    # 아이템 조회 및 반환 코드
    return {"item_name": f"item : {item_id}"}
