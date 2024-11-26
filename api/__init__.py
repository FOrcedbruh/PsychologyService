from fastapi import APIRouter
from .invites.views import router as inviteRouter
from .auth.views import router as authRouter
from .posts.views import router as postsRouter

router = APIRouter(prefix="/api")
router.include_router(router=inviteRouter)
router.include_router(router=authRouter)
router.include_router(router=postsRouter)