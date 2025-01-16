from repositories import AuthRepository, PostRepository
from dto.posts import PostReadSchema, PostCreateSchema, PostUpdateSchema
from .helpers.auth_helper import user_is_auth
from models import Post

class PostService:

    def __init__(self, repository: PostRepository, auth_repository: AuthRepository):
        self.repository = repository
        self.auth_repository = auth_repository


    async def get_post(self, post_id: int, token: str):
        await user_is_auth(repository=self.auth_repository, token=token)
        return await self.repository.get_one(id=post_id)
        
    
    async def create_post(self, post_in: PostCreateSchema, token: str) -> PostReadSchema:
        await user_is_auth(repository=self.auth_repository, token=token)
        post_to_create = Post(**post_in.model_dump())

        return await self.repository.create(data=post_to_create)