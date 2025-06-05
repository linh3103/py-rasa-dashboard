# Schema for Warehouse, matching the model definition
from pydantic import BaseModel, ConfigDict

class WarehouseBase(BaseModel):
    product_code: str
    product_name: str
    quantity: int
    unit: str

class WarehouseResponse(WarehouseBase):
    model_config = ConfigDict(from_attributes=True)

class WarehouseUpdate(BaseModel):
    product_name: str
    quantity: int
    unit: str

class WarehouseWrite(WarehouseBase):
    pass
