"""Command-line student manager for the DevOps Lab 5."""

try:  # Supports both `python src/main.py` and package-style imports.
    from .student import Student
except ImportError:
    from student import Student


def add_student(
    students: list[Student], student_id: str, name: str, age: int, grade: str
) -> list[Student]:
    """Append a student unless the ID already exists; return the list."""
    if any(student.student_id == student_id for student in students):
        print(f"❌ Mã sinh viên {student_id} đã tồn tại!")
        return students

    new_student = Student(student_id, name, age, grade)
    students.append(new_student)
    print(f"Đã thêm sinh viên: {new_student}")
    return students


def search_student(students: list[Student], keyword: str) -> list[Student]:
    """Find students by a case-insensitive name or ID substring."""
    normalized_keyword = keyword.casefold()
    results = [
        student
        for student in students
        if normalized_keyword in student.name.casefold()
        or normalized_keyword in student.student_id.casefold()
    ]
    if results:
        print(f"🔍 Tìm thấy {len(results)} sinh viên với từ khóa '{keyword}':")
        for student in results:
            print(f"  {student}")
    else:
        print(f"❌ Không tìm thấy sinh viên nào với từ khóa '{keyword}'")
    return results


def main() -> None:
    """Run the sample application and demonstrate both features."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]
    add_student(students, "SV004", "Pham Thi D", 22, "K19")
    print("\n--- Danh sách sinh viên ---")
    for student in students:
        print(f"  {student}")
    print(f"\nTotal: {len(students)} students")
    print("\n--- Tìm kiếm ---")
    search_student(students, "Van")


if __name__ == "__main__":
    main()
