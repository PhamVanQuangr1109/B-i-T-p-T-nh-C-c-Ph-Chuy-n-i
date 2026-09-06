#import thư viện sys để dùng lệnh thoát chương trình khi gặp lỗi
import sys

#1. Nhập thông tin chuyến đi
ten_khach_hang=input("Nhập tên khách hàng: ").strip()
quang_duong_str=input("Nhập quãng đường (km): ").strip()
gio_xuat_phat_str=input("Nhập giờ xuất phát: ").strip()
loai_xe=input("Nhập loại xe (4 cho/7 cho): ").strip()
thoi_tiet=input("Trời có mưa không? (co/khong): ").strip()

#2. Kiểm tra dữ liệu hợp lệ

#Kiểm tra tên
if not ten_khach_hang:
    print("Tên khách hàng không được để trống!")
    sys.exit()

#Kiểm tra quãng đường
try:
    quang_duong=int(quang_duong_str)
    if quang_duong <= 0:
        print("Quãng đường phải > 0")
        sys.exit
except ValueError:
    print("Quãng đường không hợp lệ!")
    sys.exit()

#Kiểm tra giờ xuất phát
try:
    gio_xuat_phat=int(gio_xuat_phat_str)
    if (gio_xuat_phat < 0) or (gio_xuat_phat > 23):
        print("Giờ xuất phát phải thuộc 0-23")
        sys.exit()
except ValueError:
    print("Giờ xuất phát không hợp lệ!")
    sys.exit()

#Kiểm tra loại xe
if loai_xe not in ["4 cho", "7 cho"]:
    print("Loại xe chỉ được là \"4 cho\" hoặc \"7 cho\"")
    sys.exit()

#3. Tính toán cước phí

#Cước cơ bản
if loai_xe == "4 cho":
    don_gia=12_000
else:
    don_gia=15_000
cuoc_co_ban=quang_duong*don_gia

#Phụ thu giờ cao điểm
phi_gio_cao_diem=0
if (6 <= gio_xuat_phat <= 8) or (17 <= gio_xuat_phat <= 19):
    phi_gio_cao_diem=cuoc_co_ban*0.1

#Phụ thu trời mưa
phu_thu_mua=0
if thoi_tiet=="co":
    phu_thu_mua=5_000*quang_duong

#Tính tổng cước
tong_cuoc=cuoc_co_ban+phi_gio_cao_diem+phu_thu_mua

#4. Phân loại chuyến đi
loai_chuyen_di=""
if quang_duong < 5:
    loai_chuyen_di="Chuyến ngắn"
elif 5 <= quang_duong <= 15:
    loai_chuyen_di="Chuyến trung bình"
else:
    loai_chuyen_di="Chuyến dài"

#5. Mức độ ưu tiên điều xe
uu_tien_dieu_xe=""
if loai_chuyen_di=="Chuyến dài":
    uu_tien_dieu_xe="Tài xế nhiều kinh nghiệm"
elif loai_chuyen_di=="Chuyến ngắn":
    uu_tien_dieu_xe="Ưu tiên tài xế gần nhất"
else:
    uu_tien_dieu_xe="Bình thường"

#6. Đánh giá mức cước
muc_cuoc=""
if tong_cuoc > 150_000:
    muc_cuoc="Cao"
else:
    muc_cuoc="Thấp"

#In kết quả
print("--- KẾT QUẢ ---")
print(f"Khách hàng: {ten_khach_hang}")
print(f"Quãng đường: {quang_duong} km")
if loai_xe=="4 cho":
    print("4 chỗ")
else:
    print("7 chỗ")
print()
print(f"Cước cơ bản: {cuoc_co_ban} VND")
print(f"Phụ thu giờ cao điểm: {phi_gio_cao_diem} VND")
print(f"Phụ thu trời mưa: {phu_thu_mua} VND")
print(f"Tổng cước: {tong_cuoc} VND")

print(f"Loại chuyến đi: {loai_chuyen_di}")
print(f"Ưu tiên điều xe: {uu_tien_dieu_xe}")
print(f"Mức cước: {muc_cuoc}")


