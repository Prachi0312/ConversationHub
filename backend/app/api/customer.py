from fastapi import APIRouter

router = APIRouter(prefix="/customers", tags=["Customers"])

customers = []

@router.get("/")
def get_customers():
    return customers

@router.post("/")
def create_customer(customer: dict):
    customers.append(customer)
    return {
        "message": "Customer created",
        "customer": customer
    }