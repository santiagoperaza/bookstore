# app/main.py
from fastapi import FastAPI
from app.database import create_db_and_tables, engine, Base
from app.routers import books

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(books.router, prefix="/books", tags=["books"])
