from domain.entities import Book
from domain.repositories import AbstractBookRepository

class BookService:
    def __init__(self, book_repository: AbstractBookRepository):
        self.book_repository = book_repository

    def get_all_books(self) -> list[Book]:
        return self.book_repository.get_all()

    def get_book_by_id(self, book_id: int) -> Book:
        return self.book_repository.get_by_id(book_id)

    def create_book(self, book: Book) -> Book:
        return self.book_repository.create(book)

    def update_book(self, book: Book) -> Book:
        return self.book_repository.update(book)

    def delete_book(self, book_id: int) -> None:
        self.book_repository.delete(book_id)