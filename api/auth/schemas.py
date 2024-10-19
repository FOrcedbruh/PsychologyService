from pydantic import BaseModel, EmailStr, Field



class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str | bytes = Field(min_length=6),
    login: str = Field(min_length=3)
    invite_id: int


class UserSchema(UserCreateSchema):
    id: int

class UserLoginSchema(BaseModel):
    email: str
    password: str = Field(min_length=6)

class UserReadSchema(UserSchema):
    bio: str = Field(max_length=400)
    status: str = Field(max_length=60)



class TokenResponseInfo(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str =  "Bearer"
