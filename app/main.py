from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from transformers import pipeline

from app.api.endpoints import router as api_router
from app.auth.auth import check_auth
from app.db.database import init_db

app = FastAPI(title="AI Code Smell Detector")

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Load Code Smell detection model
classifier = pipeline("text-classification", model="microsoft/codebert-base")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "code": None, "prediction": None})

@app.post("/detect", response_class=HTMLResponse)
async def detect_smell(request: Request, code: str = Form(...)):
    prediction = classifier(code)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "code": code,
        "prediction": prediction
    })

# Include the API routes with auth
app.include_router(api_router, dependencies=[Depends(check_auth)])
