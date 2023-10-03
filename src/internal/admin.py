from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def post_admin():
    return {"message": "admin GET Done"}


@router.post("/")
async def post_admin():
    return {"message": "admin POST Done"}
