from fastapi import FastAPI, Depends, HTTPException
from helpers.database import Base

from routes.IntentRoute import router as intent_router

app = FastAPI()

app.include_router(intent_router)