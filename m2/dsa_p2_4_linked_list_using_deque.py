from collections import deque

class Student:
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    def display_info(self):
        print(f"Name: {self.name} - Age: {self.age} - Class: {self.class_}")

# Tạo danh sách liên kết sinh viên
student_list = deque()

# Thêm sinh viên vào danh sách liên kết theo vị trí
student_list.append(Student("Nguyễn Văn A", 10, "5D4"))
student_list.append(Student("Nguyễn Văn B", 9, "4C3"))
student_list.append(Student("Nguyễn Văn D", 8, "3B2"))
student_list.append(Student("Nguyễn Văn D", 7, "2A1"))

# In thông tin sinh viên đầu tiên
print("Thông tin sinh viên đầu tiên:")
student_list[0].display_info()

# In thông tin sinh viên cuối cùng
print("\nThông tin sinh viên cuối cùng:")
student_list[-1].display_info()

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
oldest_student = max(student_list, key=lambda x: x.age)
print(f"\nSinh viên nhiều tuổi nhất:")
oldest_student.display_info()

# Tìm sinh viên ít tuổi nhất và in ra màn hình
youngest_student = min(student_list, key=lambda x: x.age)
print(f"\nSinh viên ít tuổi nhất:")
youngest_student.display_info()

# Đổi chỗ sinh viên có vị trí 0 với sinh viên ở vị trí 3
student_list[0], student_list[3] = student_list[3], student_list[0]

# In lại danh sách liên kết ra màn hình
print("\nDanh sách sinh viên sau khi đổi chỗ:")
for student in student_list:
    student.display_info()
