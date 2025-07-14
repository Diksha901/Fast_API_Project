from sqlalchemy import create_engine
from .models import Base
from sqlalchemy.orm import sessionmaker
engine = create_engine("postgresql://postgres:postgres@localhost:5432/kpa_db")
SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

