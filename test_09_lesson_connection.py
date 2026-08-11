from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

from conftest import Base, SessionLocal, engine


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)


Base.metadata.create_all(bind=engine)


def test_create_student():
    db = SessionLocal()
    test_email = f"alice_{uuid.uuid4()}@example.com"

    try:
        db.query(Student).filter(Student.email == test_email).delete()
        db.commit()

        student = Student(name="Alice", email=test_email)
        db.add(student)
        db.commit()
        db.refresh(student)

        assert student.id is not None
        assert student.name == "Alice"
        assert student.email == test_email
    finally:
        db.close()


def test_update_student():
    db = SessionLocal()
    test_email = f"alice_{uuid.uuid4()}@example.com"

    try:
        student = Student(name="Alice", email=test_email)
        db.add(student)
        db.commit()
        db.refresh(student)

        student.name = "Alicia"
        db.commit()
        db.refresh(student)

        assert student.name == "Alicia"
    finally:
        db.close()


def test_delete_student():
    db = SessionLocal()
    test_email = f"alice_{uuid.uuid4()}@example.com"

    try:
        student = Student(name="Alice", email=test_email)
        db.add(student)
        db.commit()

        db.delete(student)
        db.commit()

        deleted = db.query(Student).filter(Student.email == test_email).first()
        assert deleted is None
    finally:
        db.close()
       # 