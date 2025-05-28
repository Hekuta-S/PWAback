from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router
from app.core.config import settings


app = FastAPI(title=settings.PROJECT_NAME)

# Configuración de CORS para permitir peticiones desde Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=[  "http://localhost:4200",
        "http://127.0.0.1:8080",
        "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "ok"}