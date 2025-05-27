from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.helpers.database import get_db
from app.schemas import IntentCreate, IntentOut
from app.controllers import create_intent, read_all_intents

router = APIRouter(prefix="/intents", tags=["Intents"])

@router.post("/", response_model=IntentOut)
def createIntent(intent: IntentCreate, db: Session = Depends(get_db)):
    return create_intent(db, intent)

@router.get("/", response_model=list[IntentOut])
def readAllIntents(db: Session = Depends(get_db)):
    return read_all_intents(db)
