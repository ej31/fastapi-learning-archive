from fastapi import APIRouter
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def get():
    return templates.TemplateResponse("index.html", {"request": {}, "title": "FastAPI", "message": "Hello, World!"})
