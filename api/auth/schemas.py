from pydantic import BaseModel, EmailStr, Field



class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str | bytes = Field(min_length=6),
    login: str = Field(min_length=3)
    invite_id: int | None
    is_waiting: bool


class UserSchema(UserCreateSchema):
    id: int

class UserLoginSchema(BaseModel):
    email: str
    password: str = Field(min_length=6)

class UserReadSchema(BaseModel):
    id: int
    bio: str | None = Field(max_length=400)
    status: str | None = Field(max_length=60)
    login: str = Field(min_length=3)
    invite_id: int | None
    is_waiting: bool
    email: EmailStr



class TokenResponseInfo(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str =  "Bearer"
