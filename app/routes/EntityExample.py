from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.helpers import get_db
from app.schemas import EntityExampleWrite, EntityExampleRead
from app.controllers import EntityExampleController as controller

router = APIRouter(prefix="/entity_examples", tags=["Entity examples"])

@router.post("/", response_model=EntityExampleWrite)
def addEntityExample(example: EntityExampleWrite, db: Session = Depends(get_db)):
    return controller.create_entity_example(example, db)

@router.get("/{page}")
def readAllEntityExample():
    print("get all entity example")

@router.get("/{entityID}/{page}")
def readManyEntityExample():
    print("get many entity example")

@router.put("/{entityID}")
def updateEntityExample(entityID: int, ee: EntityExampleWrite, db: Session = Depends(get_db)):
    return controller.update_entity_example(entityID, ee, db)

@router.delete("/{entityID}")
def deleteEntityExample(entityID: int, db: Session=Depends(get_db)):
    return controller.delete_entity_example(entityID, db)
