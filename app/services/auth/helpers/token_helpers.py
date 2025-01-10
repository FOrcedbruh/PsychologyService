from config import settings
from datetime import datetime, UTC, timedelta
import bcrypt
import jwt





def jwt_encode(
    expires_minutes: int,
    payload: dict,
    sercet: str = settings.jwt.secret,
    algorithm: str = settings.jwt.algorithm,
) -> str:
    payload["exp"] = datetime.now(UTC) + timedelta(minutes=expires_minutes)
    payload["iat"] = datetime.now(UTC)
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



    