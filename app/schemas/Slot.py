from pydantic import BaseModel, ConfigDict

class SlotBase(BaseModel):
    name: str
    type: str
    auto_fill: bool
    entity_name: str
    initial_value: str
    influence_conversation: bool
    description: str

class SlotResponse(SlotBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class SlotWrite(SlotBase):
    pass