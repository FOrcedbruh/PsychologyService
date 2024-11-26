from fastapi import status, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import PostCreateSchema
from core.models import Post


async def create_post(session: AsyncSession, post_in: PostCreateSchema) -> dict:
    post = Post(**post_in.model_dump())
    session.add(post)

    await session.commit()

    return {
        "status": status.HTTP_200_OK,
        "created_post": post
    }

