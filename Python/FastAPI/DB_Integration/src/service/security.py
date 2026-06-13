import os
from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from email_validator import validate_email, EmailNotValidError
from jose import jwt, JWTError

from data.database import User
from data.operations import pwd_context

SECRET_KEY = os.getenv("SECRET_KEY", "A_VERY_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


async def get_user(session: AsyncSession, username: str) -> User | None:
    result = await session.execute(select(User).where(User.username == username))
    return result.scalars().first()


async def authenticate_user(
    session: AsyncSession,
    username_or_email: str,
    password: str,
) -> User | None:
    try:
        validate_email(username_or_email)
        query_filter = User.email
    except EmailNotValidError:
        query_filter = User.username
    result = await session.execute(
        select(User).where(query_filter == username_or_email)
    )
    user = result.scalars().first()
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def decode_access_token(token: str, session: AsyncSession) -> User | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
    except JWTError:
        return None
    if not username:
        return None
    return await get_user(session, username)
