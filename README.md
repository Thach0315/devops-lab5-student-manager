# Student Manager

Ứng dụng quản lý sinh viên — DevOps Lab 5: Git Flow & Code Review.

**Version 1.0.0** — Nhóm An – Hoàng Thạch An.

## Tính năng

- Mô hình sinh viên với mã, họ tên, tuổi và khóa.
- Thêm sinh viên mới; từ chối mã sinh viên bị trùng.
- Tìm kiếm không phân biệt hoa thường theo tên hoặc mã sinh viên.

## Chạy ứng dụng

Yêu cầu Python 3.10 trở lên; không cần cài thư viện ngoài.

```bash
python3 src/main.py
```

Chạy kiểm thử tự động:

```bash
python3 -m unittest discover -s tests -v
```

## Cấu trúc

```text
src/main.py       # Ứng dụng và chức năng thêm/tìm kiếm
src/student.py    # Student model
tests/            # Unit tests cho thêm và tìm kiếm sinh viên
screenshots/      # Ảnh minh chứng cho bài nộp
```

## GitHub

Repo: [Thach0315/devops-lab5-student-manager](https://github.com/Thach0315/devops-lab5-student-manager)

## Tác giả

- Dev A: Hoàng Thạch An
- Dev B: _điền họ tên_
- DevOps Course — Lab 5
