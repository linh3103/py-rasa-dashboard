from sqlalchemy.orm import Session
from app.models import Form
from app.schemas import FormWrite

def CREATE(form: FormWrite, db: Session):
    db_form = Form(
        form_name=form.form_name,
        fields=form.fields,
        description=form.description
    )

    db.add(db_form)
    db.commit()
    db.refresh(db_form)

    return db_form

def READ_ALL(db: Session):
    return db.query(Form).all()

def READ_ONE(id: int, db: Session):
    return db.query(Form).filter(Form.id == id).first()

def UPDATE(formID: int, form: FormWrite, db: Session):
    db_form = db.query(Form).filter(formID == Form.id).first()
    if db_form:
        db_form.form_name = form.form_name
        db_form.fields = form.fields
        db_form.description = form.description
        db.commit()
        db.refresh(db_form)
        return db_form
    return None

def DELETE(formID: int, db: Session):
    db_form = db.query(Form).filter(formID == Form.id).first()
    if db_form:
        db.delete(db_form)
        db.commit()
        return True
    return False
