from ..base.BaseRepository import BaseRepository
from models import User
from .exceptions.exceptions import UsersNotFoundException, USERS_NOT_FOUND_EXCEPTION_DETAIL, USERS_NOT_FOUND_EXCEPTION_STATUS
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class AuthRepository(BaseRepository[User]):
    table = User
    exception: UsersNotFoundException = UsersNotFoundException(
        detail=USERS_NOT_FOUND_EXCEPTION_DETAIL,
        status=USERS_NOT_FOUND_EXCEPTION_STATUS
    )

    def __init__(self, session: AsyncSession):
        super().__init__(table=self.table, session=session, exception=self.exception)

    async def get_one_by_telegram_user_id(self, id: int) -> User:
        query = select(self.table).where(self.table.telegram_user_id == id)
        stmt =  await self.session.execute(query)
        res = stmt.scalar()

        return res