from sqlalchemy.orm import Session
from app.models import Intent
from app.schemas import IntentCreate

def CREATE(intent: IntentCreate, db: Session):
    db_intent = Intent(name=intent.name, description=intent.description)
    db.add(db_intent)
    db.commit()
    db.refresh(db_intent)
    return db_intent

def READ_ALL(db: Session):
    return db.query(Intent).all()