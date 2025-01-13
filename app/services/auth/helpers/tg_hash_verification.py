from dto.users import UserAuthTelegramData
import hashlib
import hmac
from ..exceptions.exceptions import AuthVerificationException, AUTH_VERIFICATION_EXCEPTION_DETAIL, AUTH_VERIFICATION_EXCEPTION_STATUS


def verification_hash(data: UserAuthTelegramData, bot_token: str) -> UserAuthTelegramData:
    data_dict: dict = data.model_dump(exclude_none=True)
    received_hash: str = data_dict.pop("hash")

    data_verify_str: str = "\n".join(sorted(f"{key}={value}" for key, value in data_dict.items() if value is not None))

    secret_key: bytes = hashlib.sha256(bot_token.encode()).digest()

    hmac_: str = hmac.new(secret_key, data_verify_str.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(hmac_, received_hash):
        raise AuthVerificationException(
            status=AUTH_VERIFICATION_EXCEPTION_STATUS,
            detail=AUTH_VERIFICATION_EXCEPTION_DETAIL
        )

    return data