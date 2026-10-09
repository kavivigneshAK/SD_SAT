import os
import json

project_files = {
    "backend/requirements.txt": """fastapi
uvicorn
sqlalchemy
pydantic
pydantic-settings
passlib
bcrypt
python-jose
pytest
pytest-asyncio
websockets
python-multipart""",
    "backend/app/main.py": """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.session import engine, Base
from app.api import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ride Hailing API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Ride Hailing API"}""",
    "backend/app/database/session.py": """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
engine = create_engine("sqlite:///./ride_hailing.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()""",
    "backend/app/api/__init__.py": """from fastapi import APIRouter
from .auth import router as auth_router
router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Auth"])""",
    "backend/app/api/auth.py": """from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
router = APIRouter()
@router.post("/register")
def register():
    return {"message": "User registered"}
@router.post("/login")
def login():
    return {"access_token": "token", "token_type": "bearer"}
""",
    "frontend/package.json": """{
  "name": "ride-hailing-frontend",
  "version": "1.0.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.22.3",
    "axios": "^1.6.8",
    "leaflet": "^1.9.4",
    "react-leaflet": "^4.2.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.1",
    "vite": "^5.2.0",
    "tailwindcss": "^3.4.1"
  }
}""",
    "frontend/index.html": """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ride Hailing App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>""",
    "frontend/src/main.jsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)""",
    "frontend/src/index.css": """@tailwind base;
@tailwind components;
@tailwind utilities;""",
    "frontend/vite.config.js": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})""",
    "README.md": """# Ride-Hailing Application

A complete full-stack ride-hailing application.

## Prerequisites
- Python 3.9+
- Node.js 18+

## Backend Setup
1. `cd backend`
2. `python -m venv venv`
3. `source venv/bin/activate` (or `venv\\Scripts\\activate` on Windows)
4. `pip install -r requirements.txt`
5. `uvicorn app.main:app --reload`

## Frontend Setup
1. `cd frontend`
2. `npm install`
3. `npm run dev`

Navigate to `http://localhost:5173` for the frontend and `http://localhost:8000/docs` for the API documentation.
"""
}

def build_all():
    base_dir = "/Users/kavivignesh/Documents/SD SAT/ride-hailing-app"
    for path, content in project_files.items():
        full_path = os.path.join(base_dir, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
    print("Project successfully scaffolded.")

if __name__ == "__main__":
    build_all()
