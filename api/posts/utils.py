from fastapi import Body, Depends, HTTPException, status
from .schemas import PostCreateSchema, PostUpdateSchema
from api.auth.schemas import UserSchema
from api.auth.utils import get_current_authuser



def CreateForm(post_in: PostCreateSchema = Body(), authUser: UserSchema = Depends(get_current_authuser)) -> PostCreateSchema:
    if not authUser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Вы не авторизованы"
        )
    
    
    return PostCreateSchema(
        title=post_in.title,
        receiver=post_in.receiver,
        type=post_in.type,
        user_id=authUser.id,
        body=post_in.body
    )




def EraseForm(post_id: int = Body(), authUser: UserSchema = Depends(get_current_authuser)) -> int:
    if not authUser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Вы не авторизованы"
        )
    
    return post_id


def UpdateForm(post_in: PostUpdateSchema = Body(), authUser: UserSchema = Depends(get_current_authuser)) -> PostUpdateSchema:
    if not authUser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Вы не авторизованы"
        )
    
    return PostUpdateSchema(
            title=post_in.title,
            body=post_in.body,
            type=post_in.type,
            id=post_in.id
        )