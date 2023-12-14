from srvc.book_srvc import BookSrvc
from models.book import BookResponse

class BookController:
    def __init__(self, book_srvc: BookSrvc) -> None:
        self.book_srvc = book_srvc

    async def get_all_books(self):
        books = self.book_srvc.get_all_books()
        books_res = []
        for book in books:
            book_res = BookResponse()
            book_res.id = book[0]
            book_res.title = book[1]
            book_res.author = book[2]
            book_res.created_at = book[3]
            books_res.append(book_res)

        return books_res