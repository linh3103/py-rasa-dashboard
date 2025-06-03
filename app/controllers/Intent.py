from sqlalchemy.orm import Session
from app.schemas import IntentCreate, IntentUpdate, IntentOut
from app.services import CREATE, READ_ALL, UPDATE, DELETE
from fastapi.responses import JSONResponse
from app.schemas import IntentOut

def create_intent(db: Session, intent: IntentCreate):
    return CREATE(intent, db)

def read_all_intents(db: Session):
    return READ_ALL(db)

def update_intent(intentID: int, intent: IntentUpdate, db: Session):
    return UPDATE(intentID, intent, db)

def delete_intent(intentID: int, db: Session):
    result = DELETE(intentID, db)
    if result == True:
        return JSONResponse({"success": True, "message": "Đã xóa"})
    return JSONResponse({"success": False, "message": "Đã xảy ra lỗi"})


def export_intents(db: Session):
    intents = [IntentOut.validate(intent).model_dump() for intent in READ_ALL(db)]
    intents_content = "intents:\n"
    for intent in intents:
        print(type(intent))
        name = intent["name"]
        intents_content += f"  - {name}\n"

    with open("app/datas/intents.yml", "w") as file:
        file.write(intents_content)
