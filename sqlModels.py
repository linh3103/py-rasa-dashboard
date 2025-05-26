from sqlalchemy import Column, Integer, String, Text
from helpers.database import Base

class Intent(Base):
    __tablename__ = "intents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    examples = Column(Text)