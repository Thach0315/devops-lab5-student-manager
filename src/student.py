"""Student model for the DevOps Lab 5 student manager."""


class Student:
    """Represent a student with an ID, name, age, and grade."""

    def __init__(self, student_id: str, name: str, age: int, grade: str):
        if not student_id.strip():
            raise ValueError("student_id must not be empty")
        if not name.strip():
            raise ValueError("name must not be empty")
        if age < 0:
            raise ValueError("age must not be negative")
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self) -> str:
        return (
            f"Student(id={self.student_id}, name='{self.name}', "
            f"age={self.age}, grade='{self.grade}')"
        )

    def to_dict(self) -> dict:
        """Return this student as a dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
        }
