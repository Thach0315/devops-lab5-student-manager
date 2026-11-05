# Hướng dẫn hoàn tất và nộp Lab 5

## Trạng thái hiện tại

Đã chuẩn bị ứng dụng Python, `.gitignore`, README và repo/lịch sử Git cục bộ. Các bước sau **không thể tự làm nếu chưa có tài khoản và thao tác của hai thành viên**: tạo repo GitHub, mời collaborator, tạo/duyệt PR và chụp ảnh màn hình thật. Không đưa token/mật khẩu vào mã nguồn hoặc ZIP.

## Trước khi nộp

1. Điền tên nhóm, họ tên Dev A/Dev B và URL repo thật trong `README.md`.
2. Một thành viên tạo repo public `devops-lab5-student-manager` trên GitHub (không tạo README/.gitignore ở GitHub), thêm thành viên còn lại làm collaborator và chấp nhận lời mời.
3. Thêm remote rồi push các nhánh cần thiết:

   ```bash
   git remote add origin https://github.com/<USERNAME>/devops-lab5-student-manager.git
   git push -u origin main
   git push -u origin develop
   git push origin feature/add-student feature/search-student
   ```

4. Trên GitHub tạo **2 PR riêng** từ `feature/add-student` và `feature/search-student` vào `develop`. Thành viên kia review, để lại nhận xét, approve; tác giả merge. PR phải hiển thị trạng thái **Merged**.
5. Thực hiện bài thực hành conflict giữa hai nhánh README trên GitHub (hoặc trong repo clone riêng của thành viên thứ hai), giải quyết và ghi nhận kết quả. Lịch sử local đã có nội dung tích hợp; cần ảnh thật chứng minh quy trình conflict.
6. Sau khi tích hợp, cập nhật `main` từ `develop` nếu repo remote chưa phản ánh bản hoàn chỉnh. Kiểm tra `python3 src/main.py` và `git status`.
7. Chụp ảnh thật vào `screenshots/` theo danh sách dưới đây. Ảnh PR/review phải chụp trên GitHub; không thay bằng ảnh giả hoặc ảnh mẫu.

## Danh sách minh chứng

| Tên ảnh | Nội dung cần thấy | Trạng thái |
|---|---|---|
| `01-git-log.png` | `git log --oneline --graph --all` | Chụp sau khi hoàn tất lịch sử |
| `02-git-branch.png` | `git branch -a` có main, develop, feature | Chụp sau khi push |
| `03-pr-add-student.png` | PR add-student đã merged vào develop | Chưa chụp — cần GitHub |
| `04-pr-search-student.png` | PR search-student đã merged vào develop | Chưa chụp — cần GitHub |
| `05-code-review.png` | Review/comment và trạng thái approve | Chưa chụp — cần hai thành viên |
| `06-merge-conflict.png` | Conflict marker hoặc GitHub báo conflict | Chưa chụp — cần thực hành |
| `07-conflict-resolved.png` | Bản README sau resolve và trạng thái sạch | Chụp sau khi resolve |
| `08-final-output.png` | Terminal chạy `python3 src/main.py` thành công | Chụp sau khi chạy |

## Đóng gói ZIP

Đứng tại thư mục dự án, sau khi đã thêm đủ ảnh thật, tạo ZIP với tên theo mẫu `Lab5_NhomX_HoTenA_HoTenB.zip`. ZIP cần có `README.md`, `.gitignore`, `src/`, và `screenshots/` với ảnh minh chứng thật. Xóa `screenshots/README.md` khỏi gói nếu muốn thư mục chỉ có ảnh. Không cần đưa thư mục `.git/` vào ZIP trừ khi giảng viên yêu cầu.

```bash
zip -r Lab5_NhomX_HoTenA_HoTenB.zip README.md .gitignore src screenshots
unzip -l Lab5_NhomX_HoTenA_HoTenB.zip
```

Upload ZIP lên LMS trước deadline. Mở lại ZIP để chắc chắn đủ file và ảnh trước khi nộp.

## Checklist cuối

- [ ] Thay tên nhóm/thành viên/URL placeholder trong README.
- [ ] Repo GitHub có main và develop; code đã push.
- [ ] Hai PR đã được review, approve và merged.
- [ ] Đã thực hành và chụp minh chứng merge conflict.
- [ ] Đủ 8 ảnh trong `screenshots/`.
- [ ] Chương trình chạy thành công; ZIP mở được và đã upload lên LMS.
