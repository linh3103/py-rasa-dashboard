from sqlalchemy.orm import Session
from app.models import IntentExample, Intent, EntityExample
from app.schemas import IntentExampleCreate, IntentExampleUpdate
from typing import Optional

def CREATE(example: IntentExampleCreate, db: Session):
    db_example = IntentExample(
        intent_id   = example.intent_id, 
        example     = example.example, 
        description = example.description
    )

    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example


def READ_ALL(db: Session):
    examples = (
        db.query(
            IntentExample.id,
            IntentExample.intent_id,
            Intent.name.label("intent_name"),
            IntentExample.example,
            IntentExample.description
        )
        .join(IntentExample, IntentExample.intent_id == Intent.id)
        .all()
    )

    result = []
    for example in examples:
        db_en_example = db.query(
            EntityExample
        ).filter(
            example.id == EntityExample.example_id
        ).all()
        result.append(db_en_example)

    print(result)

    return result

def READ_MANY(intentID: int, db: Session):
    examples = (
        db.query(
            IntentExample.id,
            IntentExample.intent_id,
            Intent.name.label("intent_name"),
            IntentExample.example,
            IntentExample.description
        )
        .join(IntentExample, IntentExample.intent_id == Intent.id)
        .filter(IntentExample.intent_id == intentID)
    )
    return examples

def UPDATE(exampleID: int, example: IntentExampleUpdate, db: Session):
    db_example = db.query(IntentExample).filter(exampleID == IntentExample.id).first()
    if db_example:
        db_example.intent_id   = example.intent_id
        db_example.example     = example.example
        db_example.description = example.description
        db.commit()
        db.refresh(db_example)
        return db_example
    return None

def DELETE(exampleID: int, db: Session):
    db_example = db.query(IntentExample).filter(exampleID == IntentExample.id).first()
    if db_example:
        db.delete(db_example)
        db.commit()
        return True
    return None