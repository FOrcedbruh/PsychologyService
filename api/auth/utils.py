import jwt
from core.settings import settings
import datetime
import bcrypt
from fastapi import Body
from .schemas import UserCreateSchema, TokenResponseInfo, UserSchema, UserLoginSchema

def jwt_encode(
    expires_minutes: int,
    payload: dict,
    sercet: str = settings.jwt.secret,
    algorithm: str = settings.jwt.algorithm,
) -> str:
    payload["exp"] = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=expires_minutes)
    payload["iat"] = datetime.datetime.now(datetime.UTC)
    return jwt.encode(payload=payload, key=sercet, algorithm=algorithm)


def jwt_decode(
    token: str,
    algorithm: str = settings.jwt.algorithm,
    secret: str = settings.jwt.secret,
) -> dict:
    return jwt.decode(key=secret, algorithms=[algorithm], jwt=token)


def encrypt_password(
    password: str
) -> bytes:
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())


def validate_password(
    hashed: bytes,
    password: str
) -> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed)


def RegForm(user_in: UserCreateSchema = Body()) -> UserCreateSchema:
    return UserCreateSchema(
        login=user_in.login,
        email=user_in.email,
        password=user_in.password,
        invite_id=None,
        is_waiting=user_in.is_waiting
    )

def LogForm(user_in: UserLoginSchema = Body()) -> UserLoginSchema:
    return UserLoginSchema(
        email=user_in.email,
        password=user_in.password
    )


def create_access_token(
    user: UserSchema, 
    expires_minutes: int = settings.jwt.access_expires_minutes
) -> str:
    payload: dict = {
        "sub": user.login,
        "email": user.email,
        "id": user.id
    }

    return jwt_encode(payload=payload, expires_minutes=expires_minutes)

def create_refresh_token(
    user: UserSchema,
    expires_minutes: int = settings.jwt.refresh_expires_minutes
) -> str:
    payload: dict = {
        "sub": user.login,
    }
    return jwt_encode(payload=payload, expires_minutes=expires_minutes)
