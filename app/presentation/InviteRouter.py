from fastapi import APIRouter, Depends, Body
from dependencies import get_invite_services
from services import InviteService
from dto.invites import InviteReadSchema, InviteSchemaCreatePartial

router = APIRouter(prefix="/invites", tags=["Invites"])



@router.post("/", response_model=InviteReadSchema)
async def index(
    invite_in: InviteSchemaCreatePartial = Body(),
    service: InviteService = Depends(get_invite_services)
) -> InviteReadSchema:
    return await service.generate_invite(invite_in=invite_in)


@router.get("/", response_model=list[InviteReadSchema])
async def index(
    service: InviteService = Depends(get_invite_services)
) -> list[InviteReadSchema]:
    return await service.get_invites()


@router.delete("/", response_model=dict)
async def index(
    invite_id: int,
    service: InviteService = Depends(get_invite_services)
) -> dict:
    return await service.delete_invite(invite_id=invite_id)