from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis-service")

r = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    try:
        r.incr("counter")
        count = r.get("counter").decode("utf-8")
        return f"Fluid AI DevOps Assignment Running Successfully. Visits: {count}"
    except Exception as e:
        return f"Redis connection failed: {str(e)}"

@app.route("/health")
def health():
    return "healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)