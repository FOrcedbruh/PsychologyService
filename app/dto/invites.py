from pydantic import BaseModel, Field

class InviteSchemaCreatePartial(BaseModel):
    type: str = "disposable"
    limit: int = 1
    is_activate: bool = True


class InviteSchemaCreate(InviteSchemaCreatePartial):
    value: str = Field(max_length=9)
    

class InviteReadSchema(InviteSchemaCreate):
    id: int

