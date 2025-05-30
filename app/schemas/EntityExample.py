from pydantic import BaseModel
class EntityExampleBase(BaseModel):
    entity_id: int
    example_id: int
    role: str
    value: str
    char_start: int
    char_end: int

class EntityExampleWrite(EntityExampleBase):
    pass

class EntityExampleRead(EntityExampleBase):
    id: int
    entity_name: str
    class Config:
        from_attributes = True
