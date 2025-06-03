from fastapi import FastAPI
from app.helpers import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

from app.routes import *

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(intent_router)
app.include_router(intent_example_router)
app.include_router(exporting_router)
app.include_router(entity_router)
app.include_router(entity_example_router)
app.include_router(slot_router)
