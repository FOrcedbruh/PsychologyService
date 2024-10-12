from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL: str = os.environ.get("DB_URL")


class RunCfg(BaseModel):
    port: int =  8080
    reload: bool = True

class DBCfg(BaseModel):
    url: str = DB_URL
    echo: bool = True



class Settings(BaseSettings):
    run: RunCfg = RunCfg()
    db: DBCfg = DBCfg()



settings = Settings()