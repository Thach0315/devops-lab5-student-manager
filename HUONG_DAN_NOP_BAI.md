# Hướng dẫn hoàn tất và nộp Lab 5

## Trạng thái hiện tại

Đã tạo repo GitHub công khai: https://github.com/Thach0315/devops-lab5-student-manager; đã push các nhánh chính và mở hai PR vào `develop`:

- PR #1 (search): https://github.com/Thach0315/devops-lab5-student-manager/pull/1
- PR #2 (add): https://github.com/Thach0315/devops-lab5-student-manager/pull/2

PR đang mở và chờ review. Vì cả hai PR do cùng tài khoản tác giả tạo, cần thành viên thứ hai được mời vào repo để review/approve; không tự duyệt PR của chính mình. Không đưa token/mật khẩu vào mã nguồn hoặc ZIP.

## Trước khi nộp

1. Điền họ tên Dev B trong `README.md` (Dev A: Hoàng Thạch An; repo: tài khoản Thach0315).
2. Thêm thành viên còn lại làm collaborator tại GitHub → Settings → Collaborators và để họ chấp nhận lời mời.
3. Hai PR đã mở sẵn; thành viên còn lại review, để lại nhận xét, approve. Tác giả merge PR sau khi review.
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
| `01-github-commit-history.jpg` | Lịch sử commit GitHub trên main | Đã chụp; cần chụp thêm terminal `git log --oneline --graph --all` nếu rubric yêu cầu chính xác lệnh này |
| `02-github-branches.jpg` | Danh sách nhánh GitHub | Đã chụp; có main/develop/feature |
| `03-pr-add-student.jpg` | PR add-student trên GitHub | Đã chụp; PR #2 đang mở, chưa merged |
| `04-pr-search-student.jpg` | PR search-student trên GitHub | Đã chụp; PR #1 đang mở, chưa merged |
| `05-code-review.png` | Review/comment và trạng thái approve | Chưa có — cần thành viên thứ hai |
| `06-merge-conflict.png` | Conflict marker hoặc GitHub báo conflict | Chưa có ảnh — lịch sử conflict hiện tại là local |
| `07-conflict-resolved.png` | Bản README sau resolve và trạng thái sạch | Chưa có ảnh minh chứng |
| `08-final-output.png` | Terminal chạy `python3 src/main.py` thành công | Chưa có ảnh minh chứng |

## Đóng gói ZIP

Đứng tại thư mục dự án, sau khi đã thêm đủ ảnh thật, tạo ZIP với tên theo mẫu `Lab5_NhomX_HoTenA_HoTenB.zip`. ZIP cần có `README.md`, `.gitignore`, `src/`, và `screenshots/` với ảnh minh chứng thật. Xóa `screenshots/README.md` khỏi gói nếu muốn thư mục chỉ có ảnh. Không cần đưa thư mục `.git/` vào ZIP trừ khi giảng viên yêu cầu.

```bash
zip -r Lab5_NhomX_HoTenA_HoTenB.zip README.md .gitignore src screenshots
unzip -l Lab5_NhomX_HoTenA_HoTenB.zip
```

Upload ZIP lên LMS trước deadline. Mở lại ZIP để chắc chắn đủ file và ảnh trước khi nộp.

## Checklist cuối

- [ ] Điền tên Dev B trong README.
- [ ] Repo GitHub có main và develop; code đã push.
- [ ] Hai PR đã được review, approve và merged.
- [ ] Đã thực hành và chụp minh chứng merge conflict.
- [ ] Đủ 8 ảnh trong `screenshots/`.
- [ ] Chương trình chạy thành công; ZIP mở được và đã upload lên LMS.
