from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from helpers.database import get_db
import schemas.IntentSchema as IntentSchema

from controllers import create_intent_controller, get_all_intents_controller

router = APIRouter(prefix="/intents", tags=["Intents"])

@router.post("/", response_model=IntentSchema.IntentOut)
def create_intent(intent: IntentSchema.IntentCreate, db: Session = Depends(get_db)):
    return create_intent_controller(intent, db)

@router.get("/", response_model=list[IntentSchema.IntentOut])
def get_intents(db: Session = Depends(get_db)):
    return get_all_intents_controller(db)