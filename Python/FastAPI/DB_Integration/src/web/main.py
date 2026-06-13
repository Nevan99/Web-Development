from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated
from sqlalchemy.exc import SQLAlchemyError

from data.database import Base
from data.db_connection import get_engine, AsyncSession, get_db_session
from data.operations import add_user, create_ticket, update_ticket, delete_ticket, get_ticket as ops_get_ticket
from schema.schema import UserCreateBody, UserCreateResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


class TicketRequest(BaseModel):
    price: float | None
    show: str | None
    user: str | None


@app.post('/ticket', response_model=dict[str, int])
async def create_ticket_route(ticket: TicketRequest, db_session: Annotated[AsyncSession, Depends(get_db_session)]):
    try:
        ticket_id = await create_ticket(db_session, ticket.show, ticket.user, ticket.price)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")
    return {"ticket_id": ticket_id}


@app.get('/ticket/{ticket_id}', response_model=dict)
async def get_ticket_route(ticket_id: int, db_session: Annotated[AsyncSession, Depends(get_db_session)]) -> dict:
    try:
        ticket = await ops_get_ticket(db_session, ticket_id)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")

    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {
        "id": ticket.id,
        "show": ticket.show,
        "user": ticket.user,
        "price": ticket.price,
    }

@app.post("/register/user", status_code=status.HTTP_201_CREATED, response_model=UserCreateResponse, responses={status.HTTP_409_CONFLICT:{"description": "THe user already exists"}},)
async def register(
    user: UserCreateBody,
    db_session: AsyncSession = Depends(get_db_session),
) -> dict[str, str | UserCreateResponse]:
    user = await add_user(
        db_session=db_session, **user.model_dump()
    )
    if not user:
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            "username or email already exists",
        )
    user_response = UserCreateResponse(
        username = user.username, email=user.email
    )
    return {
        "message": "user created",
        "user": user_response,
    }
