from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint, DateTime, func
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

    # Không được nhập trùng
    __table_args__ = (
        UniqueConstraint('entity_id', 'example_id', 'char_start', 'char_end'),
    )

class Form(Base):
    __tablename__ = "forms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    form_name = Column(String(100), unique=True, nullable=False)
    fields = Column(Text, nullable=False)
    description = Column(Text, nullable=False, default="")


class Warehouse(Base):
    __tablename__ = "warehouse"

    product_code = Column(String(50), primary_key=True)
    product_name = Column(String(100), unique=True, nullable=False)
    quantity = Column(Integer, default=0, nullable=False)
    unit = Column(String(50), default="Cái", nullable=False)

class WarehouseEntry(Base):
    __tablename__ = "warehouse_entry"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_code = Column(String(50), ForeignKey(Warehouse.product_code), nullable=False)
    quantity_entry = Column(Integer, default=0, nullable=False)
    quantity_remaining = Column(Integer, default=0, nullable=False)
    entry_date = Column(DateTime, server_default=func.now(), nullable=False)

class ExportInvoice(Base):
    __tablename__ = "export_invoice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_code = Column(String(50), ForeignKey("warehouse.product_code"), nullable=False)
    quantity = Column(Integer, nullable=False)
    export_date = Column(DateTime, server_default=func.now(), nullable=False)
    note = Column(Text, default="", nullable=True)
