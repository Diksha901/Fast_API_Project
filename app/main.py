from fastapi import FastAPI,Depends,HTTPException,status,Query,APIRouter
from .api.endpoints import BogieSpecs #import create_bogie
from .api.endpoints import WheelsSpecification #import wheel

app=FastAPI()

app.include_router(BogieSpecs.create_bogie)
app.include_router(WheelsSpecification.wheel)
