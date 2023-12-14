from repo.book_repo import BookRepo

class BookSrvc:
    def __init__(self, book_repo: BookRepo) -> None:
        self.book_repo = book_repo

    def get_all_books(self):
        return self.book_repo.get_all()