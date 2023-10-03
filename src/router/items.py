from typing import Union

from fastapi import APIRouter, Depends, HTTPException

from src.dependencies import get_token_header
from src.models.item import Item

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not Found..!"}}
)


@router.post("/")
async def create_item(item: Item):
    return item


@router.get("/")
async def read_item(search_keyword: str, page: int = 1, q: Union[str, None] = None, is_crush: bool = False):
    return {
        "search_keyword_result": [{"name": "Some result 1.."}, {"name": "Some result 2.."}],
        "page": page,
        "search_keyword": search_keyword,
        "q": q,
        "is_crush": is_crush
    }


@router.put("{item_id}", tags=["custome_tag"], responses={403: {"description": "잘못된 요청"}})
async def update_item(item_id: int):
    if item_id != "1":
        raise HTTPException(status_code=403, detail="지금은 아이디가 1번인 아이템만 업데이트 할 수 있습니다")
    return {"item_id": item_id, "name": "업데이트된 이름이라고 가정합니다."}
