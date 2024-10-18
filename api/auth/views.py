from fastapi import APIRouter
from fastapi import Depends, Body
from . import utils, crud
from sqlalchemy.ext.asyncio import AsyncSession
from core.db_connection import db_connection
from .schemas import UserCreateSchema

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/registration")
async def registration(
    session: AsyncSession = Depends(db_connection.session_creation),
    user_in: UserCreateSchema = Depends(utils.RegForm), 
    invite_value: str = Body()
):
    return await crud.registration(session=session, user_in=user_in, invite_value=invite_value)