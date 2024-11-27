from pydantic import BaseModel, Field




class PostCreateSchema(BaseModel):
    title: str
    type: str
    receiver: str
    user_id: int | None = None
    body: str


class PostReadSchema(PostCreateSchema):
    pass