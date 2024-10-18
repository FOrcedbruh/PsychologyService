from fastapi import APIRouter
from fastapi import Depends
from . import utils, crud
from sqlalchemy.ext.asyncio import AsyncSession
from core.db_connection import db_connection
from .schemas import UserCreateSchema

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/registration")
def registration(
    session: AsyncSession = Depends(db_connection.session_creation),
    user_in: UserCreateSchema = Depends(utils.RegForm), 
    invite_value: str = Depends(utils.InviteForm)
):
    return crud.registration(session=session, user_in=user_in, invite_value=invite_value)