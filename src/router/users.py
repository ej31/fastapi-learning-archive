from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

router = APIRouter()


@router.get("/users", tags=["users"])
async def read_users():
    return [{"username": "테드창"}, {"username": "로빈"}]


@router.get("/user/{user_id}", tags=["users"])
async def read_item(user_id: int, response: Response):
    if user_id == 1:
        return {"user_name": "고재형"}
    elif user_id == 2:
        return {"user_name": "김세빈"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "없는 유저 입니다."}
