#Viết hàm nhập từ bàn phím và hiển thị ra màn hình danh sách hai chiều kích thước MxN.
def NhapDanhSach(m,n):
   DS = []
   for i in range(m):
      hang = input("Nhap vao hang thu.{}: ".format(i)).split()
      if len(hang) != n:
         print("Vui long nhap dung kich thuoc")

         return None
      DS.append(hang)
   return DS

def InDanhSach(s):
   for i in s:
      print(*i)


try:
   m,n = map(int,input("nhap vao danh sach MxN:").split())
   if m <= 0 or n <= 0:
      print("Vui long nhap so nguyen duong")
   else:
      DanhSach = NhapDanhSach(m,n)
      InDanhSach(DanhSach)
      
except:
   print("Dinh dang dau vao khong hop le")