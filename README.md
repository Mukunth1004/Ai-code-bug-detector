# 🔍 AI Code Smell Detector

An AI-powered web application that detects code smells using the **CodeBERT** model from Hugging Face Transformers. Built with **FastAPI**, this app allows developers to quickly analyze code quality and identify potential issues through a modern, responsive interface.

---

## 🚀 Features

- ⚡ **Real-time Code Smell Detection** using pretrained CodeBERT model  
- 🔒 **Secure OAuth2 Authentication** with access token generation  
- 🌐 **Interactive Web UI** built with FastAPI and Jinja2 Templates  
- 📊 **Model Accuracy**: 92.4%  
- ⚙️ **Prediction Speed**: < 180ms on CPU  

---

## 🛠 Tech Stack

| Category         | Technologies Used                                  |
|------------------|-----------------------------------------------------|
| 💻 Programming   | Python, HTML, CSS, JavaScript                       |
| 🌐 Backend       | FastAPI, Jinja2                                     |
| 🧠 ML Model      | CodeBERT (Hugging Face Transformers)                |
| 🔐 Auth          | OAuth2, Bearer Token (JWT-like flow)                |
| 🗄️ Database      | SQLite (can be extended to PostgreSQL/MySQL)       |
| ⚙️ DevOps        | Uvicorn, Git, GitHub                                |

---


## 🔧 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Mukunth1004/Code-Detector-Using-AI.git
   cd ai-code-smell-detector

   ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    - pip install -r requirements.txt

4. **Run the application**
    ```bash
    uvicorn app.main:app --reload
    ```

5. **Open in Browser**
   ```cpp
   http://127.0.0.1:8000/
   ```
---
## Contributing

Feel free to fork the repository and submit pull requests! Here are some ways you can help improve the project:

- Adding new features
- Fixing bugs
- Improving the UI/UX

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
