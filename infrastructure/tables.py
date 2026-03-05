from domain.entities.user import Role
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, String, DateTime, func, text, ForeignKey
from sqlalchemy.dialects.postgresql import BIGINT
from typing import Optional, Annotated
from datetime import datetime
from sqlalchemy import Enum as SAEnum # Импортируй это в начале файла
from sqlalchemy.dialects.postgresql import ENUM

int_primary_key = Annotated[int, mapped_column(primary_key = True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
title_url = Annotated[str, mapped_column (String(255), nullable=False, unique=True)]
type_url = Annotated[str, mapped_column (String(255), nullable=False, unique=True)]


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int_primary_key]

    username: Mapped[str] = mapped_column (
        String(32),
        unique=True,
        nullable=True
    ) 

    role: Mapped[Role] = mapped_column(ENUM(Role, name="role", create_type=True), nullable=False, default=Role.user)
    
    first_name: Mapped[str] = mapped_column (
        String(64),
        unique = False,
        nullable = False,
    )

    last_name: Mapped[str] = mapped_column (
        String(64),
        unique = False,
        nullable = True,
    )

    telegram_id: Mapped[int] = mapped_column (
        BigInteger,
        unique=True,
        nullable=False
    )

    phone_number: Mapped[str] = mapped_column (
        String(20),
        nullable = True,
        unique = True
    )

    created_at: Mapped[created_at]

class FAQ(Base):
    __tablename__ = "faq"

    id: Mapped[int_primary_key]

    title: Mapped[title_url]

    url: Mapped[type_url]

    moderator_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False    
    )


    created_at: Mapped[created_at]

class Channel(Base):
    __tablename__ = "channel"

    id: Mapped[int_primary_key]

    title: Mapped[title_url]

    url: Mapped[type_url]

    moderator_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False    
    )


    created_at: Mapped[created_at]