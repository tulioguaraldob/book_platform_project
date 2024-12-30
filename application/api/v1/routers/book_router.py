from fastapi import APIRouter, Depends
from typing import List
from application.services.book_service import BookService
from domain.entities import Book
from domain.repositories import AbstractBookRepository

router = APIRouter(prefix="/books", tags=["Books"])

def get_book_service(book_repository: AbstractBookRepository) -> BookService:
    return BookService(book_repository)

@router.get("/", response_model=List[Book])
async def list_books(book_service: BookService = Depends(get_book_service)):
    return book_service.get_all_books()

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int, book_service: BookService = Depends(get_book_service)):
    book = book_service.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=Book)
async def create_book(book: Book, book_service: BookService = Depends(get_book_service)):
    return book_service.create_book(book)

@router.put("/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book, book_service: BookService = Depends(get_book_service)):
    book.id = book_id
    updated_book = book_service.update_book(book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/{book_id}")
async def delete_book(book_id: int, book_service: BookService = Depends(get_book_service)):
    book_service.delete_book(book_id)
    return {"message": "Book deleted successfully"}

def get_router():
    return router