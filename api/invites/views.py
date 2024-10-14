from fastapi import APIRouter, Depends
from .schemas import InviteSchemaCreate, InviteSchemaCreatePartial
from . import crud
from . import utils


router = APIRouter(prefix="/invite", tags=["Invite"])


@router.post("/generate")
async def create_disposable_invite(invite_in: InviteSchemaCreatePartial = Depends(utils.invite_form)) -> InviteSchemaCreate:
    return await crud.create_invite(invite_in=invite_in)