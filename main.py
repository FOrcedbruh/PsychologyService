from fastapi import FastAPI
import uvicorn
from core.settings import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware
)



@app.get("/")
def index():
    return {
        "message": "Welcome to service"
    }



if __name__ == "__main__":
    uvicorn.run(app="main:app", port=settings.run.port, reload=settings.run.reload)