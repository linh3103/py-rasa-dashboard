from fastapi import APIRouter, Depends
from app.controllers import EntityController as controller
from sqlalchemy.orm import Session
from app.helpers import get_db
from app.schemas import EntityCreate, EntityResponse

router = APIRouter(prefix="/entity", tags=["Entity"])

@router.get("/", response_model=list[EntityResponse])
def readAllEntities(db: Session = Depends(get_db)):
    return controller.read_all_entity(db)

@router.post("/", response_model=EntityResponse)
def createEntity(entity: EntityCreate, db: Session = Depends(get_db)):
    return controller.create_entity(entity, db)

@router.put("/{entityID}", response_model=EntityResponse)
def updateEntity(entityID: int, entity: EntityCreate, db: Session = Depends(get_db)):
    return controller.update_entity(entityID, entity, db)

@router.delete("/{entityID}")
def deleteEntity(entityID: int, db: Session = Depends(get_db)):
    return controller.delete_entity(entityID, db)