# app/repositories/book_repository.py
from sqlmodel import select
from sqlalchemy.orm import Session
from app.models import Book as BookModel

class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_book(self, book_data):
        db_book = BookModel(**book_data)
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book

    def get_all(self):
        return self.db.exec(select(BookModel)).all()

    def get_book(self, book_id: int):
        return self.db.get(BookModel, book_id)
