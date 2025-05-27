from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from helpers.database import get_db
from schemas.ExampleSchema import ExampleCreate, ExampleOut, ExampleJoin
from controllers import create_example_controller, get_all_examples_controller, create_examples_controller

router = APIRouter(prefix="/example", tags=["Example"])

@router.get("/", response_model=list[ExampleOut])
def get_examples(db: Session = Depends(get_db)):
    return get_all_examples_controller(db)

@router.post("/", response_model=ExampleOut)
def create_example(example: ExampleCreate, db: Session = Depends(get_db)):
    return create_example_controller(example, db)

@router.get("/create_examples", response_model=list[ExampleJoin])
def create_examples(db: Session = Depends(get_db)):
    return create_examples_controller(db)