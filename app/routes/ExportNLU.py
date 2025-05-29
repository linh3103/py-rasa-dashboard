from app.controllers import IntentController, IntentExampleController
from fastapi import APIRouter, Depends
from app.schemas import IntentOut, IntentExampleRead
from sqlalchemy.orm import Session
from app.helpers import get_db
from collections import defaultdict
from fastapi.responses import FileResponse

router = APIRouter(prefix="/export", tags=["Export"])

@router.get("/nlu")
def exportNLU(db: Session = Depends(get_db)):

    nluContent = "version: \"3.1\"\nnlu:"

    result = IntentExampleController.read_all_intent_expl(db)
    exampleList = [IntentExampleRead.model_validate(e).model_dump() for e in result]
    

    grouped = defaultdict(list)
    for example in exampleList:
        grouped[example["intent_name"]].append(example["example"])

    for intent, examples in grouped.items():
        nluContent += f"\n- intent: {intent}\n"
        nluContent += "  examples: |\n"
        for example in examples:
            nluContent += f"  - {example}\n"
    
    with open("nlu.yml", "w", encoding="utf-8") as file:
        file.write(nluContent)

    return FileResponse("nlu.yml", media_type="application/x-yaml", filename="nlu.yml")

        