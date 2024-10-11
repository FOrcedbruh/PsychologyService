from fastapi import FastAPI
import uvicorn
from core.settings import settings

app = FastAPI()


@app.get("/")
def index():
    return "Hello"

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=settings.run.port, reload=settings.run.reload)