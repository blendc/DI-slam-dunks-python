import logging

from sqlalchemy import create_engine, orm
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base

logger = logging.getLogger(__name__)
Base = declarative_base()


class Database:
    def __init__(self, db_url: URL | str) -> None:
        logger.info("Database initializing...")
        self._engine = create_engine(db_url, future=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                bind=self._engine,
                future=True
            ),
        )
        logger.info("Database initialized.")

    @property
    def session(self) -> orm.Session:
        return self._session_factory()
