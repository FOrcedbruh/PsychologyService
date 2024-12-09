from fastapi import FastAPI
import uvicorn
from core.settings import settings
from fastapi.middleware.cors import CORSMiddleware
from api import router



app = FastAPI()
app.include_router(router=router)
app.add_middleware(
    CORSMiddleware
)



@app.get("/")
def index():
    return {
        "message": "Welcome to service"
    }



if __name__ == "__main__":
    uvicorn.run(app="main:app", port=int(settings.run.port),  reload=settings.run.reload)