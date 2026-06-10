# Cinema Management System

## 1. Giới thiệu

Cinema Management System là ứng dụng quản lý rạp chiếu phim được xây dựng bằng Python. Hệ thống hỗ trợ quản lý phim, suất chiếu, ghế ngồi, đặt vé và báo cáo thống kê. Dữ liệu được lưu trữ bằng file JSON và được giữ lại sau khi đóng chương trình.

## 2. Công nghệ sử dụng

* Python
* JSON
* OOP (Object-Oriented Programming)
* CSV
* Git/GitHub

## 3. Chức năng chính

### Movie Management

* Thêm phim.
* Hiển thị danh sách phim.
* Tìm phim theo mã phim.
* Cập nhật thông tin phim.
* Xóa phim.
* Sắp xếp phim theo tên.
* Sắp xếp phim theo thời lượng giảm dần.

### Showtime Management

* Thêm suất chiếu.
* Hiển thị danh sách suất chiếu.
* Tìm suất chiếu theo mã.
* Cập nhật suất chiếu.
* Xóa suất chiếu.

### Seat Management

* Thêm ghế Standard.
* Thêm ghế VIP.
* Thêm ghế Couple.
* Hiển thị danh sách ghế.
* Xóa ghế.
* Đánh dấu ghế đã được đặt.

### Ticket Booking

* Đặt vé.
* Tính giá vé theo loại ghế.
* Kiểm tra ghế đã được đặt hay chưa.
* Lưu thông tin vé.
* Hiển thị danh sách vé.

### Reports

* Thống kê tổng doanh thu.
* Thống kê tổng số vé đã bán.
* Thống kê tổng số phim.
* Thống kê tổng số suất chiếu.
* Thống kê số ghế còn trống.
* Xuất báo cáo ra file CSV.

---

## 4. Cấu trúc thư mục

CinemaManagement/
│
├── main.py
│
├── data/
│   ├── movies.json
│   ├── showtimes.json
│   ├── seats.json
│   ├── tickets.json
│   └── report.csv
│
├── models/
│   ├── movie.py
│   ├── showtime.py
│   ├── seat.py
│   └── ticket.py
│
├── services/
│   ├── movie_service.py
│   ├── showtime_service.py
│   ├── seat_service.py
│   └── ticket_service.py
│
└── views/
    └── menu.py


## 5. Kiến trúc hệ thống

Dự án được chia thành các tầng:

### models

Chứa các lớp đối tượng:

* Movie
* Showtime
* Seat
* Ticket

### services

Chứa các xử lý nghiệp vụ:

* CRUD dữ liệu.
* Tìm kiếm.
* Sắp xếp.
* Đặt vé.
* Lưu và đọc dữ liệu JSON.

### views

Chứa giao diện menu tương tác với người dùng.


## 6. Lưu trữ dữ liệu

Hệ thống sử dụng file JSON:

* movies.json
* showtimes.json
* seats.json
* tickets.json

Dữ liệu được lưu lại sau khi chương trình kết thúc.


## 7. Áp dụng lập trình hướng đối tượng

### Inheritance

Lớp Seat là lớp cha của:

* StandardSeat
* VIPSeat
* CoupleSeat

### Encapsulation

Dự án sử dụng thuộc tính private (__attribute) kết hợp với @property và setter trong các lớp:

* Movie
* Showtime
* Seat
* Ticket

### Polymorphism

Các lớp:

* StandardSeat
* VIPSeat
* CoupleSeat

ghi đè phương thức:

* calculate_price()
* get_seat_type()

### Abstraction

Lớp Seat được xây dựng dưới dạng Abstract Base Class (ABC) và sử dụng @abstractmethod.

## 8. Kết quả đạt được

* Xây dựng thành công hệ thống quản lý rạp chiếu phim bằng Python.
* Quản lý phim, suất chiếu, ghế ngồi và vé.
* Hỗ trợ đặt vé và tính giá theo loại ghế.
* Hỗ trợ báo cáo thống kê.
* Hỗ trợ xuất báo cáo CSV.
* Áp dụng đầy đủ các nguyên lý OOP.
* Có cấu trúc phân tầng rõ ràng.

## 9. Tự đánh giá theo thang điểm

| STT | Tiêu chí | Điểm tối đa | Tự chấm | Giải thích |
|------|----------|------------|----------|------------|
| 1 | Encapsulation | 0.5 | 0.5 | Sử dụng thuộc tính private (__attribute) kết hợp với @property và setter trong các lớp Movie, Showtime, Seat và Ticket để bảo vệ dữ liệu và kiểm soát truy cập. |
| 2 | Inheritance | 0.5 | 0.5 | Các lớp StandardSeat, VIPSeat và CoupleSeat kế thừa từ lớp cha Seat. |
| 3 | Polymorphism & Abstraction | 1.0 | 1.0 | Sử dụng lớp trừu tượng Seat kế thừa từ ABC cùng các phương thức calculate_price() và get_seat_type() được ghi đè trong các lớp con. |
| 4 | Layered Architecture | 1.0 | 1.0 | Dự án được chia thành các tầng riêng biệt gồm models, services và views, giúp dễ bảo trì và mở rộng hệ thống. |
| 5 | Clean Code (SRP) | 0.5 | 0.5 | Mỗi lớp đảm nhiệm một chức năng riêng biệt. Các phương thức và tên lớp được đặt rõ ràng, dễ hiểu. |
| 6 | Exception Handling | 0.5 | 0.5 | Sử dụng try-except để xử lý lỗi khi đọc/ghi file JSON và lỗi nhập dữ liệu không hợp lệ. |
| 7 | CRUD Operations | 1.0 | 1.0 | Hỗ trợ đầy đủ chức năng thêm, xem, sửa và xóa cho các đối tượng phim, suất chiếu, ghế và vé. |
| 8 | Search & Sort | 1.0 | 1.0 | Có chức năng tìm kiếm phim, suất chiếu, ghế và sắp xếp phim theo tên hoặc thời lượng. |
| 9 | Permanent Storage | 1.0 | 1.0 | Dữ liệu được lưu bằng file JSON (movies.json, showtimes.json, seats.json, tickets.json) và được giữ lại sau khi đóng chương trình. |
| 10 | Complex Transaction Logic | 1.0 | 1.0 | Chức năng đặt vé kiểm tra ghế tồn tại, kiểm tra ghế đã được đặt hay chưa, tính giá vé theo loại ghế và cập nhật trạng thái ghế sau khi đặt thành công. |
| 11 | Statistics & Export | 1.0 | 1.0 | Hệ thống hỗ trợ thống kê tổng doanh thu, tổng số vé đã bán, tổng số phim, tổng số suất chiếu, số ghế còn trống và xuất báo cáo ra file CSV. |
| 12 | Advanced Technology | 0.5 | 0.0 | Phiên bản hiện tại sử dụng giao diện dòng lệnh (CLI) và file JSON, chưa áp dụng GUI hoặc cơ sở dữ liệu SQLite. |
| 13 | Git & GitHub Management | 0.5 | 0.5 | Dự án được quản lý bằng Git và lưu trữ trên GitHub với lịch sử commit và các nhánh phát triển riêng. |

### TỔNG CỘNG: 9.5 / 10

## 10. Thành viên thực hiện

* Họ và tên: Lưu Thảo Ngân

* Lớp: Tin 2E

* Môn học: Programming Methods

* Giảng viên hướng dẫn: ThS. Trần Văn Long