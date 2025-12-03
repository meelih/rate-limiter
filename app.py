from fastapi import FastAPI, Request
import redis
from datetime import datetime

app = FastAPI()
r = redis.Redis(host="redis", port=6379, db=0)

LIMIT = 5  # requests per minute

@app.get("/")
def index(request: Request):
    ip = request.client.host
    minute = datetime.utcnow().strftime("%Y%m%d%H%M")
    key = f"rate:{ip}:{minute}"

    count = r.incr(key)
    r.expire(key, 60)

    if count > LIMIT:
        return {"status": "blocked", "msg": "Rate limit exceeded"}

    return {"status": "ok", "requests": int(count)}
