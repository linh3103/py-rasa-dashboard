from sqlalchemy.orm import Session
from app.schemas import WarehouseWrite, WarehouseResponse, WarehouseUpdate
from app.services import WarehouseService as service
from app.services import WarehouseEntryService as entry_service
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_warehouse(warehouse: WarehouseWrite, db: Session):
    try:
        return service.CREATE(warehouse, db)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Mã sản phẩm đã tồn tại, hãy dùng mã khác")

def read_all_warehouses(db: Session):
    return service.READ_ALL(db)

def read_warehouse_by_code(product_code: str, db: Session):
    return service.READ_ONE(product_code, db)

def update_warehouse(product_code: str, warehouse: WarehouseUpdate, db: Session):
    return service.UPDATE(product_code, warehouse, db)

def delete_warehouse(product_code: str, db: Session):
    return service.DELETE(product_code, db)


def export_products(product_code: str, db: Session):
    warehouse = service.READ_ONE(product_code, db)
    if not warehouse:
        raise HTTPException(status_code=404, detail="Sản phẩm không tồn tại trong kho")

    entries = entry_service.READ_BY_PRODUCT_CODE(product_code, db)
    if not entries:
        raise HTTPException(status_code=404, detail="Không có dữ liệu nhập kho cho sản phẩm này")
    
    return {
        "product_code": warehouse.product_code,
        "product_name": warehouse.product_name,
        "unit": warehouse.unit,
        "quantity": warehouse.quantity,
        "entries": [entry.to_dict() for entry in entries]
    }
