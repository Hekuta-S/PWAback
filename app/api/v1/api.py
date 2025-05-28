from fastapi import APIRouter
from app.api.v1.endpoints import items
from app.api.v1.endpoints import test_db  # Importa el endpoint de prueba de DB

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(test_db.router, prefix="/utils", tags=["utils"])  # Incluye el router de prueba de DB