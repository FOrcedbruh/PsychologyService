from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User



class Disposable_Invite(Base):
    __tablename__ = "disposable_invites"

    value: Mapped[str] = mapped_column(nullable=False)

    from_user: Mapped["User"] = relationship(back_populates="disposable_invite")
    from_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=False)

    to_user: Mapped["User"] = relationship(back_populates="disposable_invite")
    to_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=False)

    is_used: Mapped[bool] = mapped_column(default=False)