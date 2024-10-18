from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from .user import User


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    receiver: Mapped[str] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship(back_populates="posts")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))