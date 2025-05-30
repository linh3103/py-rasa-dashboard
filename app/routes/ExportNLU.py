from app.controllers import IntentExampleController
from fastapi import APIRouter, Depends
from app.schemas import IntentExampleRead, EntityExampleRead
from sqlalchemy.orm import Session
from app.helpers import get_db
from collections import defaultdict
from fastapi.responses import FileResponse
from pprint import pprint


router = APIRouter(prefix="/export", tags=["Export"])

@router.get("/nlu")
def exportNLU(db: Session = Depends(get_db)):

    # Khai báo định dạng nlu
    nluContent = "version: \"3.1\"\nnlu:"

    # Lấy danh sách example
    result = IntentExampleController.read_all_intent_expl(db)
    # Chuyển danh sách example từ tupple sang dict
    exampleList = [IntentExampleRead.model_validate(e).model_dump() for e in result]
    
    intent_examples_entities = defaultdict(list)

    for item in exampleList:
        intent      = item["intent_name"]
        example     = item["example"]
        entities    = item["entities"]

        intent_examples_entities[intent].append({
            "example": example,
            "entities": entities
        })

    for intent, examples in intent_examples_entities.items():
        nluContent += f"\n- intent: {intent}\n"
        nluContent += "  examples: |\n"

        for item in examples:
            example  = item["example"]
            entities = item["entities"]

            nluExample = formatEntityString(example, entities)

            nluExample = f"  - {nluExample}\n"
            nluContent += nluExample
    
    with open("nlu.yml", "w", encoding="utf-8") as file:
        file.write(nluContent)

    return FileResponse("nlu.yml", media_type="application/x-yaml", filename="nlu.yml")

        
def formatEntityString(text, entities):
    if not entities:
        return text

    entities = sorted(entities, key=lambda x: x["char_start"])
    offset = 0

    for entity in entities:
        start = entity["char_start"] + offset
        end = entity["char_end"] + 1 + offset

        entity_text = text[start:end]
        entity_name = entity["entity_name"]
        value       = entity["value"]

        replacement = f'[{entity_text}]{{"entity": "{entity_name}", "value": "{value}"}}'

        text = text[:start] + replacement + text[end:]

        offset += len(replacement) - (end - start)

    return text