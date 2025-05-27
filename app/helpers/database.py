from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "mysql+pymysql://root@localhost/py_rasa_dashboard"

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    print("session created")
    try:
        yield db
    finally:
        print("session closed")
        db.close()