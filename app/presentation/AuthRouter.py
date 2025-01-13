from fastapi import APIRouter
from dependencies import get_auth_service
from services import AuthService
from fastapi import Depends, Body
from dto.users import UserLoginSchema, UserReadSchema, UserAuthTelegramData
from dto.jwt_token import TokenInfo
from fastapi.security import HTTPBearer, OAuth2PasswordBearer


http_bearer = HTTPBearer(auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
router = APIRouter(prefix="/auth", tags=["Auth"], dependencies=[Depends(http_bearer)])



@router.post("/login", response_model=TokenInfo)
async def index(
    user_in: UserAuthTelegramData  = Body(),
    service: AuthService = Depends(get_auth_service)
) -> TokenInfo:
    return await service.login(user_in=user_in)


@router.get("/me", response_model=UserReadSchema)
async def index(
    token: str = Depends(oauth2_scheme),
    service: AuthService = Depends(get_auth_service)
) -> UserReadSchema:
    return await service.me(token=token)


@router.get("/refresh")
async def index(
    token: str = Depends(oauth2_scheme),
    service: AuthService = Depends(get_auth_service)
) -> TokenInfo:
    return await service.refresh(token=token)

@router.post("/check_hash")
async def index(
    auth_data: UserAuthTelegramData = Body(),
    service: AuthService = Depends(get_auth_service)
):
    return await service.check_hash(auth_data=auth_data)