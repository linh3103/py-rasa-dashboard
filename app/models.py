from sqlalchemy import Column, Integer, String, Text
from app.helpers import Base

class Intent(Base):
    __tablename__ = "intents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, default="", nullable=False)

class IntentExample(Base):
    __tablename__ = "intent_example"

    id = Column(Integer, primary_key=True, index=True)
    intent_id = Column(Integer)
    example = Column(Text, unique=True, nullable=False)
    description = Column(Text, default="", nullable=False)