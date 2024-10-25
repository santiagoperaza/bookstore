# app/routers/books.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.models import BookResponse
from sqlalchemy.orm import Session
from app.schemas import BookCreate, Book
from app.database import get_session
from app.services.book_service import BookService

router = APIRouter()

@router.post("/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_session)):
    service = BookService(db)
    return service.create_book(book.dict())

@router.get("/", response_model=List[BookResponse])
def read_book(db: Session = Depends(get_session)):
    service = BookService(db)
    return service.get_all()

@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_session)):
    service = BookService(db)
    try:
        return service.get_book(book_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Book not found")
