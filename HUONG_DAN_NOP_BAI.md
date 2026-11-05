# Hướng dẫn hoàn tất và nộp Lab 5

## Trạng thái hiện tại

Đã tạo repo GitHub công khai: https://github.com/Thach0315/devops-lab5-student-manager; đã push các nhánh chính và mở hai PR vào `develop`:

- PR #1 (search): https://github.com/Thach0315/devops-lab5-student-manager/pull/1
- PR #2 (add): https://github.com/Thach0315/devops-lab5-student-manager/pull/2

**ThachRC đã chấp nhận** lời mời collaborator quyền ghi và đã được gán reviewer cho hai PR. Tại lần kiểm tra gần nhất, chưa có review nào được gửi; cần review/approve trước khi merge. Không tự duyệt PR của chính mình. Không đưa token/mật khẩu vào mã nguồn hoặc ZIP.

## Trước khi nộp

1. Đã ghi Dev A: Hoàng Thạch An và Dev B: ThachRC trong `README.md`.
2. ThachRC đã chấp nhận lời mời collaborator.
3. ThachRC review, để lại nhận xét, approve hai PR; sau đó tác giả merge.
4. Các nhánh chính và hai nhánh PR đã push. Nếu cần đồng bộ lại sau khi thêm commit:

   ```bash
   git remote -v
   git push -u origin main
   git push -u origin develop
   git push origin feature/add-student feature/search-student
   ```

5. Bài thực hành conflict đã được tạo và resolve trong lịch sử Git cục bộ; phần GitHub remote chưa có minh chứng conflict. Thực hiện lại bằng nhánh/PR thứ hai sau khi PR đầu tiên đã merge nếu cần trình diễn conflict trực tiếp trên GitHub.
6. Sau khi các PR hoàn tất, cập nhật `main` từ `develop` theo hướng dẫn lab. Kiểm tra `python3 src/main.py` và `git status`.
7. Đã chụp các ảnh GitHub có thể tự động vào `screenshots/`. Bổ sung ảnh code review, conflict, conflict resolved và output chương trình thật; không thay bằng ảnh giả.

## Danh sách minh chứng

| Tên ảnh | Nội dung cần thấy | Trạng thái |
|---|---|---|
| `01-git-log.png` | Lịch sử commit trên GitHub | Đã chụp GitHub commit history; nếu yêu cầu đúng lệnh CLI thì thay bằng ảnh terminal `git log --oneline --graph --all` |
| `02-git-branch.png` | Danh sách nhánh | Đã chụp GitHub Branches; nếu yêu cầu đúng lệnh CLI thì thay bằng ảnh terminal `git branch -a` |
| `03-pr-add-student.png` | PR add-student trên GitHub | Đã chụp PR #2 (GitHub đã đánh số #2) |
| `04-pr-search-student.png` | PR search-student trên GitHub | Đã chụp PR #1 (GitHub đã đánh số #1) |
| `05-code-review.png` | Code Review comment | Chờ ThachRC review |
| `06-merge-conflict.png` | Conflict trong VS Code | Cần chụp màn hình conflict thật |
| `07-conflict-resolved.png` | Sau khi resolve conflict | Cần chụp màn hình kết quả thật |
| `08-final-output.png` | `python src/main.py` output | Cần chụp terminal thật |

## Đóng gói ZIP

Đứng tại thư mục dự án, sau khi đủ 8 ảnh, tạo ZIP đúng mẫu `Lab5_NhomX_HoTenA_HoTenB.zip`. Theo file hướng dẫn, ZIP gồm `README.md`, `.gitignore` và `screenshots/` chứa đúng 8 ảnh dưới đây. Ví dụ tên theo nhóm hiện tại: `Lab5_NhomAn_HoangThachAn_ThachRC.zip`.

```text
Lab5_NhomAn_HoangThachAn_ThachRC.zip
├── README.md
├── .gitignore
└── screenshots/
    ├── 01-git-log.png
    ├── 02-git-branch.png
    ├── 03-pr-add-student.png
    ├── 04-pr-search-student.png
    ├── 05-code-review.png
    ├── 06-merge-conflict.png
    ├── 07-conflict-resolved.png
    └── 08-final-output.png
```

```bash
zip -r Lab5_NhomAn_HoangThachAn_ThachRC.zip README.md .gitignore screenshots/01-git-log.png screenshots/02-git-branch.png screenshots/03-pr-add-student.png screenshots/04-pr-search-student.png screenshots/05-code-review.png screenshots/06-merge-conflict.png screenshots/07-conflict-resolved.png screenshots/08-final-output.png
unzip -l Lab5_NhomAn_HoangThachAn_ThachRC.zip
```

Upload ZIP lên LMS trước deadline. Mở lại ZIP để chắc chắn đủ file và ảnh trước khi nộp.

## Checklist cuối

- [x] Ghi Dev B là ThachRC trong README.
- [ ] Repo GitHub có main và develop; code đã push.
- [ ] Hai PR đã được review, approve và merged.
- [ ] Đã thực hành và chụp minh chứng merge conflict.
- [ ] Đủ 8 ảnh `.png` đúng tên trong `screenshots/`.
- [ ] Chương trình chạy thành công; ZIP mở được và đã upload lên LMS.
