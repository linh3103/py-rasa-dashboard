from app.schemas import EntityCreate
from sqlalchemy.orm import Session
from app.services import EntityService as service

def create_entity(entity: EntityCreate, db: Session):
    return service.CREATE(entity, db)

def read_all_entity(db: Session):
    return service.READ_ALL(db)

def update_entity(entityID: int, entity: EntityCreate, db: Session):
    return service.UPDATE(entityID, entity, db)

def delete_entity(entityID: int, db: Session):
    return service.DELETE(entityID, db)