from pydantic import BaseModel

class IntentBase(BaseModel):
    name: str
    examples: str

class IntentCreate(IntentBase):
    pass

class IntentOut(IntentBase):
    id: int

    class Config:
        orm_mode = True
