from fastapi import APIRouter, Depends
from app.controllers import FormController as controller
from sqlalchemy.orm import Session
from app.helpers import get_db
from app.schemas import FormWrite, FormResponse

router = APIRouter(prefix="/form", tags=["Form"])

@router.get("/", response_model=list[FormResponse])
def readAllForms(db: Session = Depends(get_db)):
    return controller.read_all_forms(db)

@router.post("/", response_model=FormResponse)
def createForm(form: FormWrite, db: Session = Depends(get_db)):
    return controller.create_form(form, db)

@router.put("/{formID}", response_model=FormResponse)
def updateForm(formID: int, form: FormWrite, db: Session = Depends(get_db)):
    return controller.update_form(formID, form, db)

@router.delete("/{formID}")
def deleteForm(formID: int, db: Session = Depends(get_db)):
    return controller.delete_form(formID, db)

@router.get("/export")
def exportForms(db: Session=Depends(get_db)):
    return controller.export_form(db)
