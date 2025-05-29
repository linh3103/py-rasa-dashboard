from app.services   import EntityExampleService as service
from app.schemas    import EntityExampleWrite
from sqlalchemy.orm import Session

def create_entity_example(example: EntityExampleWrite, db: Session):
    return service.CREATE(example, db)

def delete_entity_example(eeID: int, db: Session):
    return service.DELETE(eeID, db)