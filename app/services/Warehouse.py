from sqlalchemy.orm import Session
from app.models import Warehouse
from app.schemas import WarehouseWrite, WarehouseUpdate

def CREATE(warehouse: WarehouseWrite, db: Session):
    db_warehouse = Warehouse(
        product_code=warehouse.product_code,
        product_name=warehouse.product_name,
        quantity=warehouse.quantity,
        unit=warehouse.unit
    )
    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse

def READ_ALL(db: Session):
    return db.query(Warehouse).all()

def READ_ONE(product_code: str, db: Session):
    return db.query(Warehouse).filter(Warehouse.product_code == product_code).first()

def UPDATE(product_code: str, warehouse: WarehouseUpdate, db: Session):
    db_warehouse = db.query(Warehouse).filter(Warehouse.product_code == product_code).first()
    if db_warehouse:
        db_warehouse.product_name = warehouse.product_name
        db_warehouse.quantity = warehouse.quantity
        db_warehouse.unit = warehouse.unit
        db.commit()
        db.refresh(db_warehouse)
        return db_warehouse
    return None

def DELETE(product_code: str, db: Session):
    db_warehouse = db.query(Warehouse).filter(Warehouse.product_code == product_code).first()
    if db_warehouse:
        db.delete(db_warehouse)
        db.commit()
        return True
    return False

def FIND_BY_NAME(product_name: str, db: Session):
    if not product_name:
        return db.query(Warehouse).all()
    return db.query(Warehouse).filter(Warehouse.product_name.like(f"%{product_name}%")).all()
