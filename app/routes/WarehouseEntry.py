from fastapi import Query
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.helpers import get_db
from app.schemas import WarehouseEntryWrite
from app.controllers import WarehouseEntryController as controller

router = APIRouter(prefix="/warehouse_entry", tags=["WarehouseEntry"])

@router.post("/")
def createWarehouseEntry(entry: WarehouseEntryWrite, db: Session = Depends(get_db)):
    return controller.create_warehouse_entry(entry, db)

@router.get("/")
def readAllWarehouseEntries(db: Session = Depends(get_db)):
    return controller.read_all_warehouse_entries(db)

@router.get("/{entry_id}")
def readWarehouseEntry(entry_id: int, db: Session = Depends(get_db)):
    return controller.read_warehouse_entry_by_id(entry_id, db)

@router.put("/{entry_id}")
def updateWarehouseEntry(entry_id: int, entry: WarehouseEntryWrite, db: Session = Depends(get_db)):
    return controller.update_warehouse_entry(entry_id, entry, db)

@router.delete("/{entry_id}")
def deleteWarehouseEntry(entry_id: int, db: Session = Depends(get_db)):
    return controller.delete_warehouse_entry(entry_id, db)

@router.post("/export")
def exportWarehouseEntry(product_code: str, quantity: int, db: Session = Depends(get_db)):
    return controller.export_warehouse_entry(product_code, quantity, db)