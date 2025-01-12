from fastapi import APIRouter, Body, Depends, File, UploadFile
from dto.users import UserUpdateSchema, UserReadSchema
from dependencies import get_user_service
from services import UserService
from repositories import S3Repository
from dependencies import get_s3_repository_for_images_bucket

router = APIRouter(prefix="/users", tags=["Users"])


@router.patch("/{user_id}", response_model=UserReadSchema)
async def index(
    user_id: int,
    user_in: UserUpdateSchema = Body(),
    service: UserService = Depends(get_user_service)
) -> UserReadSchema:
    return await service.update_user(user_id=user_id, user_in=user_in)

@router.delete("/{user_id}", response_model=dict)
async def index(
    user_id: int,
    service: UserService = Depends(get_user_service)
) -> dict:
    return await service.delete_user(user_id=user_id)

@router.patch("/profile-image/{user_id}", response_model=UserReadSchema)
async def index(
    user_id: int,
    object: UploadFile = File(),
    service: UserService = Depends(get_user_service),
    s3_repository: S3Repository = Depends(get_s3_repository_for_images_bucket)
) -> UserReadSchema:
    return await service.change_profile_image(user_id=user_id, object=object, s3_repository=s3_repository)