from fastapi import FastAPI, Depends

from src.dependencies import get_token_header
from src.internal import admin
from src.router import company, users, items, greet, root

app = FastAPI()

# 라우터 등록
app.include_router(root.router)
app.include_router(company.router)
app.include_router(users.router)
app.include_router(items.router)
app.include_router(greet.router)
app.include_router(admin.router,
                   prefix="/admin", dependencies=[Depends(get_token_header)],
                   responses={
                       422: {"description": "ㅈㅓ리가!"},
                       418: {"description": "Teapot!"}}
                   )
