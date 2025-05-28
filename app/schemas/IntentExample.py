from pydantic import BaseModel

class IntentExampleBase(BaseModel):
    intent_id:   int
    example:     str
    description: str

class IntentExampleCreate(IntentExampleBase):
    pass

class IntentExampleResponse(IntentExampleBase):
    id: int

    class Config:
        from_attributes = True

class IntentExampleRead(BaseModel):
    id:          int
    intent_id:   int
    intent_name: str
    example:     str
    description: str

    class Config:
        from_attributes = True


class IntentExampleUpdate(IntentExampleBase):
    pass
