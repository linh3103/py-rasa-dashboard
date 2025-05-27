from sqlalchemy.orm import Session
from schemas.ExampleSchema import ExampleCreate
from sqlModels import Example, Intent


def CREATE(example: ExampleCreate, db: Session):
    db_example = Example(intent_id=example.intent_id, text=example.text)
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example


def ALL(db: Session):
    result = db.query(Example).all()
    return result

def READ_TO_CREATE_EXAMPLE(db: Session):
    result = (
        db.query(
            Intent.id.label("intent_id"),
            Intent.name.label("intent_name"),
            Example.text.label("example_name")
        )
        .join(Example, Example.intent_id == Intent.id)
        .all()
    )
    return result