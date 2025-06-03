from app.schemas import EntityCreate, EntityResponse
from sqlalchemy.orm import Session
from app.services import EntityService as service

def create_entity(entity: EntityCreate, db: Session):
    return service.CREATE(entity, db)

def read_all_entity(db: Session):
    return service.READ_ALL(db)

def read_entity_by_id(id: int, db: Session):
    return service.READ_ONE(id, db)

def update_entity(entityID: int, entity: EntityCreate, db: Session):
    return service.UPDATE(entityID, entity, db)

def delete_entity(entityID: int, db: Session):
    return service.DELETE(entityID, db)

def export_entities(db: Session):
    entities = [EntityResponse.model_validate(item).model_dump() for item in service.READ_ALL(db)]
    entities_content = "entities:\n"
    for entity in entities:
        entities_content += f'  - {entity["entity_name"]}\n'

    with open("app/datas/entities.yml", "w") as file:
        file.write(entities_content)