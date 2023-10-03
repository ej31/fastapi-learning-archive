from fastapi import APIRouter, Depends

from src.dependencies import get_query_token

router = APIRouter(prefix="/greet",
                   tags=["greet"],
                   dependencies=[Depends(get_query_token)],
                   responses={404: {"description": "Not Found..!"}})


@router.get("/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
