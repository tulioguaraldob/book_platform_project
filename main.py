from fastapi import FastAPI, Depends
from application.api.v1.routers import book_router
from infrastructure.repositories.mysql_repository import MySQLBookRepository
from infrastructure.repositories.redis_cache import RedisCache
import logging

app = FastAPI()
logger = logging.getLogger(__name__)

logger.info("Attempting to connect to MySQL Server database")

def get_mysql_repository():
    db_url = "mysql://root:root@127.0.0.1:3306/books"  # Replace with your actual database URL
    return MySQLBookRepository(db_url)

logger.info("Attempting to connect to Redis cache")

def get_redis_cache():
    redis_url = "redis://localhost:6379"  # Replace with your actual Redis URL
    return RedisCache(redis_url)

app.include_router(book_router.get_router(), dependencies=[Depends(get_mysql_repository)])

# ... (Optional: Add caching logic using RedisCache)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)