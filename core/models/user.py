from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .invite import Invite
    from .post import Post


class User(Base):
    __tablename__ = "users"

    login: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[bytes] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    invite: Mapped["Invite"] = relationship(back_populates="users")
    invite_id: Mapped[int] = mapped_column(ForeignKey("invites.id"), nullable=False)
    bio: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(nullable=True)
    role: Mapped[str] = mapped_column(nullable=False, default="User")

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
