from sqlalchemy.orm import Mapped, mapped_column
from .base import Base




class Confirmation_Code(Base):
    __tablename__ = "confirmation_codes"

    value: Mapped[str] = mapped_column(nullable=False)
    user_email: Mapped[str] = mapped_column(nullable=False)