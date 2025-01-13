from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import TYPE_CHECKING
from sqlalchemy import ARRAY, String
from sqlalchemy.ext.mutable import MutableList

if TYPE_CHECKING:
    from .post import Post



class User(Base):
    __tablename__ = "users"

    telegram_user_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=True)
    tel: Mapped[str] = mapped_column(unique=True, nullable=True)
    hobbies: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String)), nullable=True)
    profile_image: Mapped[str] = mapped_column(unique=True, nullable=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")