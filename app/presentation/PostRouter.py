from fastapi import APIRouter, Depends, Body
from fastapi.security import OAuth2PasswordBearer
from dto.posts import PostReadSchema, PostCreateSchema
from services import PostService
from dependencies import get_post_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/posts")

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/{post_id}", response_model=PostReadSchema)
async def index(
    post_id: int,
    token: str = Depends(oauth2_scheme),
    service: PostService = Depends(get_post_service)
) -> PostReadSchema:
    return await service.get_post(post_id=post_id, token=token)


@router.post("/", response_model=PostReadSchema)
async def index(
    post_in: PostCreateSchema = Body(),
    token: str = Depends(oauth2_scheme),
    service: PostService = Depends(get_post_service)
) -> PostReadSchema:
    return await service.create_post(post_in=post_in, token=token)
    