from pydantic import BaseModel, EmailStr
from datetime import datetime



class UserLoginSchema(BaseModel):
    telegram_user_id: int
    first_name: str
    last_name: str | None = None
    profile_image: str | None = None

class UserReadSchema(UserLoginSchema):
    id: int
    created_at: datetime
    email: EmailStr | None
    tel: str | None
    hobbies: list[str] | None
    profile_image: str | None

class UserUpdateSchema(BaseModel):
    email: EmailStr | None = None
    tel: str | None = None
    hobbies: list[str] | None = None

class UserAuthTelegramData(BaseModel):
    id: int
    username: str
    hash: str
    first_name: str | None = None
    last_name: str | None = None
    photo_url: str
    auth_date: int

