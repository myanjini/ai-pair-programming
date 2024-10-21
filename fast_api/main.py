from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users")
def get_users():
    users = [
        {"name": "Alice", "age": 30, "contact": "alice@example.com"},
        {"name": "Bob", "age": 25, "contact": "bob@example.com"},
        {"name": "Charlie", "age": 35, "contact": "charlie@example.com"}
    ]
    return users

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
