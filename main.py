from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World ecs ngisndis !"}

@app.get("/items")
def read_items():
    return {"items": ["Item 1", "Item 2", "Item 3"]}
