# Lesson 2: Factorial
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