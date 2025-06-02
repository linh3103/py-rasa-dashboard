from app.schemas import EntityExampleWrite
from app.models import EntityExample
from sqlalchemy.orm import Session

def CREATE(example: EntityExampleWrite, db: Session):
    db_example = EntityExample(
        entity_id  = example.entity_id,
        example_id = example.example_id,
        role       = example.role,
        value      = example.value,
        char_start = example.char_start,
        char_end   = example.char_end
    )
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example

def READ_ALL(db: Session):
    return db.query(EntityExample).all()

def UPDATE(eeID: int, ee: EntityExampleWrite, db: Session):
    db_example = db.query(EntityExample).filter(eeID == EntityExample.id).first()
    if db_example:
        db_example.entity_id  = ee.entity_id,
        db_example.role       = ee.role,
        db_example.value      = ee.value
        db.commit()
        db.refresh(db_example)
        return db_example
    return None

def DELETE(eeID: int, db: Session):
    db_example = db.query(EntityExample).filter(eeID == EntityExample.id).first()
    if db_example:
        db.delete(db_example)
        db.commit()
        return True
    return False