from fastapi import APIRouter
from models.loan_model import LoanRequest
from services.loan_service import calculate_simple_interest

router = APIRouter()

@router.post("/simple-interest")
def simple_interest(data: LoanRequest):

    interest, total = calculate_simple_interest(
        data.principal,
        data.rate,
        data.time
    )

    return {
        "principal": data.principal,
        "interest": interest,
        "total_amount": total
    }