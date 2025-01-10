from ...base.base_exception.exceptions import BaseException



NOT_FOUND_INVITE_EXCEPTION_DETAIL: str = "Инвайты не найдены"
NOT_FOUND_INVITE_EXCEPTION_STATUS: int = 400

class NotFoundInviteException(BaseException):
    def __init__(self, status: int, detail: str):
        super().__init__(status=status, detail=detail)