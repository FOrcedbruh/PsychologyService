from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Generic
from models import Base
from .base_exception.exceptions import BaseException

TableType = TypeVar(name="TableType", bound=Base)
ExceptionType = TypeVar(name="ExceptionType", bound=BaseException)

# Базовый родительский репозиторий от которого нследуются иные, данный содержит CRUD операции с моделями

class BaseRepository(Generic[TableType]):
    def __init__(self, table: TableType, session: AsyncSession, exception: ExceptionType):
        self.table = table
        self.session = session
        self.exception = exception

    async def list(self) -> list[TableType]:
        query = select(self.table)
        stmt = await self.session.execute(query)
        res = stmt.scalars().all()

        return list(res)
    
    async def get_one(self, id: int) -> TableType:
        res = await self.session.get(self.table, id)

        if not res:
            raise self.exception
        
        return res

    async def create(self, data: TableType) -> TableType:
        self.session.add(data)
        await self.session.commit()
        await self.session.refresh(data)

        return data
    
    async def delete(self, id: int) -> None:
        res = await self.session.get(self.table, id)
        if not res:
            raise self.exception


        await self.session.delete(res)
        await self.session.commit()




    
    
    

    