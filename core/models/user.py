from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .invite import Invite


class User(Base):
    __tablename__ = "users"

    login: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[bytes] = mapped_column(nullable=True)
    invite: Mapped["Invite"] = relationship(back_populates="user")
    invite_id: Mapped[int] = mapped_column(ForeignKey("invites.id"))
    bio: Mapped[str]
    status: Mapped[str]
