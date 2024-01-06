'''
Cho một danh sách sinh viên như sau

Index   Name            Age Class
0       Nguyễn Văn A    10  5D4
1       Nguyễn Văn B    9   4C3
2       Nguyễn Văn D    8   3B2
3       Nguyễn Văn D    7   2A1

Tái sử dụng cấu trúc dữ liệu sinh viên trong bài tập phần trước.
Thực hiện các việc sau:
Tạo mảng danh sách sinh viên
Thêm sinh viên vào mảng theo chỉ mục như ở trên
In toàn bộ danh sách sinh viên ra màn hình
Tìm kiếm sinh viên có tên là  Nguyễn Văn A và in thông tin sinh viên đó ra màn hình.
Tìm sinh viên nhiều tuổi nhất và in ra màn hình
Tìm sinh viên ít tuổi nhất và in ra màn hình
Đổi chỗ sinh viên có chỉ số 0 với sinh viên cho chỉ số 3. In lại mảng ra màn hình.
'''
class Student:
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    def display_info(self):
        print(f"Name: {self.name} - Age: {self.age} - Class: {self.class_}")

# Tạo mảng danh sách sinh viên
student_list = []

# Thêm sinh viên vào mảng theo chỉ mục
student_list.append(Student("Nguyễn Văn A", 10, "5D4"))
student_list.append(Student("Nguyễn Văn B", 9, "4C3"))
student_list.append(Student("Nguyễn Văn D", 8, "3B2"))
student_list.append(Student("Nguyễn Văn D", 7, "2A1"))

# In toàn bộ danh sách sinh viên ra màn hình
print("----------Danh sách sinh viên-----------")
for student in student_list:
    student.display_info()

# Tìm kiếm sinh viên có tên là Nguyễn Văn A và in thông tin sinh viên đó ra màn hình
print("\nThông tin sinh viên có tên là Nguyễn Văn A:")
for student in student_list:
    if student.name == "Nguyễn Văn A":
        student.display_info()

# Tìm sinh viên nhiều tuổi nhất và in ra màn hình
oldest_student = max(student_list, key=lambda s: s.age)
print(f"\nSinh viên nhiều tuổi nhất:")
oldest_student.display_info()

# Tìm sinh viên ít tuổi nhất và in ra màn hình
youngest_student = min(student_list, key=lambda s: s.age)
print(f"\nSinh viên ít tuổi nhất:")
youngest_student.display_info()

# Đổi chỗ sinh viên có chỉ số 0 với sinh viên cho chỉ số 3
student_list[0], student_list[3] = student_list[3], student_list[0]

# In lại mảng ra màn hình
print("\nDanh sách sinh viên sau khi đổi chỗ:")
for student in student_list:
    student.display_info()