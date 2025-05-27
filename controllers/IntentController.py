from services import IntentService
from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.IntentSchema import IntentCreate

def create_intent_controller(intent: IntentCreate, db: Session):
    try:
        return IntentService.CREATE(intent, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_all_intents_controller(db: Session):
    try:
        return IntentService.ALL(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
