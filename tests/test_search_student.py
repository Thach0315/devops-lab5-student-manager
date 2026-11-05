"""Tests for the search-student feature."""

import unittest

from src.main import search_student
from src.student import Student


class SearchStudentTests(unittest.TestCase):
    def setUp(self):
        self.students = [Student("SV001", "Nguyen Van A", 20, "K20")]

    def test_search_matches_name_case_insensitively(self):
        results = search_student(self.students, "vAn")
        self.assertEqual([student.student_id for student in results], ["SV001"])

    def test_search_matches_id_and_returns_empty_when_missing(self):
        self.assertEqual(search_student(self.students, "sv001"), self.students)
        self.assertEqual(search_student(self.students, "missing"), [])

    def test_empty_keyword_returns_all_students(self):
        self.assertEqual(search_student(self.students, ""), self.students)


if __name__ == "__main__":
    unittest.main()
