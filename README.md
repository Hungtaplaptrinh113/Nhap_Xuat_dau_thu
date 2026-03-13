# Ứng dụng nhập – xuất dầu (Streamlit)

Ứng dụng web nhỏ viết bằng **Python + Streamlit** để nhập và lưu dữ liệu **nhập – xuất dầu** giống file Excel hiện tại của bạn.

## 1. Yêu cầu

- Python 3 đã cài trên máy
- Các thư viện trong `requirements.txt`:
  - `streamlit`
  - `pandas`
  - `openpyxl`

## 2. Cài đặt thư viện

Mở **PowerShell** trong thư mục dự án này và chạy:

```bash
pip install -r requirements.txt
```

## 3. Chạy ứng dụng

Trong thư mục dự án, chạy:

```bash
streamlit run app.py
```

Sau khi chạy, Streamlit sẽ in ra đường dẫn, thường là:

```text
http://localhost:8501
```

Mở trình duyệt (Chrome/Edge, ...) và truy cập đường dẫn đó để sử dụng ứng dụng.

## 4. Lưu dữ liệu

- Mỗi lần bấm nút **“Lưu vào Excel”**, ứng dụng sẽ ghi thêm một dòng vào file:
  - `du_lieu_nhap_xuat_dau.xlsx`
- File Excel được lưu ngay trong thư mục dự án.

## 5. Tùy chỉnh thêm

- Nếu bạn muốn đổi tên cột, thêm/bớt cột hoặc thay đổi công thức tính **chênh lệch**, hãy chỉnh trực tiếp trong file `app.py` hoặc gửi yêu cầu chi tiết để tôi sửa giúp.

