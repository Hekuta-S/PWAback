from sqlalchemy.orm import Session
from app.db.models.item import Item
from app.schemas.item import ItemCreate

def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 100):
    # Para MSSQL, se requiere un order_by cuando se usa offset/limit
    return db.query(Item).order_by(Item.id).offset(skip).limit(limit).all()

def import_items(db: Session, items: list[ItemCreate]):
    db_items = [Item(**item.dict()) for item in items]
    db.add_all(db_items)
    db.commit()
    return db_items

def delete_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    return False

def delete_all_items(db: Session):
    num_deleted = db.query(Item).delete()
    db.commit()
    return num_deleted