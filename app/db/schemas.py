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
# "fields": {
#     "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
#     "bearingSeatDiameter": "130.043 TO 130.068",
#     "condemningDia": "825 (800-900)",
#     "intermediateWWP": "20 TO 28",
#     "lastShopIssueSize": "837 (800-900)",
#     "rollerBearingBoreDia": "130 (+0.0/-0.025)",
#     "rollerBearingOuterDia": "280 (+0.0/-0.035)",
#     "rollerBearingWidth": "93 (+0/-0.250)",
#     "treadDiameterNew": "915 (900-1000)",
#     "variationSameAxle": "0.5",
#     "variationSameBogie": "5",
#     "variationSameCoach": "13",
#     "wheelDiscWidth": "127 (+4/-0)",
#     "wheelGauge": "1600 (+2,-1)",
#     "wheelProfile": "29.4 Flange Thickness"
#   },
#   "formNumber": "WHEEL-2025-001",
#   "submittedBy": "user_id_123",
#   "submittedDate": "2025-07-03"