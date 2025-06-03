from sqlalchemy.orm import Session
from app.schemas import SlotWrite
from app.models import Slot

def CREATE(slot: SlotWrite, db: Session):
    db_slot = Slot(
        name=slot.name,
        type=slot.type,
        auto_fill=slot.auto_fill,
        entity_name=slot.entity_name,
        initial_value=slot.initial_value,
        influence_conversation=slot.influence_conversation,
        description=slot.description
    )
    db.add(db_slot)
    db.commit()
    db.refresh(db_slot)
    return db_slot

def READ_ALL_SLOT(db: Session):
    return db.query(Slot).all()

def UPDATE(id: int, slot: SlotWrite, db: Session):
    db_slot = db.query(Slot).filter(Slot.id == id).first()
    if db_slot:

        db_slot.name=slot.name,
        db_slot.type=slot.type,
        db_slot.auto_fill=slot.auto_fill,
        db_slot.entity_name=slot.entity_name,
        db_slot.initial_value=slot.initial_value,
        db_slot.influence_conversation=slot.influence_conversation,
        db_slot.description=slot.description

        db.commit()
        db.refresh(db_slot)
        return db_slot
    return None

def DELETE(id: int, db: Session):
    db_slot = db.query(Slot).filter(Slot.id == id).first()
    if db_slot:
        db.delete(db_slot)
        db.commit()
        return True
    return False