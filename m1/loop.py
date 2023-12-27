# Lesson 1: Print multiplication table
def l1():
    for i in range(1, 11):
        print("-----Bảng cửu chương {}-----".format(i))

        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

        print('\n')
# l1()
# Lesson 2: Factorial
def l2():
    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result = result * i
        return result

    n = int(input("Nhập n: "))
    while n < 0:
        print(f"Nhập n nguyên dương. Nhập lại!")
        n = int(input("Nhập n: "))

    print(f"{n}! = {factorial(n)}")
# l2()
# Lesson 3: Prime numbers
def l3():
    def prime_num(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    for i in range(1, 100):
        if prime_num(i):
            print(f"{i}", end=' ')
# Lesson 4: Sum of even numbers
def l4():
    n = int(input("Nhập n: "))
    while n < 0:
        print(f"Nhập n nguyên dương. Nhập lại!")
        n = int(input("Nhập n: "))
    result = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            result += i
    print(f"Tổng các số chẵn từ 1 đến {n}: {result}")
# Lesson 5: Print a triangle
def l5():
    n = int(input("Nhập n: "))
    while n < 0:
        print(f"Nhập n nguyên dương. Nhập lại!")
        n = int(input("Nhập n: "))
    for i in range(1, n + 1):
        for j in range(1, n + 1 - i):
            print("", end=" ")
        for k in range(1, i + 1):
            print("*", end=" ")
        print()
l5()




