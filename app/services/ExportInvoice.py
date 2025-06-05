from sqlalchemy.orm import Session
from app.models import ExportInvoice
from app.schemas import ExportInvoiceCreate

def CREATE(invoice: ExportInvoiceCreate, db: Session):
    db_invoice = ExportInvoice(
        product_code=invoice.product_code,
        quantity=invoice.quantity,
        note=invoice.note
    )
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def READ_ALL(db: Session):
    return db.query(ExportInvoice).all()

def READ_ONE(invoice_id: int, db: Session):
    return db.query(ExportInvoice).filter(ExportInvoice.id == invoice_id).first()
