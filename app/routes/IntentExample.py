from app.controllers import IntentExampleController as controller
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.helpers import get_db
from app.schemas import IntentExampleCreate, IntentExampleUpdate, IntentExampleRead, IntentExampleResponse

router = APIRouter(prefix="/intent_examples", tags=["Intent example"])

@router.post("/", response_model=IntentExampleResponse)
def addIntentExample(example: IntentExampleCreate, db: Session = Depends(get_db)):
    return controller.create_intent_expl(example, db)

@router.get("/", response_model=list[IntentExampleRead])
def readAllIntentExample(db: Session = Depends(get_db)):
    return controller.read_all_intent_expl(db)

@router.get("/{intentID}", response_model=list[IntentExampleRead])
def readManyIntentExample(intentID: int, db: Session = Depends(get_db)):
    return controller.read_many_intent_expl(intentID, db)

@router.put("/{exampleID}", response_model=IntentExampleResponse)
def updateIntentExample(exampleID: int, example: IntentExampleUpdate, db: Session = Depends(get_db)):
    return controller.update_intent_expl(exampleID, example, db)

@router.delete("/{exampleID}")
def deleteIntentExample(exampleID: int, db: Session = Depends(get_db)):
    return controller.delete_intent_expl(exampleID, db)