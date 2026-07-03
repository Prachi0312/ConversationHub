from fastapi import FastAPI
from backend.app.api.customer import router as customer_router

app = FastAPI(
    title="ConversationHub",
    version="1.0.0"
)

app.include_router(customer_router)

@app.get("/")
def home():
    return {
        "message": "ConversationHub API is running 🚀"
    }