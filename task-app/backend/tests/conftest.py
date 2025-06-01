from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.main import app
from app.db.database import Base, get_db

# SQLite in-memory в тесте
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_override() -> Generator[Session, None, None]:
    """
    перед каждым тестом создаём таблицы
    Возвращает сессию SQLAlchemy.
    """
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_override: Session) -> TestClient:
    """
    переопределяем get_db, чтобы вместо postgre
    использовать тестовую sqlite, возвращаем TestClient
    """

    def _get_test_db() -> Generator[Session, None, None]:
        yield db_override

    app.dependency_overrides[get_db] = _get_test_db
    return TestClient(app)
