from ..base.BaseRepository import BaseRepository
from models import Invite
from .exceptions.exceptions import NotFoundInviteException, NOT_FOUND_INVITE_EXCEPTION_DETAIL, NOT_FOUND_INVITE_EXCEPTION_STATUS
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select



class InviteRepository(BaseRepository[Invite]):
    table = Invite
    exception: NotFoundInviteException = NotFoundInviteException(
        status=NOT_FOUND_INVITE_EXCEPTION_STATUS,
        detail=NOT_FOUND_INVITE_EXCEPTION_DETAIL
    )


    def __init__(self, session: AsyncSession):
        super().__init__(table=self.table, session=session, exception=self.exception)

    async def get_one_by_value(self, value: str) -> Invite:
        query = select(self.table).where(self.table.value == value)
        stmt = await self.session.execute(query)
        res = stmt.scalar()

        return res
    
    