from sqlalchemy.orm import Session
from app.models import Intent
from app.schemas import IntentCreate, IntentUpdate

def CREATE(intent: IntentCreate, db: Session):
    db_intent = Intent(name=intent.name, description=intent.description)
    db.add(db_intent)
    db.commit()
    db.refresh(db_intent)
    return db_intent

def READ_ALL(db: Session):
    return db.query(Intent).all()

def UPDATE(intentID: int, intent: IntentUpdate, db: Session):
    
    # Tìm db_intent theo intentID
    db_intent = db.query(Intent).filter(intentID == Intent.id).first()
    # Nếu tìm thấy thì cập nhật
    if db_intent:
        db_intent.name = intent.name
        db_intent.description = intent.description
        db.commit()
        db.refresh(db_intent)
        return db_intent
    
    return None


def DELETE(intentID: int, db: Session):
    db_intent = db.query(Intent).filter(intentID == Intent.id).first()
    if db_intent:
        db.delete(db_intent)
        db.commit()
        return True
    return False