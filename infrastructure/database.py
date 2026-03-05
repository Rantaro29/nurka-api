from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import asyncio
from config import settings

DATABASE_URL = settings.DB_URL

engine = create_async_engine(
    DATABASE_URL, 
    echo=True)

AsyncSessionLocal = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False)

async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session 

#async def init_db():
  #  async with engine.begin() as conn:
 #       await conn.run_sync(Base.metadata.create_all)
#    print("Таблицы созданы")

#asyncio.run(init_db())
