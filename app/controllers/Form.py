from app.schemas import FormWrite, FormResponse
from sqlalchemy.orm import Session
from app.services import FormService as service

def create_form(form: FormWrite, db: Session):
    return service.CREATE(form, db)

def read_all_forms(db: Session):
    return service.READ_ALL(db)

def read_form_by_id(id: int, db: Session):
    return service.READ_ONE(id, db)

def update_form(formID: int, form: FormWrite, db: Session):
    return service.UPDATE(formID, form, db)

def delete_form(formID: int, db: Session):
    return service.DELETE(formID, db)

def export_form(db: Session):
    forms = [FormResponse.model_validate(item).model_dump() for item in service.READ_ALL(db)]
    forms_content = "forms:\n"
    for form in forms:
        forms_content += f'  {form["form_name"]}:\n'
        forms_content += f'    required_slots:\n'

        fields = form["fields"].split(";")
        for field in fields:
            forms_content += f'      - {field}\n'

    with open("app/datas/forms.yml", "w") as file:
        file.write(forms_content)


    
