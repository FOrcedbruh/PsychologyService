from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing import AsyncGenerator



class DatabaseConnection():
    def __init__(self, db_url: str, db_echo: bool, db_pool_size: int):
        self.engine = create_async_engine(
            url=db_url,
            echo=db_echo,
            pool_size=db_pool_size,
        )
        self.session_factory: AsyncGenerator[AsyncSession, None] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
    async def create_async_session(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
