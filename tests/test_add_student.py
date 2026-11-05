"""Tests for the add-student feature."""

import unittest

from src.main import add_student
from src.student import Student


class AddStudentTests(unittest.TestCase):
    def test_adds_new_student(self):
        students = [Student("SV001", "Nguyen Van A", 20, "K20")]
        add_student(students, "SV002", "Tran Thi B", 21, "K20")
        self.assertEqual([student.student_id for student in students], ["SV001", "SV002"])

    def test_rejects_duplicate_id(self):
        students = [Student("SV001", "Nguyen Van A", 20, "K20")]
        add_student(students, "SV001", "Someone Else", 22, "K19")
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Nguyen Van A")


if __name__ == "__main__":
    unittest.main()
