import pytest
from database import SessionLocal, init_db
from models import Student


@pytest.fixture(scope="session")
def db():
    init_db()
    session = SessionLocal()
    session.query(Student).delete()
    session.commit()
    yield session
    session.close()
