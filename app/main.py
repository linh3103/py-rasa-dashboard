from fastapi import FastAPI
from app.helpers import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

from app.routes import intent_router, intent_example_router

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # có thể dùng ["*"] nếu public
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE"],  # hoặc giới hạn như ["GET", "POST"]
    allow_headers=["*"],
)

app.include_router(intent_router)
app.include_router(intent_example_router)