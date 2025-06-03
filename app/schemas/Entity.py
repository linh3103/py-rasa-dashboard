from pydantic import BaseModel, ConfigDict

class EntityBase(BaseModel):
    entity_name: str
    description: str

class EntityCreate(EntityBase):
    pass

class EntityResponse(EntityBase):
    id: int
    model_config = ConfigDict(from_attributes=True)