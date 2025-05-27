from sqlalchemy.orm import Session
from app.schemas import IntentCreate
from app.services import CREATE, READ_ALL

def create_intent(db: Session, intent: IntentCreate):
    return CREATE(intent, db)

def read_all_intents(db: Session):
    return READ_ALL(db)
