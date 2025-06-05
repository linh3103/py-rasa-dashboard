# Schema for WarehouseEntry, matching the model definition
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class WarehouseEntryBase(BaseModel):
    product_code: str
    quantity_entry: int
    quantity_remaining: int
    entry_date: datetime

class WarehouseEntryResponse(WarehouseEntryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class WarehouseEntryWrite(BaseModel):
    product_code: str
    quantity_entry: int
    entry_date: datetime

class WarehouseEntryUpdate(WarehouseEntryBase):
    pass

class WarehouseEntryExport(BaseModel):
    product_code: str
    quantity: int