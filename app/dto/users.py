from pydantic import BaseModel, EmailStr
from datetime import datetime



class UserLoginSchema(BaseModel):
    telegram_user_id: int
    firstname: str
    lastname: str

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

