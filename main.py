from db.database import start_db
from repo.book_repo import BookRepo
from srvc.book_srvc import BookSrvc
from controllers.book_controller import BookController
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Db
db, cursor = start_db()

# Repo
book_repo = BookRepo(db, cursor)

# Srvc
book_srvc = BookSrvc(book_repo)

# Controllers
book_controller = BookController(book_srvc)

# Handlers
@app.get("/book")
async def get_all_books():
    return await book_controller.get_all_books()