from schemas.IntentSchema import IntentCreate
from sqlalchemy.orm import Session
import sqlModels as models

def CREATE(intent: IntentCreate, db: Session):
    db_intent = models.Intent(name=intent.name, description=intent.description)
    db.add(db_intent)
    db.commit()
    db.refresh(db_intent)
    return db_intent

def ALL(db: Session):
    print("Fetching all intents")
    result = db.query(models.Intent).all()
    print("Type: ", type(result))
    return result