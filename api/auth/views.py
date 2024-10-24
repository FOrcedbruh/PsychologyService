from fastapi import APIRouter
from fastapi import Depends, Body
from . import utils, crud
from sqlalchemy.ext.asyncio import AsyncSession
from core.db_connection import db_connection
from .schemas import UserCreateSchema, TokenResponseInfo, UserLoginSchema, UserReadSchema, UserUpdateSchema



router = APIRouter(prefix="/auth", tags=["Auth"], dependencies=[Depends(utils.http_bearer)])


@router.post("/registration", response_model=TokenResponseInfo, response_model_exclude_none=True)
async def registration(
    session: AsyncSession = Depends(db_connection.session_creation),
    user_in: UserCreateSchema = Depends(utils.RegForm),
    invite_value: str = Body()
) -> TokenResponseInfo:
    return await crud.registration(session=session, user_in=user_in, invite_value=invite_value)

@router.post("/login", response_model=TokenResponseInfo, response_model_exclude_none=True)
async def login(
    session: AsyncSession = Depends(db_connection.session_creation),
    user_in: UserLoginSchema = Depends(utils.LogForm)
) -> TokenResponseInfo:
    return await crud.login(session=session, user_in=user_in)


@router.post("/users/me", response_model=UserReadSchema, response_model_exclude_none=True)
async def get_me(data: UserReadSchema = Depends(utils.get_current_authuser)) -> UserReadSchema:
    return crud.me(data=data)

@router.patch("/user/update")
async def update_user(session: AsyncSession = Depends(db_connection.session_creation), user_for_update: UserUpdateSchema = Body(), authUser: UserUpdateSchema = Depends(utils.get_current_authuser)):
    return await crud.update_user(session=session, user_for_update=user_for_update, authUser=authUser)