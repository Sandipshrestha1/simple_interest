from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.loan_routes import router

app = FastAPI()

# ✅ CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Loan Calculator API"}