from sqlalchemy import Column, Integer, String, Text, DateTime, CHAR
from sqlalchemy.sql import func
from helpers.database import Base

class Intent(Base):
    __tablename__ = "intents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    used = Column(CHAR(1), nullable=False, default="Y", comment="Y: Yes, N: No")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Example(Base):
    __tablename__ = "examples"

    id = Column(Integer, primary_key=True, index=True)
    intent_id = Column(Integer, nullable=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class IntentExample(Base):
    __tablename__ = "intent_examples"

    id = Column(Integer, primary_key=True, index=True)
    intent_id = Column(Integer, nullable=False)
    example_id = Column(Integer, nullable=False)

# class Synonym(Base):
#     __tablename__ = "synonyms"

#     id = Column(Integer, primary_key=True, index=True)
#     role = Column(String(50), nullable=True, comment="Vai trò của từ: động từ, danh từ, tính từ")
#     name = Column(String(100), nullable=False)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

# class SynonymExample(Base):
#     __tablename__ = "synonym_examples"

#     id = Column(Integer, primary_key=True, index=True)
#     synonym_id = Column(Integer, nullable=False)
#     example_name_vi = Column(String(100), nullable=False)
#     example_name_en = Column(String(100), nullable=True)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())