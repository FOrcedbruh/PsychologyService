from sqlalchemy.ext.asyncio import AsyncSession
from ..base.BaseRepository import BaseRepository
from models import Post
from .exceptions.exceptions import NotFoundPostException, NOT_FOUND_POST_EXCEPTION_DETAIL, NOT_FOUND_POST_EXCEPTION_STATUS


class PostRepository(BaseRepository[Post]):
    table = Post
    exception: NotFoundPostException = NotFoundPostException(
        status=NOT_FOUND_POST_EXCEPTION_STATUS,
        detail=NOT_FOUND_POST_EXCEPTION_DETAIL
    )

    def __init__(self, session: AsyncSession):
        super().__init__(table=self.table, session=session, exception=self.exception)

    
