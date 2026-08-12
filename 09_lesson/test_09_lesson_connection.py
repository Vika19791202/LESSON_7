import uuid
from models import Student


def test_create_student(db):
    test_email = f"alice_{uuid.uuid4()}@example.com"
    student = Student(name="Alice", email=test_email)
    db.add(student)
    db.commit()
    db.refresh(student)

    assert student.id is not None
    assert student.name == "Alice"
    assert student.email == test_email


def test_update_student(db):
    test_email = f"alice_{uuid.uuid4()}@example.com"
    student = Student(name="Alice", email=test_email)
    db.add(student)
    db.commit()
    db.refresh(student)

    student.name = "Alicia"
    db.commit()
    db.refresh(student)

    assert student.name == "Alicia"


def test_delete_student(db):
    test_email = f"alice_{uuid.uuid4()}@example.com"
    student = Student(name="Alice", email=test_email)
    db.add(student)
    db.commit()

    db.delete(student)
    db.commit()

    deleted = db.query(Student).filter(Student.email == test_email).first()
    assert deleted is None
