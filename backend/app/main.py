from fastapi import FastAPI
from backend.app.database.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ConversationHub")

@app.get("/")
def home():
    return {
        "message": "ConversationHub API is running 🚀"
    }