from fastapi import Header, HTTPException


# 요청 헤더에 "x-token:fake-super-secret-token"가 포함되어야 한다.
# 이 요청은 포스트맨으로 실습 가능하다.
async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


# URL Query Parameter에 "?token=super-hidden-token-key" 값이 있어야만 한다.
async def get_query_token(token: str):
    if token != "super-hidden-token-key":
        raise HTTPException(status_code=400, detail="No provided super hidden token")
