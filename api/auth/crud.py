from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Invite, User
from .schemas import UserCreateSchema
from sqlalchemy import select
from fastapi import HTTPException, status
from . import utils



async def registration(session: AsyncSession, user_in: UserCreateSchema, invite_value: str):
    inviteStmt = await session.execute(select(Invite).filter(Invite.value == invite_value))
    invite = inviteStmt.scalars().first()

    if not invite:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Инвайт код неактивен или некорректен"
        )

    stmt = await session.execute(select(User).filter(User.email == user_in.email))
    candidate = stmt.scalars().first()

    if candidate:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Такой пользователь уже существует"
        )
    
    invite.limit -= 1
    
    user_in_dict = user_in.model_dump()
    user_in_dict["password"] = utils.encrypt_password(password=user_in.password)
    user_in_dict["invite_id"] = invite.id
    user = User(**user_in_dict)
    session.add(user)

    await session.commit()

    return "success"


