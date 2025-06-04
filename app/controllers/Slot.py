from sqlalchemy.orm import Session
from app.schemas import SlotWrite, SlotResponse, EntityResponse, FormResponse
from app.services import SlotService, EntityService, FormService
from collections import defaultdict
import pprint

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
    slots    = [SlotResponse.model_validate(slot).model_dump() for slot in SlotService.READ_ALL_SLOT(db)]

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

def export_slots(db: Session):
    entities = [EntityResponse.model_validate(entity).model_dump() for entity in EntityService.READ_ALL(db)]
    entity_names = [entity["entity_name"] for entity in entities]
    forms    = [FormResponse.model_validate(form).model_dump() for form in FormService.READ_ALL(db)]

    slots_content = "slots:\n"
    slot_forms = defaultdict(list)
    for form in forms:
        fields = form["fields"].split(";")
        for field in fields:
            slot_forms[field].append(form["form_name"])

    for entity_name in entity_names:
        if entity_name not in slot_forms.keys():
            slot_forms[entity_name] = []

    for field, form_names in slot_forms.items():
        slots_content += f"  {field}:\n"
        slots_content += f"    type: text\n"
        # slots_content += f"    influence_conversation: true\n"
        slots_content += f"    mappings:\n"

        conditions_content = ""
        if len(form_names) > 0:
            conditions_content = "conditions:\n"
            for form_name in form_names:
                conditions_content += f"          - active_loop: {form_name}\n"
                conditions_content += f"            requested_slot: {field}\n"

            slots_content += f"      - type: from_text\n"
            slots_content += f"        {conditions_content}\n"

        if field in entity_names:
            slots_content += f"      - type: from_entity\n"
            slots_content += f"        entity: {field}\n"
            slots_content += f"        {conditions_content}\n"



    with open("app/datas/slots.yml", "w") as s:
        s.write(slots_content)

    response_content = "responses:\n"
    for slot in slot_forms.keys():
        response_content += f"  utter_ask_{slot}:\n"
        response_content += f"    - text: \n"

    with open("app/datas/responses.yml", "w") as r:
        r.write(response_content)
    
    

