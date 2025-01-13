from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL: str = os.environ.get("DB_URL")
#=======
JWT_SECRET: str = os.environ.get("JWT_KEY")
#=======
PORT: str = os.environ.get("PORT")
HOST: str = os.environ.get("HOST")
RELOAD: str = os.environ.get("RELOAD")
#=======
MAIL_SENDER_URL: str = os.environ.get("MAIL_SENDER_URL")
#=======
S3_GET_URL: str = os.environ.get("S3_GET_URL")
S3_URL: str = os.environ.get("S3_URL")
S3_SECRET_KEY: str = os.environ.get("S3_SECRET_KEY")
S3_ACCESS_KEY: str = os.environ.get("S3_ACCESS_KEY")
S3_BUCKET_NAME_IMAGES: str = os.environ.get("S3_BUCKET_NAME_IMAGES")
#=======
AUTH_BOT_TOKEN: str = os.environ.get("AUTH_BOT_TOKEN")

class TelegramCfg(BaseModel):
    bot_token: str = AUTH_BOT_TOKEN

class S3Cfg(BaseModel):
    url: str = S3_URL
    get_url: str = S3_GET_URL
    images_bucket_name: str = S3_BUCKET_NAME_IMAGES
    secret_key: str = S3_SECRET_KEY
    access_key: str = S3_ACCESS_KEY

class JwtCfg(BaseModel):
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


class MailServiceCfg(BaseModel):
    base_url: str = MAIL_SENDER_URL


class Settings(BaseSettings):
    run: RunCfg = RunCfg()
    db: DBCfg = DBCfg()
    jwt: JwtCfg = JwtCfg()
    mail_sender: MailServiceCfg = MailServiceCfg()
    s3: S3Cfg = S3Cfg()
    telegram: TelegramCfg = TelegramCfg()



settings = Settings()