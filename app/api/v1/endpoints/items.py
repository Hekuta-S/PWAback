from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.item import Item, ItemCreate
from app.crud.item import create_item, get_items, import_items, delete_item, delete_all_items
from app.db.session import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=Item)
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)

@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        items = get_items(db, skip=skip, limit=limit)
        print("[DEBUG] Items fetched:", items)
        return items
    except Exception as e:
        print("[ERROR] Exception in read_items:", e)
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/import", response_model=List[Item])
def import_items_endpoint(items: List[ItemCreate], db: Session = Depends(get_db)):
    return import_items(db, items)

@router.delete("/{item_id}")
def delete_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    success = delete_item(db, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"success": True}

@router.delete("/")
def delete_all_items_endpoint(db: Session = Depends(get_db)):
    num_deleted = delete_all_items(db)
    return {"deleted": num_deleted}