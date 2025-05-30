from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.services import IntentExampleService as service
from app.schemas import IntentExampleCreate, IntentExampleUpdate

def create_intent_expl(example: IntentExampleCreate, db: Session):
    return service.CREATE(example, db)

def read_all_intent_expl(db: Session):
    intent_examples = service.READ_ALL(db)
    # print("list: ", intent_examples)
    return intent_examples
    
def read_many_intent_expl(intentID: int, db: Session):
    return service.READ_MANY(intentID, db)

def update_intent_expl(exampleID: int, example: IntentExampleUpdate, db: Session):
    return service.UPDATE(exampleID, example, db)

def delete_intent_expl(exampleID: int, db: Session):
    return service.DELETE(exampleID, db)