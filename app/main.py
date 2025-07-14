from fastapi import FastAPI
from .api.endpoints import BogieSpecs 
from .api.endpoints import WheelsSpecification 

app=FastAPI()

app.include_router(BogieSpecs.create_bogie)
app.include_router(WheelsSpecification.wheel)
