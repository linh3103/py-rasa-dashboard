from sqlalchemy.orm import Session
from app.schemas import ExportInvoiceCreate
from app.services import ExportInvoice as service

def create_export_invoice(invoice: ExportInvoiceCreate, db: Session):
    return service.CREATE(invoice, db)

def read_all_export_invoices(db: Session):
    return service.READ_ALL(db)

def read_export_invoice_by_id(invoice_id: int, db: Session):
    return service.READ_ONE(invoice_id, db)
