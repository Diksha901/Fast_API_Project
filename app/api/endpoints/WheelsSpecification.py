from fastapi import APIRouter,Depends,Query,HTTPException,status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from ...db.database import get_db
from ...db.schemas import Wheels
from ...db.models import Wheels as WheelModel 
wheel=APIRouter(prefix='/api/forms',tags=['wheels-specification'])
@wheel.post('/wheel-specification')
def Create_Wheels(wheels:Wheels,db:Session=Depends(get_db)):
    db_form=WheelModel(**wheels.model_dump())
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return JSONResponse(
        status_code=201,
        content={
            "data": {
                "formNumber": db_form.formNumber,
                "submittedBy": db_form.submittedBy,
                "submittedDate": db_form.submittedDate,
                "status": "Saved"
            },
            "message": "Wheel Specification submitted successfully.",
            "success": True
        }
    )
@wheel.get('/wheel-specifications')
def getWheel(form_number: str=Query(None),submitted_by:str=Query(None),submitted_date:str=Query(None),db:Session=Depends(get_db)):
    # Build the query step-by-step to allow flexible filtering
    query = db.query(WheelModel)
    if form_number:
        query = query.filter(WheelModel.formNumber == form_number)
    if submitted_by:
        query = query.filter(WheelModel.submittedBy == submitted_by)
    if submitted_date:
        query = query.filter(WheelModel.submittedDate == submitted_date)

    form = query.first()

    if not form:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Form with formNumber={form_number} not found"
        )

    result = {
        "fields": form.fields,
        "formNumber": form.formNumber,
        "submittedBy": form.submittedBy,
        "submittedDate": form.submittedDate
    }

    return JSONResponse(
        status_code=200,
        content={
            "data": [result],
            "message": "Filtered wheel specification forms fetched successfully.",
            "success": True
        }
    )
