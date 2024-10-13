from .base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Invite(Base):
    __tablename__ = "invites"

    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    used: Mapped[bool] = mapped_column(nullable=False, default=False)
    value: Mapped[str] = mapped_column(nullable=False)
