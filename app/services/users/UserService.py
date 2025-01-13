from dto.users import UserReadSchema, UserUpdateSchema
from repositories import UserRepository, S3Repository


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository


    async def update_user(self, user_id: int, user_in: UserUpdateSchema) -> UserReadSchema:
        user_to_update: dict = user_in.model_dump(exclude_none=True)
        return await self.repository.update(id=user_id, data=user_to_update)
    

    async def delete_user(self, user_id: int) -> dict:
        await self.repository.delete(id=user_id)

        return {
            "message": "Пользователь успешно удален"
        }
    
    async def change_profile_image(self, user_id: int, object, s3_repository: S3Repository, key: str | None = None, ) -> UserReadSchema:
        url: str = await s3_repository.upload_object(file=object)
        if key is not None:
            await s3_repository.delete_object(filename=key)
        return await self.repository.change_profile_image(id=user_id, data=url)