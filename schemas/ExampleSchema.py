from pydantic import BaseModel

class ExampleBase(BaseModel):
    intent_id: int
    text: str

class ExampleCreate(ExampleBase):
    pass

class ExampleOut(ExampleBase):
    id: int

    # This is used to convert SQLAlchemy models to Pydantic models
    # Tự động chuyển đổi dữ liệu từ ORM sang JSON
    class Config:
        from_attributes = True

class ExampleJoin(BaseModel):
    intent_id: int
    intent_name: str
    example_name: str
    
    class Config:
        from_attributes = True


