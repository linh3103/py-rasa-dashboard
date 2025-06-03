from sqlalchemy.orm import Session
from app.schemas import SlotWrite, SlotResponse, EntityResponse
from app.services import SlotService, EntityService

def read_all_slots(db: Session):
    return SlotService.READ_ALL_SLOT(db)

def create_slot(slot: SlotWrite, db: Session):
    return SlotService.CREATE(slot, db)

def update_slot(id: int, slot: SlotWrite, db: Session):
    return SlotService.UPDATE(id, slot, db)

def delete_slot(id: int, db: Session):
    return SlotService.DELETE(id, db)

def create_slot_by_entity(entity_id: int, db: Session):
    entity = EntityService.READ_ONE(entity_id, db)
    if entity:
        entity_dict = EntityResponse.model_validate(entity).model_dump()
        slot = SlotWrite(
            name=entity_dict["entity_name"],
            auto_fill=True,
            entity_name=entity_dict["entity_name"],
            influence_conversation=False,
            initial_value="",
            type="text",
            description=""
        )

        return SlotService.CREATE(slot, db)
    
def create_slots_by_all_entities(db: Session):
    entities = [EntityResponse.model_validate(entity).model_dump() for entity in EntityService.READ_ALL(db)]
    slots = [SlotResponse.model_validate(slot).model_dump() for slot in SlotService.READ_ALL_SLOT(db)]

    slot_names = []
    if len(slots) > 0:
        for slot in slots:
            slot_name = slot["name"]
            slot_names.append(slot_name)

    slots_response = []
    for entity in entities:
        entity_name=entity["entity_name"]
        if entity_name not in slot_names:
            new_slot = SlotWrite(
                name=entity_name,
                type="text",
                entity_name=entity_name,
                auto_fill=True,
                influence_conversation=False,
                initial_value="",
                description=""
            )

            slot_response = SlotService.CREATE(new_slot, db)
            slots_response.append(slot_response)

    return slots_response

        

