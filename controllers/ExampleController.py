from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.ExampleSchema import ExampleCreate
from services import ExampleService

def create_example_controller(example: ExampleCreate, db: Session):
    try:
        return ExampleService.CREATE(example, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_all_examples_controller(db: Session):
    try:
        return ExampleService.ALL(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

# product_synonyms = ["sản phẩm", "hàng hóa", "mặt hàng", "đồ vật", "vật phẩm", "hàng"]
# concept_room_synonyms = ["các phòng", "những phòng", "một số phòng", "phòng", "không gian", "kiến trúc"]
# relation_synonyms = ["liên quan", "liên quan đến", "về"]
# action = ["Hiển thị", "show", "tôi muốn xem", "đề xuất", "gợi ý", "xem"]

from fastapi.responses import FileResponse
from collections import defaultdict
def create_examples_controller(db: Session):
    try:

        response = ExampleService.READ_TO_CREATE_EXAMPLE(db)

        intent_examples = defaultdict(list)
        for _, intent_name, example_name in response:
            intent_examples[intent_name].append(example_name)

       
        with open("nlu.yml", "a", encoding="utf-8") as file:
            for intent_name, examples in intent_examples.items():
                file.write(f"- intent: {intent_name}\n")
                file.write("  examples: |\n")
                for example in examples:
                    file.write(f"  - {example}\n")
                file.write("\n")

        return FileResponse(
            "nlu.yml",
            media_type="text/yaml",
            filename="nlu.yml"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
        