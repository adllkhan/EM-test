from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .core import Config


engine = create_async_engine(Config().db_host)

Session = async_sessionmaker(bind=engine)

Base = declarative_base()
