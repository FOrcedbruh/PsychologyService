from pydantic import BaseModel, EmailStr
from datetime import datetime



class UserLoginSchema(BaseModel):
    telegram_user_id: int
    fisrtname: str
    lastname: str

class UserReadSchema(UserLoginSchema):
    id: int
    created_at: datetime
    email: EmailStr | None
    tel: str | None
    hobbies: list[str] | None

