from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

router = APIRouter()


@router.get("/company", tags=["company"])
async def read_users():
    return [{"company_name": "삼성"}, {"company_name": "엘지"}]


@router.get("/company/{company_id}", tags=["company"])
async def read_item(user_id: int, response: Response):
    if user_id == 1:
        return {"company_name": "삼성"}
    elif user_id == 2:
        return {"company_name": "엘지"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "없는 회사 입니다."}
