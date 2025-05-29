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

def DELETE(eeID: int, db: Session):
    db_example = db.query(EntityExample).filter(eeID == EntityExample.id).first()
    if db_example:
        db.delete(db_example)
        db.commit()
        return True
    return False