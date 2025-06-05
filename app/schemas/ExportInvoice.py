from pydantic import BaseModel
from datetime import datetime

class ExportInvoiceBase(BaseModel):
    product_code: str
    quantity: int
    note: str = ""

class ExportInvoiceCreate(ExportInvoiceBase):
    pass

class ExportInvoiceResponse(ExportInvoiceBase):
    id: int
    export_date: datetime

    class Config:
        from_attributes = True
