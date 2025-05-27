from pydantic import BaseModel

class IntentBase(BaseModel):
    name: str
    description: str

class IntentCreate(IntentBase):
    pass

class IntentOut(IntentBase):
    id: int
    class Config:
        from_attributes = True