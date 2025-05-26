from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from helpers.database import SessionLocal
import schemas.IntentSchema as IntentSchema
import sqlModels as models

router = APIRouter(prefix="/intents", tags=["Intents"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=IntentSchema.IntentOut)
def create_intent(intent: IntentSchema.IntentCreate, db: Session = Depends(get_db)):
    db_intent = models.Intent(name=intent.name, examples=intent.examples)
    db.add(db_intent)
    db.commit()
    db.refresh(db_intent)
    return db_intent
        
@router.get("/", response_model=list[IntentSchema.IntentOut])
def get_intents(db: Session = Depends(get_db)):
    print("Fetching all intents")
    return db.query(models.Intent).all()