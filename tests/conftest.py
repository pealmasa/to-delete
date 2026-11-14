from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.database import Base, get_db
from app.main import app

TEST_DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture(scope="session")
def engine() -> Iterator[Engine]:
    engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db(engine: Engine) -> Iterator[Session]:
    """Fresh DB session per test — no state leaks between tests."""
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    yield session
    session.rollback()
    session.close()


@pytest.fixture(scope="function")
def client(db: Session) -> Iterator[TestClient]:
    """TestClient with DB override."""
    app.dependency_overrides[get_db] = lambda: db
    yield TestClient(app)
    app.dependency_overrides.clear()
