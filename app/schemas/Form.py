from pydantic import BaseModel, ConfigDict

class FormBase(BaseModel):
    form_name: str
    fields: str
    description: str

class FormResponse(FormBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class FormWrite(FormBase):
    pass
