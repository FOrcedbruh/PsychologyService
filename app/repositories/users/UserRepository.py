from sqlalchemy.ext.asyncio import AsyncSession
from ..base.BaseRepository import BaseRepository
from models import User
from .exceptions.exceptions import UserNotFoundException, USER_NOT_FOUND_EXCEPTION_STATUS, USER_NOT_FOUND_EXCEPTION_DETAIL


class UserRepository(BaseRepository[User]):
    table = User
    exception: UserNotFoundException = UserNotFoundException(
        status=USER_NOT_FOUND_EXCEPTION_STATUS,
        detail=USER_NOT_FOUND_EXCEPTION_DETAIL
    )

    def __init__(self, session: AsyncSession):
        super().__init__(table=self.table, session=session, exception=self.exception)

    async def update(self, id: int, data: dict) -> User:
        res = await self.session.get(self.table, id)
        if not res:
            raise self.exception
    
        for name, val in data.items():
            setattr(res, name, val)
        
        await self.session.commit()
        await self.session.refresh(res)

        return res