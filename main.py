from fastapi import FastAPI
from helpers.database import Base, engine

from routes import intent_router
from routes import example_router
# from routes import synonym_router
# from routes import synonym_example_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(intent_router)
app.include_router(example_router)
# app.include_router(synonym_router)
# app.include_router(synonym_example_router)