from ...base.base_exception.exceptions import BaseException


USER_NOT_FOUND_EXCEPTION_STATUS: int = 400
USER_NOT_FOUND_EXCEPTION_DETAIL: str = "Пользователи не найдены"

class UserNotFoundException(BaseException):

    def __init__(self, status: int, detail: str):
        super().__init__(status=status, detail=detail)