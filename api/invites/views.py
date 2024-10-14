from fastapi import APIRouter, Depends
from .schemas import InviteSchemaCreate, InviteSchemaCreatePartial
from . import crud
from . import utils
from core.db_connection import db_connection
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix="/invite", tags=["Invite"])


@router.post("/generate")
async def create_disposable_invite(invite_in: InviteSchemaCreatePartial = Depends(utils.invite_form), session: AsyncSession = Depends(db_connection.session_creation)) -> InviteSchemaCreate:
    return await crud.create_invite(invite_in=invite_in, session=session)

