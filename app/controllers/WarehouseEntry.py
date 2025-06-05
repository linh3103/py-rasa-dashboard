from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas import WarehouseEntryWrite
from app.services import WarehouseEntryService as service
from app.services import ExportInvoice as invoice_service
from app.schemas import ExportInvoiceCreate

def create_warehouse_entry(entry: WarehouseEntryWrite, db: Session):
    try:
        result = service.CREATE(entry, db)
        return result
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Đã xảy ra lỗi, vui lòng thử lại sau")

def read_all_warehouse_entries(db: Session):
    return service.READ_ALL(db)

def read_warehouse_entry_by_id(entry_id: int, db: Session):
    return service.READ_ONE(entry_id, db)

def update_warehouse_entry(entry_id: int, entry: WarehouseEntryWrite, db: Session):
    return service.UPDATE(entry_id, entry, db)

def delete_warehouse_entry(entry_id: int, db: Session):
    return service.DELETE(entry_id, db)

def export_warehouse_entry(product_code: str, quantity: int, db: Session):
    try:
        exported_entries = service.EXPORT(product_code, quantity, db)
        return {
            "success": True,
            "exported_entries": exported_entries,
            "message": f"Đã xuất thành công {quantity} sản phẩm cho mã {product_code}"
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
