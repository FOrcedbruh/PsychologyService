from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from core.settings import settings
from typing import AsyncGenerator, Annotated



class DB_Connection():
    def __init__(self, db_url: str, db_echo: bool, db_pool_size: int):
        self.engine = create_async_engine(
            url=db_url,
            echo=db_echo,
            pool_size=db_pool_size,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
    async def session_creation(self) -> Annotated[AsyncGenerator, AsyncSession]:
        async with self.session_creation() as session:
            yield session


db_connection = DB_Connection(db_echo=settings.db.echo, db_url=settings.db.url, db_pool_size=settings.db.pool_size)