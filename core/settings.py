from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL: str = os.environ.get("DB_URL")
JWT_SECRET: str = os.environ.get("JWT_KEY")

class JwtConfig(BaseModel):
    secret: str = JWT_SECRET
    algorithm: str = "HS256"

class RunCfg(BaseModel):
    port: int =  8080
    reload: bool = True

class DBCfg(BaseModel):
    url: str = DB_URL
    echo: bool = True
    pool_size: int = 10



class Settings(BaseSettings):
    run: RunCfg = RunCfg()
    db: DBCfg = DBCfg()
    jwt: JwtConfig = JwtConfig()



settings = Settings()