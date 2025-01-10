from repositories import AuthRepository
from dto.users import UserLoginSchema, UserReadSchema
from models import User
from .helpers.utils import create_access_token, create_refresh_token, get_current_auth_user_by_token, get_current_auth_user_tg_id_by_payload, get_current_auth_user_for_refresh
from dto.jwt_token import TokenInfo


class AuthService:

    def __init__(self, repository: AuthRepository):
        self.repository = repository

    async def login(self, user_in: UserLoginSchema):
        user = await self.repository.get_one_by_telegram_user_id(id=user_in.telegram_user_id)

        user_for_token = user
        if not user:
            user_for_create = User(**user_in.model_dump())
            user_for_token = await self.repository.create(data=user_for_create)
            
        access_token: str = create_access_token(user=user_for_token)
        refresh_token: str = create_refresh_token(user=user_for_token)

        return TokenInfo(
            access_token=access_token,
            refresh_token=refresh_token
        )
    
    async def me(self, token: str) -> UserReadSchema:
        payload: dict = get_current_auth_user_by_token(token=token)
        telegram_user_id: str = get_current_auth_user_tg_id_by_payload(payload=payload)

        return await self.repository.get_one_by_telegram_user_id(id=int(telegram_user_id))


    async def refresh(self, token: str) -> TokenInfo:
        payload = get_current_auth_user_by_token(token=token)
        telegram_user_id: str = get_current_auth_user_for_refresh(payload=payload)

        user_for_token = await self.repository.get_one_by_telegram_user_id(id=int(telegram_user_id))

        access_token: str = create_access_token(user=user_for_token)

        return TokenInfo(
            access_token=access_token
        )