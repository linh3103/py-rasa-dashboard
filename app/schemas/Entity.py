from pydantic import BaseModel

class EntityBase(BaseModel):
    entity_name: str
    description: str

class EntityCreate(EntityBase):
    pass

class EntityResponse(EntityBase):
    id: int
    class Config:
        from_attributes: True