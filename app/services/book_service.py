# app/services/book_service.py
from sqlalchemy.orm import Session
from app.repositories.book_repository import BookRepository

class BookService:
    def __init__(self, db: Session):
        self.repository = BookRepository(db)

    def create_book(self, book_data):
        return self.repository.create_book(book_data)

    def get_all(self):
        return self.repository.get_all()

    def get_book(self, book_id: int):
        book = self.repository.get_book(book_id)
        if book is None:
            raise Exception("Book not found")
        return book
