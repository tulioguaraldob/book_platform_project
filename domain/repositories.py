from abc import ABC, abstractmethod
from dataclasses import dataclass
from .entities import Book

@dataclass
class AbstractBookRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Book]:
        pass

    @abstractmethod
    def get_by_id(self, book_id: int) -> Book:
        pass

    @abstractmethod
    def create(self, book: Book) -> Book:
        pass

    @abstractmethod
    def update(self, book: Book) -> Book:
        pass

    @abstractmethod
    def delete(self, book_id: int) -> None:
        pass