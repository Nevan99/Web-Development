from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///database.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

def get_engine():
    return engine

async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session