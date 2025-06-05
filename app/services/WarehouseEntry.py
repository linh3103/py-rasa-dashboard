from app.models import ExportInvoice
from app.schemas import ExportInvoiceCreate
from sqlalchemy.orm import Session
from app.models import WarehouseEntry, Warehouse
from app.schemas import WarehouseEntryWrite

def CREATE(entry: WarehouseEntryWrite, db: Session):
    db_entry = WarehouseEntry(
        product_code=entry.product_code,
        quantity_entry=entry.quantity_entry,
        quantity_remaining=entry.quantity_entry,
        entry_date=entry.entry_date if hasattr(entry, 'entry_date') else None
    )
    db.add(db_entry)

    # Cập nhật số lượng tổng trong Warehouse
    db_warehouse = db.query(Warehouse).filter(Warehouse.product_code == entry.product_code).first()
    if db_warehouse:
        db_warehouse.quantity += entry.quantity_entry

    db.commit()
    db.refresh(db_entry)
    return db_entry

def READ_ALL(db: Session):
    return db.query(WarehouseEntry).all()

def READ_ONE(entry_id: int, db: Session):
    return db.query(WarehouseEntry).filter(WarehouseEntry.id == entry_id).first()

def UPDATE(entry_id: int, entry: WarehouseEntryWrite, db: Session):
    db_entry = db.query(WarehouseEntry).filter(WarehouseEntry.id == entry_id).first()
    if db_entry:
        db_entry.product_code = entry.product_code
        db_entry.quantity_entry = entry.quantity_entry
        db_entry.quantity_remaining = entry.quantity_remaining
        if hasattr(entry, 'entry_date'):
            db_entry.entry_date = entry.entry_date
        db.commit()
        db.refresh(db_entry)
        return db_entry
    return None

def DELETE(entry_id: int, db: Session):
    db_entry = db.query(WarehouseEntry).filter(WarehouseEntry.id == entry_id).first()
    if db_entry:
        db.delete(db_entry)
        db.commit()
        return True
    return False

def EXPORT(product_code: str, quantity: int, db: Session):
    # Lấy các lô còn hàng theo FIFO
    entries = db.query(WarehouseEntry)\
        .filter(WarehouseEntry.product_code == product_code, WarehouseEntry.quantity_remaining > 0)\
        .order_by(WarehouseEntry.entry_date.asc()).all()
    if not entries:
        raise Exception("Không còn lô hàng nào để xuất!")

    db_warehouse = db.query(Warehouse).filter(Warehouse.product_code == product_code).first()
    if not db_warehouse or db_warehouse.quantity < quantity:
        raise Exception("Số lượng tồn kho không đủ!")

    qty_to_export = quantity
    exported_entries = []
    for entry in entries:
        if entry.quantity_remaining >= qty_to_export:
            entry.quantity_remaining -= qty_to_export
            exported_entries.append({"entry_id": entry.id, "exported": qty_to_export})
            qty_to_export = 0
            break
        else:
            exported_entries.append({"entry_id": entry.id, "exported": entry.quantity_remaining})
            qty_to_export -= entry.quantity_remaining
            entry.quantity_remaining = 0

    if qty_to_export > 0:
        raise Exception("Không đủ số lượng trong các lô để xuất!")

    db_warehouse.quantity -= quantity
    # Lưu hóa đơn xuất kho
    invoice = ExportInvoice(
        product_code=product_code,
        quantity=quantity,
        note=""
    )
    db.add(invoice)
    db.commit()
    return exported_entries