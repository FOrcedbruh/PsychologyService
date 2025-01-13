from config import settings
from dto.users import UserLoginSchema, UserAuthTelegramData
from jwt.exceptions import InvalidTokenError
from ..exceptions.exceptions import UnAuthException, UN_AUTH_EXCEPTION_STATUS, TokenTypeException, TOKEN_TYPE_EXCEPTION_STATUS
from .token_helpers import jwt_decode, jwt_encode

ACCESS_TOKEN_TYPE: str = "access"
REFRESH_TOKEN_TYPE: str = "refresh"

def create_access_token(
    user: UserLoginSchema, 
    expires_minutes: int = settings.jwt.access_expires_minutes
) -> str:
    payload: dict = {
        "sub": str(user.telegram_user_id),
        "first_name": user.first_name,
        "last_name": user.last_name,
        "type": ACCESS_TOKEN_TYPE,
        "id": user.id
    }

    return jwt_encode(payload=payload, expires_minutes=expires_minutes)

def create_refresh_token(
    user: UserLoginSchema,
    expires_minutes: int = settings.jwt.refresh_expires_minutes
) -> str:
    payload: dict = {
        "sub": str(user.telegram_user_id),
        "type": REFRESH_TOKEN_TYPE
    }
    return jwt_encode(payload=payload, expires_minutes=expires_minutes)

def get_current_auth_user_by_token(
    token: str
) -> dict:
    try:
        payload: dict = jwt_decode(token=token)
    except InvalidTokenError as exc:
        raise UnAuthException(
            status=UN_AUTH_EXCEPTION_STATUS,
            detail=f"Некорректный токен: {exc}"
        )
    return payload

def get_current_auth_user_tg_id_by_payload(
    payload: dict
) -> str:
    telegram_user_id: str = payload.get("sub")
    if payload["type"] != ACCESS_TOKEN_TYPE:
        raise TokenTypeException(
            status=TOKEN_TYPE_EXCEPTION_STATUS,
            expected_token_type=ACCESS_TOKEN_TYPE
        )
    return telegram_user_id


def get_current_auth_user_for_refresh(
    payload: dict
) -> dict:
    telegram_user_id: str = payload.get("sub")
    if payload["type"] != REFRESH_TOKEN_TYPE:
        raise TokenTypeException(
            status=TOKEN_TYPE_EXCEPTION_STATUS,
            expected_token_type=REFRESH_TOKEN_TYPE
        )
    return telegram_user_id


def tg_user_to_user(tg_user: UserAuthTelegramData) -> UserLoginSchema:
    return UserLoginSchema(
        telegram_user_id=tg_user.id,
        first_name=tg_user.first_name,
        last_name=tg_user.last_name,
        profile_image=tg_user.photo_url
    )