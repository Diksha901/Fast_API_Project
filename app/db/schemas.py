from pydantic import BaseModel
from typing import Dict
class Checks(BaseModel):
    adjustingTube :str 
    cylinderBody :str
    pistonTurning:str 
    plungerSpring:str 
class Components(BaseModel):
    axleGuide:str 
    bogieFrameCondition:str 
    bolster:str 
    bolsterSuspensionBracket:str 
    lowerSppringSheet:str 
class Details(BaseModel):
    bogieNo:str 
    dateOfIOH:str 
    deficitComponents:str 
    incomingDivandDate:str 
    makeYearBuilt:str 
class Bogie(BaseModel):
    bmbcChecksheet: Checks
    bogieChecksheet:Components
    bogieDetails:Details
    formNumber:str 
    inspectionBy:str 
    inspectionDate:str 
 
#######################
class WheelComps(BaseModel):
    axleBoxHousingBoreDia: str
    bearingSeatDiameter: str
    condemningDia: str
    intermediateWWP: str
    lastShopIssueSize: str
    rollerBearingBoreDia: str
    rollerBearingOuterDia: str
    rollerBearingWidth: str
    treadDiameterNew: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelDiscWidth: str
    wheelGauge: str
    wheelProfile:str
class Wheels(BaseModel):
    fields:WheelComps 
    formNumber:str 
    submittedBy:str 
    submittedDate:str 
