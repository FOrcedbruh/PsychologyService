from pydantic import BaseModel, Field
from datetime import datetime 

class PostCreateSchema(BaseModel):
    title: str
    type: str
    receiver: str
    user_id: int | None = None
    body: str


class PostReadSchema(PostCreateSchema):
    id: int
    created_at: datetime


class PostUpdateSchema(BaseModel):
    title: str | None = None
    type: str | None = None
    body: str | None = None
    id: int | None = None
    

