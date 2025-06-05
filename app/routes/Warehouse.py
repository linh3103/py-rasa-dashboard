from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.helpers import get_db
from app.schemas import WarehouseWrite, WarehouseResponse, WarehouseUpdate
from app.controllers import WarehouseController as controller

router = APIRouter(prefix="/warehouse", tags=["Warehouse"])

@router.post("/", response_model=WarehouseResponse)
def createWarehouse(warehouse: WarehouseWrite, db: Session = Depends(get_db)):
    return controller.create_warehouse(warehouse, db)

@router.get("/", response_model=list[WarehouseResponse])
def readAllWarehouses(db: Session = Depends(get_db)):
    return controller.read_all_warehouses(db)

@router.get("/{product_code}", response_model=WarehouseResponse)
def readWarehouse(product_code: str, db: Session = Depends(get_db)):
    return controller.read_warehouse_by_code(product_code, db)

@router.put("/{product_code}", response_model=WarehouseResponse)
def updateWarehouse(product_code: str, warehouse: WarehouseUpdate, db: Session = Depends(get_db)):
    return controller.update_warehouse(product_code, warehouse, db)

@router.delete("/{product_code}")
def deleteWarehouse(product_code: str, db: Session = Depends(get_db)):
    return controller.delete_warehouse(product_code, db)
