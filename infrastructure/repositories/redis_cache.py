import redis

class RedisCache:
    def __init__(self, redis_url: str):
        self.redis_client = redis.from_url(redis_url)

    def get(self, key: str):
        value = self.redis_client.get(key)
        if value:
            return value.decode('utf-8')
        return None

    def set(self, key: str, value: str, ex: int = 3600):  # 1 hour expiration
        self.redis_client.set(key, value, ex=ex)