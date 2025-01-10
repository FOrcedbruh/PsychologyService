from fastapi import FastAPI, HTTPException
import uvicorn
from config import settings
from fastapi.middleware.cors import CORSMiddleware
from repositories.base.base_exception.exceptions import BaseException
from presentation import router
from services.auth.exceptions.exceptions import AuthBaseException


app = FastAPI(
    title="*****.online API"
)
app.include_router(router=router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=[
        "POST",
        "PATCH", 
        "GET",
        "DELETE"
    ],
    allow_headers=["*"],
    allow_credentials=True
)



@app.exception_handler(BaseException)
def exception_handler(req, exc: BaseException):
    raise HTTPException(
        status_code=exc.status,
        detail=exc.detail
    )
@app.exception_handler(AuthBaseException)
def exception_handler(req, exc: AuthBaseException):
    raise HTTPException(
        status_code=exc.status,
        detail=exc.detail
    )




@app.get("/")
def index():
    return {
        "message": "Welcome to service"
    }



if __name__ == "__main__":
    uvicorn.run(app="main:app", port=int(settings.run.port), host=settings.run.host, reload=bool(settings.run.reload))