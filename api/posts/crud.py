from fastapi import status, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import PostCreateSchema, PostUpdateSchema
from core.models import Post


async def create_post(session: AsyncSession, post_in: PostCreateSchema) -> dict:
    post = Post(**post_in.model_dump())
    session.add(post)

    await session.commit()

    return {
        "status": status.HTTP_201_CREATED,
        "created_post": post
    }

async def erase_post(session: AsyncSession, post_id: int) -> dict:
    st = await session.execute(select(Post).filter(Post.id == post_id))
    post_to_erase = st.scalars().first()

    if not post_to_erase:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ошибка удаления поста"
        )

    await session.delete(post_to_erase)
    await session.commit()

    return {
        "status": status.HTTP_200_OK,
        "erased_post": post_to_erase
    }


async def update_post(session: AsyncSession, post_in: PostUpdateSchema):
    st = await session.execute(select(Post).filter(Post.id == post_in.id))
    post_to_update = st.scalars().first()


    for name, value in post_in.model_dump(exclude_none=True).items():
        setattr(post_to_update, name, value)

    
    await session.commit()

    return {
        "status": status.HTTP_200_OK,
        "updated_post": post_to_update
    }

    