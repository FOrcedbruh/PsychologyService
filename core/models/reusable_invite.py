from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class Reusable_invite(Base):
    __tablename__ = "reusable_invites"

    value: Mapped[str] = mapped_column(nullable=False)

    from_user: Mapped["User"] = relationship(back_populates="reusable_invite")
    from_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=False)

    to_user: Mapped["User"] = relationship(back_populates="reusable_invite")
    to_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=False)

    limit: Mapped[int] = mapped_column(nullable=False, default=99)
    is_activate: Mapped[bool] = mapped_column(nullable=False, default=False)
