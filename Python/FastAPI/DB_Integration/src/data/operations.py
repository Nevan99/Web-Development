from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from .database import Ticket, User
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_ticket(
    db_session: AsyncSession,
    show_name: str,
    user: str | None = None,
    price: float | None = None,
) -> int:
    ticket = Ticket(show=show_name, user=user, price=price)
    db_session.add(ticket)
    await db_session.flush()
    ticket_id = ticket.id
    await db_session.commit()
    return ticket_id


async def get_ticket(db_session: AsyncSession, ticket_id: int) -> Ticket | None:
    query = select(Ticket).where(Ticket.id == ticket_id)
    result = await db_session.execute(query)
    return result.scalars().first()


async def update_ticket(db_session: AsyncSession, ticket_id: int, new_price: float) -> bool:
    query = update(Ticket).where(Ticket.id == ticket_id).values(price=new_price)
    result = await db_session.execute(query)
    await db_session.commit()
    return result.rowcount > 0


async def delete_ticket(db_session: AsyncSession, ticket_id: int) -> bool:
    result = await db_session.execute(delete(Ticket).where(Ticket.id == ticket_id))
    await db_session.commit()
    return result.rowcount > 0

async def add_user(db_session: AsyncSession, username: str, password: str, email: str) -> User| None:
    hashed_password = pwd_context.hash(password)
    db_user = User(username=username, 
                   email=email,
                   hashed_password=hashed_password,
                   )
    db_session.add(db_user)
    try: 
        await db_session.commit()
        await db_session.refresh(db_user)
    except IntegrityError:
        await db_session.rollback()
        return
    return db_user

