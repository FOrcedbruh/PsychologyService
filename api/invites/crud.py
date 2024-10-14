from .schemas import InviteSchemaCreatePartial, InviteSchemaCreate
from . import utils
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Invite
from sqlalchemy import select
from fastapi import HTTPException, status


async def create_invite(invite_in: InviteSchemaCreatePartial, session: AsyncSession) -> InviteSchemaCreate:
    invite_value = utils.generate_invite_code()
    st = await session.execute(select(Invite).filter(Invite.value == invite_value))
    candidate = st.scalars().first()

    if candidate:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ошибка генерации инвайт кода"
        )
    else:
        invite_in_dict = invite_in.model_dump()
        invite_in_dict["value"] = invite_value
        invite = Invite(**invite_in_dict)
        session.add(invite)

        await session.commit()


        return InviteSchemaCreate(
            limit=invite_in.limit,
            type=invite_in.type,
            value=invite_value,
            is_activate=invite_in.is_activate
    )

