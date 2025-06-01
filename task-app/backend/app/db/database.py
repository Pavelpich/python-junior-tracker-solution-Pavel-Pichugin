from typing import Generator

from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    raise NotImplementedError
