from ...base.base_exception.exceptions import BaseException


USERS_NOT_FOUND_EXCEPTION_DETAIL: str = "Пользователи не найдены"
USERS_NOT_FOUND_EXCEPTION_STATUS: int = 400


class UsersNotFoundException(BaseException):
    def __init__(self, detail: str, status: int):
        super().__init__(detail=detail, status=status)