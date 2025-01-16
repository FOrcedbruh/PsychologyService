from fastapi import Depends
from config import DatabaseConnection, settings
from sqlalchemy.ext.asyncio import AsyncSession
from repositories import InviteRepository, AuthRepository, UserRepository, S3Repository, PostRepository
from services import InviteService, AuthService, UserService, PostService

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

def get_user_repository(
    session: AsyncSession = Depends(get_db_connection().create_async_session)
) -> UserRepository:
    return UserRepository(session=session)


def get_post_repository(
    session: AsyncSession = Depends(get_db_connection().create_async_session)
) -> PostRepository:
    return PostRepository(session=session)

def get_s3_repository_for_images_bucket() -> S3Repository:
    return S3Repository(
        storage_url=settings.s3.url,
        access_key=settings.s3.access_key,
        secret_key=settings.s3.secret_key,
        bucket_name=settings.s3.images_bucket_name
    )

#services depends
def get_invite_services(
    repository: InviteRepository = Depends(get_invite_repository)
) -> InviteService:
    return InviteService(repository=repository)

def get_auth_service(
    repository: AuthRepository = Depends(get_auth_repository)
) -> AuthService:
    return AuthService(repository=repository)

def get_user_service(
    repository: UserRepository = Depends(get_user_repository)
) -> UserService:
    return UserService(repository=repository)

def get_post_service(
    repository: PostRepository = Depends(get_post_repository),
    auth_repository: AuthRepository = Depends(get_auth_repository)
) -> PostService:
    return PostService(repository=repository, auth_repository=auth_repository)