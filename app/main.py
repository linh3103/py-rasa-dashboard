from fastapi import FastAPI
from app.helpers import Base, engine

Base.metadata.create_all(bind=engine)

from app.routes import intent_router

app = FastAPI()

app.include_router(intent_router)