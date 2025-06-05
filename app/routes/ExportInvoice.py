from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.helpers import get_db
from app.schemas import ExportInvoiceCreate, ExportInvoiceResponse
from app.controllers import ExportInvoice as controller

router = APIRouter(prefix="/export_invoice", tags=["ExportInvoice"])

@router.post("/", response_model=ExportInvoiceResponse)
def createExportInvoice(invoice: ExportInvoiceCreate, db: Session = Depends(get_db)):
    return controller.create_export_invoice(invoice, db)

@router.get("/", response_model=list[ExportInvoiceResponse])
def readAllExportInvoices(db: Session = Depends(get_db)):
    return controller.read_all_export_invoices(db)

@router.get("/{invoice_id}", response_model=ExportInvoiceResponse)
def readExportInvoice(invoice_id: int, db: Session = Depends(get_db)):
    return controller.read_export_invoice_by_id(invoice_id, db)
