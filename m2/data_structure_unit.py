class Student:
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    def display_info(self):
        print(f"Name: {self.name} - Age: {self.age} - Class: {self.class_}")


# Create a student
s = Student("Nguyễn Văn A", 6, "1A3")

# display information about student
s.display_info()

# change class name: 1A7
s.class_ = "1A7"

# display information about student
s.display_info()

#delete student
try:
    del s
    print("Delete successfully!")
except:
    print(f"Error")