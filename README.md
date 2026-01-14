# Chat App

## Prerequisites

- Git
- Python 3.x
- Optional: VS Code (mit Live Server Extension)

## Clone the repository

```bash
git clone https://github.com/ManuelGiehl/chat_app_frontend_backend.git
cd chat_app_frontend_backend
```

## Backend Setup (Windows)

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Test backend in browser: http://127.0.0.1:8000/api/chat/

## Backend Setup (macOS / Linux)

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Test backend in browser: http://127.0.0.1:8000/api/chat/

## Frontend Setup

1. Öffne ein zweites Terminal
2. Öffne `frontend/index.html` mit einem Live Server (z.B. VS Code Live Server Extension)
3. Frontend öffnet sich im Browser: http://localhost:5500
4. Optional (Empfohlen) Rechtsklick im VS Code auf die index.html und "Open with Live-Server"