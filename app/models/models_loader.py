from transformers import pipeline

def get_model():
    return pipeline("text-classification", model="microsoft/codebert-base")  # Replace with fine-tuned
