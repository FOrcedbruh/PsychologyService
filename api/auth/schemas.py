from pydantic import BaseModel, EmailStr, Field



class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str | bytes = Field(min_length=6),
    login: str = Field(min_length=3)
    invite_id: int


class UserSchema(UserCreateSchema):
    id: int