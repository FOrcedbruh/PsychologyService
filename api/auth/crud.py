from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Invite, User
from .schemas import UserCreateSchema, TokenResponseInfo, UserReadSchema, UserUpdateSchema
from sqlalchemy import select
from fastapi import HTTPException, status, Depends
from . import utils



async def registration(session: AsyncSession, user_in: UserCreateSchema, invite_value: str) -> TokenResponseInfo:
    inviteStmt = await session.execute(select(Invite).filter(Invite.value == invite_value))
    invite = inviteStmt.scalars().first()

    if user_in.is_waiting == False:
        if not invite:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Инвайт код неактивен или некорректен"
            )
            
        if invite.limit == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Инвайт уже был использован"
            )

    stmt = await session.execute(select(User).filter(User.email == user_in.email))
    candidate = stmt.scalars().first()

    if candidate:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Такой пользователь уже существует"
        )
    
    if user_in.is_waiting == False:
        invite.limit -= 1
        if invite.limit == 0:
            invite.is_activate = False
        
    user_in_dict = user_in.model_dump()
    user_in_dict["password"] = utils.encrypt_password(password=user_in.password)
    if user_in.is_waiting == False:
        user_in_dict["invite_id"] = invite.id
    user_in_dict["invite_id"] = None

    user = User(**user_in_dict)
    session.add(user)
    await session.commit()

    access_token: str = utils.create_access_token(user=user)
    refresh_token: str = utils.create_refresh_token(user=user)

    return TokenResponseInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


async def login(session: AsyncSession, user_in: UserCreateSchema) -> TokenResponseInfo:
    stmt = await session.execute(select(User).filter(User.email == user_in.email))
    user = stmt.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Такого пользователя не существует"
        )
    
    valid_password: bool = utils.validate_password(password=user_in.password, hashed=user.password)

    if valid_password == False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Неверные пароль и/или почта"
        )
    
    access_token: str = utils.create_access_token(user=user)
    refresh_token: str = utils.create_refresh_token(user=user)

    return TokenResponseInfo(
        access_token=access_token,
        refresh_token=refresh_token
    )

def me(
    data: UserReadSchema
) -> UserReadSchema:
    return data


async def update_user(session: AsyncSession, user_for_update: UserUpdateSchema, authUser: UserReadSchema) -> dict:
    stmt = await session.execute(select(User).filter(User.login == authUser.login))
    user = stmt.scalars().first()

    for name, value in user_for_update.model_dump(exclude_none=True).items():
        setattr(user, name, value)

    await session.commit()

    return {
        "message": "success",
        "status": status.HTTP_200_OK
    }