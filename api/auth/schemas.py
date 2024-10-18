from pydantic import BaseModel, EmailStr, Field



class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6),
    login: str = Field(min_length=3)
    bio: str = Field(max_length=400)
    status: str | None
    invite_id: int | None


class UserSchema(UserCreateSchema):
    id: int