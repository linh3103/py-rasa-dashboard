from sqlalchemy.orm import Session
from app.models import Entity
from app.schemas import EntityCreate


def CREATE(entity: EntityCreate, db: Session):
    db_entity = Entity(
        entity_name=entity.entity_name, 
        description=entity.description
    )

    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)

    return db_entity

def READ_ALL(db: Session):
    return db.query(Entity).all()

def READ_ONE(id: int, db: Session):
    return db.query(Entity).filter(Entity.id == id).first()

def UPDATE(entityID: int, entity: EntityCreate, db: Session):
    db_entity = db.query(Entity).filter(entityID == Entity.id).first()
    if db_entity:
        db_entity.entity_name = entity.entity_name
        db_entity.description = entity.description
        db.commit()
        db.refresh(db_entity)
        return db_entity
    return None

def DELETE(entityID, db: Session):
    db_entity = db.query(Entity).filter(entityID == Entity.id).first()
    if db_entity:
        db.delete(db_entity)
        db.commit()
        return True
    return False
