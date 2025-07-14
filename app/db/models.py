from sqlalchemy import Column, Integer, String, JSON

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Bogie(Base):
    __tablename__ = "bogies"

    id = Column(Integer, primary_key=True, index=True)
    bmbcChecksheet = Column(JSON, nullable=True)
    bogieChecksheet=Column(JSON,nullable=True)
    bogieDetails=Column(JSON,nullable=True)
    formNumber=Column(String,nullable=False)
    inspectionBy=Column(String,nullable=False)
    inspectionDate=Column(String,nullable=False)
class Wheels(Base):
    __tablename__='wheels'
    id=Column(Integer,nullable=False,primary_key=True)
    fields=Column(JSON,nullable=True)
    formNumber=Column(String,nullable=False)
    submittedBy=Column(String,nullable=False)
    submittedDate=Column(String,nullable=False)

