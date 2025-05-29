from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint
from app.helpers import Base

class Intent(Base):
    __tablename__ = "intents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, default="", nullable=False)

class IntentExample(Base):
    __tablename__ = "intent_example"

    id          = Column(Integer, primary_key=True, index=True)
    intent_id   = Column(Integer)
    example     = Column(Text, unique=True, nullable=False)
    description = Column(Text, default="", nullable=False)

class Entity(Base):
    __tablename__ = "entity"

    id          = Column(Integer, primary_key=True, index=True)
    entity_name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, default="", nullable=False)

class EntityExample(Base):
    __tablename__ = "entity_examples"

    id         = Column(Integer, primary_key=True, index=True)
    entity_id  = Column(Integer, ForeignKey(Entity.id), nullable=False)
    example_id = Column(Integer, ForeignKey(IntentExample.id), nullable=False)
    role       = Column(String(50), nullable=False, default="")
    value      = Column(String(50), nullable=False, default="")
    char_start = Column(Integer, nullable=False)
    char_end   = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('entity_id', 'example_id', 'char_start', 'char_end'),
    )