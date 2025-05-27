from pydantic import BaseModel

class IntentBase(BaseModel):
    name: str
    description: str


# Tạo các class IntentCreate và IntentOut để sử dụng trong các route tương ứng
# Giúp phần biệt giữa việc tạo mới và lấy dữ liệu của Intent
class IntentCreate(IntentBase):
    pass

class IntentOut(IntentBase):
    id: int

    # This is used to convert SQLAlchemy models to Pydantic models
    # Tự động chuyển đổi dữ liệu từ ORM sang JSON
    class Config:
        from_attributes = True

