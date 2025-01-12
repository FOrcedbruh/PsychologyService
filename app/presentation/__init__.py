from fastapi import APIRouter
from .InviteRouter import router as InvitesRouter
from .AuthRouter import router as AuthRouter
from .UserRouter import router as UserRouter

router = APIRouter(prefix="/api/v1")
router.include_router(router=InvitesRouter)
router.include_router(router=AuthRouter)
router.include_router(router=UserRouter)