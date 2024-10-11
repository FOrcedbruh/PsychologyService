from pydantic_settings import BaseSettings
from pydantic import BaseModel

class RunCfg():
    port: int =  8080
    reload: bool = True


class Settings(BaseSettings):
    run: RunCfg = RunCfg()

settings = Settings()