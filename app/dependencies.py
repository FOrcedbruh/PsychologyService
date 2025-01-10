from fastapi import Depends
from config import DatabaseConnection, settings
from sqlalchemy.ext.asyncio import AsyncSession
from repositories import InviteRepository, AuthRepository
from services import InviteService, AuthService

def get_db_connection() -> DatabaseConnection:
    return DatabaseConnection(
        db_url=settings.db.url,
        db_echo=settings.db.echo,
        db_pool_size=settings.db.pool_size
    )


#repositories depends
def get_invite_repository(
    session: AsyncSession = Depends(get_db_connection().create_async_session)
) -> InviteRepository:
    return InviteRepository(session=session)

def get_auth_repository(
    session: AsyncSession = Depends(get_db_connection().create_async_session)
) -> AuthRepository:
    return AuthRepository(session=session)

#services depends
def get_invite_services(
    repository: InviteRepository = Depends(get_invite_repository)
) -> InviteService:
    return InviteService(repository=repository)

def get_auth_service(
    repository: AuthRepository = Depends(get_auth_repository)
) -> AuthService:
    return AuthService(repository=repository)

