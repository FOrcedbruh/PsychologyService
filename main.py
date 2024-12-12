from fastapi import FastAPI
import uvicorn
from core.settings import settings
from fastapi.middleware.cors import CORSMiddleware
from api import router


app = FastAPI()
app.include_router(router=router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "PATCH", "GET", "DELETE"],
    allow_headers=["*"],
    allow_credentials=True
)



@app.get("/")
def index():
    return {
        "message": "Welcome to service"
    }



if __name__ == "__main__":
    uvicorn.run(app="main:app", port=int(settings.run.port), host=settings.run.host, reload=bool(settings.run.reload))