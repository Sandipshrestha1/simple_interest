from pydantic import BaseModel

class LoanRequest(BaseModel):
    principal: float
    rate: float
    time: float