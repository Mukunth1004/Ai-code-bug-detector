from fastapi import FastAPI, Body
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

app = FastAPI(title="AI Code Smell Detector & Refactor API")

# Load Hugging Face Code Smell Model (you can fine-tune later)
# For demo, we use sentiment-analysis as placeholder
classifier = pipeline("text-classification", model="microsoft/codebert-base")  # Replace with your fine-tuned model

class CodeInput(BaseModel):
    code: str

@app.post("/detect")
async def detect_smell(data: CodeInput):
    prediction = classifier(data.code)
    return {
        "original_code": data.code,
        "prediction": prediction
    }

@app.get("/")
def root():
    return {"message": "Welcome to the AI Code Smell Detector"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
