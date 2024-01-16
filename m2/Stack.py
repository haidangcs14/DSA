class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, item):
        self.items.append(item)
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack underflow")
        else:
            item = self.items.pop()
            self.top -= 1
            return item

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty")
        else:
            return self.items[self.top]

    def isEmpty(self):
        return self.top == -1

    def size(self):
        return self.top + 1


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def displayInfo(self):
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}"


students_stack = Stack()

students_stack.push(Student("Hai Dang", 23, "Quang Tri"))
students_stack.push(Student("Phuong Anh", 20, "Thai Nguyen"))
students_stack.push(Student("Nguyen Van A", 25, "Ha Noi"))
i = 1
while not students_stack.isEmpty():
    print(f'----Thong tin sinh vien thu {i}---------')
    print(students_stack.peek().displayInfo())
    students_stack.pop()
    i += 1