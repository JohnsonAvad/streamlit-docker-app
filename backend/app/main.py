from fastapi import FastAPI
from .database import save_record, get_records

app = FastAPI()  # Create our API application

@app.post("/calculate/")  # This handles calculation requests
async def calculate_loan(
    applicant_name: str,
    principal: float,
    months_number: int,
    monthly_interest_rate: float
):
    # Math calculations
    total_interest = (principal * (monthly_interest_rate / 100)) * months_number
    total_amount = principal + total_interest
    monthly_payment = total_amount / months_number
    
    # Package the data
    record = {
        "applicant_name": applicant_name,
        "total_amount": total_amount,
        "months_number": months_number,
        "interest_rate": monthly_interest_rate,
        "monthly_payment": monthly_payment
    }
    
    save_record(record)  # Save to CSV
    return record  # Send back to frontend

@app.get("/records/")  # This handles history requests
async def get_loan_records():
    return get_records()  # Return all records from CSV