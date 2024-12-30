from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from domain.entities import Book
from domain.repositories import AbstractBookRepository
import logging

Base = declarative_base()

class BookModel(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

    def to_domain(self) -> Book:
        return Book(id=self.id, title=self.title, author=self.author)

class MySQLBookRepository(AbstractBookRepository):
    def __init__(self, db_url: str):
        self.logger = logging.getLogger(__name__)
        try:
            self.engine = create_engine(db_url)
            Base.metadata.create_all(self.engine)
            self.session = self.engine.connect()
            self.logger.info("MySQL connection successful.")
        except Exception as e:
            self.logger.error(f"MySQL connection failed: {e}")
            raise

    def get_all(self) -> list[Book]:
        result = self.session.query(BookModel).all()
        return [book.to_domain() for book in result]

    def get_by_id(self, book_id: int) -> Book:
        result = self.session.query(BookModel).filter_by(id=book_id).first()
        if result:
            return result.to_domain()
        return None

    def create(self, book: Book) -> Book:
        new_book = BookModel(title=book.title, author=book.author)
        self.session.add(new_book)
        self.session.commit()
        return new_book.to_domain()

    def update(self, book: Book) -> Book:
        existing_book = self.session.query(BookModel).filter_by(id=book.id).first()
        if existing_book:
            existing_book.title = book.title
            existing_book.author = book.author
            self.session.commit()
            return book
        return None

    def delete(self, book_id: int) -> None:
        self.session.query(BookModel).filter_by(id=book_id).delete()
        self.session.commit()