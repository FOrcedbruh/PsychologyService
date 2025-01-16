from ...base.base_exception.exceptions import BaseException


NOT_FOUND_POST_EXCEPTION_STATUS: int = 400
NOT_FOUND_POST_EXCEPTION_DETAIL: str = "Посты не найдены"

class NotFoundPostException(BaseException):
    def __init__(self, status: int, detail: str):
        super().__init__(status=status, detail=detail)