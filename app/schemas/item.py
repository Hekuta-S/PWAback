from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    synced: bool = False

class Item(ItemCreate):
    id: int

    class Config:
        orm_mode = True