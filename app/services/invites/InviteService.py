from repositories import InviteRepository
from dto.invites import InviteReadSchema, InviteSchemaCreatePartial
from models import Invite
from .helpers.utils import generate_invite_code

class InviteService:
    
    def __init__(self, repository: InviteRepository):
        self.repository = repository


    async def generate_invite(self, invite_in: InviteSchemaCreatePartial) -> InviteReadSchema:
        invite_in_dict = invite_in.model_dump()
        invite_in_dict["value"] = generate_invite_code()
        invite_to_create = Invite(**invite_in_dict)
        return await self.repository.create(data=invite_to_create)
    
    async def delete_invite(self, invite_id: int) -> dict:
        await self.repository.delete(id=invite_id)

        return {
            "messsage": "Инвайт успешно удален"
        }
    
    async def get_invites(self) -> list[InviteReadSchema]:
        return await self.repository.list()

    