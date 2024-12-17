import jwt
from core.settings import settings
import datetime
import bcrypt
from fastapi import Body, Depends, HTTPException, status
from .schemas import UserCreateSchema, UserSchema, UserLoginSchema, UserReadSchema
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from jwt import InvalidTokenError
from core.db_connection import db_connection
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import User
import requests



http_bearer = HTTPBearer(auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login/")

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


ACCESS_TOKEN_TYPE: str = "access"
REFRESH_TOKEN_TYPE: str = "refresh"

def create_access_token(
    user: UserSchema, 
    expires_minutes: int = settings.jwt.access_expires_minutes
) -> str:
    payload: dict = {
        "sub": user.login,
        "email": user.email,
        "type": ACCESS_TOKEN_TYPE,
        "id": user.id
    }

    return jwt_encode(payload=payload, expires_minutes=expires_minutes)

def create_refresh_token(
    user: UserSchema,
    expires_minutes: int = settings.jwt.refresh_expires_minutes
) -> str:
    payload: dict = {
        "sub": user.login,
        "type": REFRESH_TOKEN_TYPE
    }
    return jwt_encode(payload=payload, expires_minutes=expires_minutes)


def get_current_token(
    token: str = Depends(oauth2_scheme)
) -> dict:
    try:
        payload: dict = jwt_decode(token=token)
    except InvalidTokenError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token error: {error}"
        )
    return payload

async def get_current_authuser(
    payload: dict = Depends(get_current_token),
    session: AsyncSession = Depends(db_connection.session_creation)
) -> UserReadSchema:
    login: str = payload.get("sub")
    if payload["type"] != ACCESS_TOKEN_TYPE:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Ожидается тип токена {ACCESS_TOKEN_TYPE}"
        )
    stmt = await session.execute(select(User).filter(User.login == login))
    user = stmt.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Некорректный токен"
        )
    
    return UserReadSchema(
        login=user.login,
        email=user.email,
        bio=user.bio,
        status=user.status,
        id=user.id,
        is_waiting=user.is_waiting,
        invite_id=user.invite_id,
    )

async def get_confirmation_code(email: str, name: str, base_url: str = settings.mail_sender.base_url) -> requests.Response:
    res: requests.Response = requests.post(url=f"{base_url}sendemail", json={
        "email": email,
        "name": name
        }
    )

    if res.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ошибка на сервере mail sender: {res.status_code} error"
        )

    return res