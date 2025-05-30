from sqlalchemy.orm import Session
from app.models import IntentExample, Intent, EntityExample, Entity
from app.schemas import IntentExampleCreate, IntentExampleUpdate, IntentExampleRead

from typing import Optional
from collections import defaultdict

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
    intent_examples = (
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

    entity_example_dict = defaultdict(list)
    entity_examples = (
        db.query(
            EntityExample,
            Entity.entity_name
        )
        .join(Entity)
        .all()
    )

    for ee, entity_name in entity_examples:
        ee.entity_name = entity_name
        entity_example_dict[ee.example_id].append(ee)

    result = []
    for ex in intent_examples:
        ex_dict = {
            "id": ex.id,
            "intent_id": ex.intent_id,
            "intent_name": ex.intent_name,
            "example": ex.example,
            "description": ex.description,
            "entities": entity_example_dict.get(ex.id, [])
        }
        result.append(IntentExampleRead(**ex_dict))

    return result

def READ_MANY(intentID: int, db: Session):
    intent_examples = (
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


    entity_example_dict = defaultdict(list)
    entity_examples = (
        db.query(
            EntityExample,
            Entity.entity_name
        )
        .join(Entity)
        .all()
    )

    for ee, entity_name in entity_examples:
        ee.entity_name = entity_name
        entity_example_dict[ee.example_id].append(ee)

    result = []
    for ex in intent_examples:
        ex_dict = {
            "id": ex.id,
            "intent_id": ex.intent_id,
            "intent_name": ex.intent_name,
            "example": ex.example,
            "description": ex.description,
            "entities": entity_example_dict.get(ex.id, [])
        }
        result.append(IntentExampleRead(**ex_dict))

    return result

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