from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import pipeline

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

classifier = pipeline("text-classification", model="microsoft/codebert-base")

@router.post("/detect", response_class=HTMLResponse)
async def detect_code_smell(request: Request, code: str = Form(...)):
    prediction = classifier(code)
    message = "No issues found!" if prediction[0]['label'] == 'LABEL_0' else "Potential code smells detected"
    return templates.TemplateResponse("index.html", {
        "request": request,
        "code": code,
        "prediction": prediction,
        "message": message
    })
