from fastapi import APIRouter,Depends,status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session 
from ...db.database import get_db
from ...db.models import Bogie as BogieModel 
from ...db.schemas import Bogie
create_bogie=APIRouter(prefix='/api/forms',tags=['Bogie-Checking'])
@create_bogie.post('/bogie-checksheet')
def bogie_checking(bogie:Bogie,db:Session=Depends(get_db)):
    db_form=BogieModel(**bogie.model_dump())
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "data": {
                "formNumber": db_form.formNumber,
                "inspectionBy": db_form.inspectionBy,
                "inspectionDate": db_form.inspectionDate,
                "status": "Saved"
            },
            "message": "Bogie checksheet submitted successfully.",
            "success": True
        }
    )