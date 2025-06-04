from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.controllers import SlotController as controller
from app.schemas import SlotWrite, SlotResponse
from app.helpers import get_db

router = APIRouter(prefix="/slots", tags=["Slots"])

@router.get("/", response_model=list[SlotResponse])
def readAllSlots(db: Session = Depends(get_db)):
    return controller.read_all_slots(db)

@router.post("/", response_model=SlotResponse)
def createSlot(slot: SlotWrite, db: Session = Depends(get_db)):
    return controller.create_slot(slot, db)

@router.get("/create_by_entity/{entity_id}")
def createSlotByEntity(entity_id, db: Session = Depends(get_db)):
    return controller.create_slot_by_entity(entity_id, db)

@router.get("/create_by_all_entities", response_model=list[SlotResponse])
def createSlotsByAllEntities(db: Session=Depends(get_db)):
    return controller.create_slots_by_all_entities(db)

@router.put("/{slot_id}", response_model=SlotResponse)
def updateSlot(slot_id: int, slot: SlotWrite, db: Session = Depends(get_db)):
    return controller.create_slot(slot_id, slot, db)

@router.delete("/{slot_id}")
def deleteSlot(slot_id: int, db: Session = Depends(get_db)):
    return controller.delete_slot(slot_id, db)

@router.get("/export")
def exportSlots(db: Session = Depends(get_db)):
    return controller.export_slots(db)