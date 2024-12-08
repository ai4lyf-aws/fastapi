from fastapi import FastAPI

app = FastAPI(
    root_path="/fastapi"
)

@app.get("/", status_code=200)
def read_root():
    return {"message": "Hello, World ecs ngisndis !"}

@app.get("/items", status_code=200)
def read_items():
    return {"items": ["Item 1", "Item 2", "Item 3"]}
