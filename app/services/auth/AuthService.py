from repositories import AuthRepository
from dto.users import UserLoginSchema, UserReadSchema, UserAuthTelegramData
from models import User
from .helpers.utils import create_access_token, create_refresh_token, get_current_auth_user_by_token, get_current_auth_user_tg_id_by_payload, get_current_auth_user_for_refresh, tg_user_to_user
from .helpers.tg_hash_verification import verification_hash
from dto.jwt_token import TokenInfo
from config import settings


class AuthService:

    def __init__(self, repository: AuthRepository):
        self.repository = repository

    async def login(self, user_in: UserAuthTelegramData):
        tg_auth_user: UserAuthTelegramData = verification_hash(data=user_in, bot_token=settings.telegram.bot_token)
        user = await self.repository.get_one_by_telegram_user_id(id=tg_auth_user.id)

        user_for_token = user
        if not user:
            login_user: UserLoginSchema = tg_user_to_user(tg_user=tg_auth_user)
            user_for_create = User(**login_user.model_dump())

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
    
    async def check_hash(self, auth_data: UserAuthTelegramData) -> UserAuthTelegramData:
        return verification_hash(data=auth_data, bot_token=settings.telegram.bot_token)