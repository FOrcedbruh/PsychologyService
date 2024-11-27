from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import PostCreateSchema
from . import utils, crud
from core.db_connection import db_connection

router = APIRouter(prefix="/posts", tags=["Posts"])



@router.post("/create")
async def create_post(
        session: AsyncSession = Depends(db_connection.session_creation),
        post_in: PostCreateSchema = Depends(utils.CreateForm)
    ):
        return await crud.create_post(session=session, post_in=post_in)


@router.patch("/update")
async def update_post(
        session: AsyncSession = Depends(db_connection.session_creation),
        post_in: dict = Depends(utils.UpdateForm)
    ):
        return await crud.update_post(session=session, post_in=post_in)



@router.delete("/erase")
async def erase_post(
        session: AsyncSession = Depends(db_connection.session_creation),
        post_id: int = Depends(utils.EraseForm)
    ):
        return await crud.erase_post(session=session, post_id=post_id)





