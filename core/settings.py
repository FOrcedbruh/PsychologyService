from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL: str = os.environ.get("DB_URL")
JWT_SECRET: str = os.environ.get("JWT_KEY")
PORT: str = os.environ.get("PORT")
HOST: str = os.environ.get("HOST")
RELOAD: str = os.environ.get("RELOAD")


class JwtConfig(BaseModel):
    secret: str = JWT_SECRET
    algorithm: str = "HS256"
    access_expires_minutes: int = 15
    refresh_expires_minutes: int = 60 * 24 * 30

class RunCfg(BaseModel):
    port: int = PORT
    reload: bool = RELOAD
    host: str = HOST

class DBCfg(BaseModel):
    url: str = DB_URL
    echo: bool = True
    pool_size: int = 10



class Settings(BaseSettings):
    run: RunCfg = RunCfg()
    db: DBCfg = DBCfg()
    jwt: JwtConfig = JwtConfig()



settings = Settings()