import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLALCHEMY_DATABASE_URL = f"sqlite+aiosqlite:///{os.path.join(_BASE_DIR, 'database.db')}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

def get_engine():
    return engine

async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session