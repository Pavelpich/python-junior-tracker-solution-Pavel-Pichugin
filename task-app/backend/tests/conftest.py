from typing import Generator
import os
import pytest
from starlette.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# SQLite in-memory в тесте
os.environ["DATABASE_URL"] = "sqlite:///./test.db"
os.environ["ENVIRONMENT"] = "test"

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

import app.db.database as database_module
from app.main import app
from app.db.database import Base, get_db

database_module.engine = engine
database_module.SessionLocal = TestingSessionLocal


@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../test.db"))
    if os.path.exists(db_path):
        os.remove(db_path)

    Base.metadata.create_all(bind=engine)
    yield

    Base.metadata.drop_all(bind=engine)
    engine.dispose()

    # удаляем test.db
    if os.path.exists(db_path):
        os.remove(db_path)


@pytest.fixture(scope="function")
def db_override() -> Generator[Session, None, None]:
    """
    перед каждым тестом создаём таблицы
    Возвращает сессию SQLAlchemy.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


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
