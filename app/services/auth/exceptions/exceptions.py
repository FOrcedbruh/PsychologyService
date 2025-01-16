

UN_AUTH_EXCEPTION_DETAIL: str = "Вы не авторизованы"
UN_AUTH_EXCEPTION_STATUS: int = 401

class AuthBaseException(Exception):
    def __init__(self, status: int, detail: str):
        self.status = status
        self.detail = detail

class UnAuthException(AuthBaseException):
    def __init__(self, status: int, detail: str):
        super().__init__(status=status, detail=detail)

TOKEN_TYPE_EXCEPTION_STATUS: int = 400

class TokenTypeException(AuthBaseException):
    def __init__(self, status: int, expected_token_type: str):
        super().__init__(status=status, detail=f"Ожидается тип токена {expected_token_type}")
        self.status = status

AUTH_VERIFICATION_EXCEPTION_STATUS: int = 401
AUTH_VERIFICATION_EXCEPTION_DETAIL: str = "Авторизация с подписью, которая не является подлинной"

class AuthVerificationException(AuthBaseException):
    def __init__(self, status: int, detail: str):
        super().__init__(status=status, detail=detail)