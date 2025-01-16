from ...auth.helpers.utils import get_current_auth_user_by_token, get_current_auth_user_tg_id_by_payload
from repositories import AuthRepository


async def user_is_auth(token: str, repository: AuthRepository) -> bool:
    payload: dict = get_current_auth_user_by_token(token=token)
    tg_user_id: str = get_current_auth_user_tg_id_by_payload(payload=payload)

    await repository.get_one_by_telegram_user_id(id=int(tg_user_id))

