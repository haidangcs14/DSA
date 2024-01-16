class Queue:
    def __init__(self):
        self.items = []
        self.front = 0
        self.rear = -1
    def isEmpty(self):
        return self.front > self.rear
    def enqueue(self, item):
        self.items.append(item)
        self.rear += 1
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            item = self.items[self.front]
            self.front += 1
            return item
    def peek(self):
        if self.isEmpty():
            raise Exception("Empty")
        else:
            return self.items[self.front]

class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def displayInfo(self):
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}"


students_queue = Queue()

students_queue.enqueue(Student("Hai Dang", 23, "Quang Tri"))
students_queue.enqueue(Student("Phuong Anh", 20, "Thai Nguyen"))
students_queue.enqueue(Student("Nguyen Van A", 25, "Ha Noi"))

i = 1
while not students_queue.isEmpty():
    print(f'----Thong tin sinh vien thu {i}---------')
    print(students_queue.peek().displayInfo())
    students_queue.dequeue()
    i += 1