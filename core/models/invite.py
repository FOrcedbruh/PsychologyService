from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class Invite(Base):
    __tablename__ = "invites"

    value: Mapped[str] = mapped_column(nullable=False)
    users: Mapped["User"] = relationship(back_populates="invite")
    limit: Mapped[int] = mapped_column(nullable=False, default=1)
    is_activate: Mapped[bool] = mapped_column(nullable=False, default=True)
    type: Mapped[str] = mapped_column(default="disposable")
