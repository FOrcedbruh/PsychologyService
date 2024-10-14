from fastapi import APIRouter
from .invites.views import router as inviteRouter

router = APIRouter(prefix="/api")
router.include_router(router=inviteRouter)