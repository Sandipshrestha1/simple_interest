from fastapi import FastAPI
from routes.loan_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Loan Calculator API"}