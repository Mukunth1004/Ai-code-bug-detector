# AI Code Smell Detector

This project is an AI-powered web application designed to detect code smells in programming code. It leverages a pre-trained model (`microsoft/codebert-base`) for code smell detection through a FastAPI web server. The application allows users to submit their code snippets and receive a prediction of whether the code contains smells, providing insights into possible areas for improvement.

## Features
- **Code Smell Detection**: Detects potential issues or smells in the submitted code using the `microsoft/codebert-base` model.
- **Web Interface**: User-friendly interface built with FastAPI and Jinja2 templates.
- **Authentication**: Secure routes with authentication using FastAPI dependencies.
- **API Integration**: Includes API routes to interact with the backend programmatically.

## Installation

To run the project locally, follow these steps:

### Prerequisites
- Python 3.7 or later
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ai-code-smell-detector.git
    cd ai-code-smell-detector
    ```

2. Create and activate a virtual environment (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

5. Visit the application in your browser at [http://localhost:8000](http://localhost:8000).

## Usage

- **Homepage**: Upon visiting the homepage, you will see a form where you can paste a code snippet.
- **Submit Code**: Paste your code in the text area and click "Detect". The application will display a prediction of whether the code contains any smells, along with possible insights for improvements.

## Endpoints

- **GET /**: Serves the homepage where users can input code for detection.
- **POST /detect**: Accepts a code snippet and returns a prediction based on the AI model.

### Example:

To detect code smells in a Python code snippet, you can submit the code through the web interface, or call the API endpoint directly.

```bash
POST /detect

