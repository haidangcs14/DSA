# Lesson 4: Sum of even numbers
n = int(input("Nhập n: "))
while n < 0:
    print(f"Nhập n nguyên dương. Nhập lại!")
    n = int(input("Nhập n: "))
result = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        result += i
print(f"Tổng các số chẵn từ 1 đến {n}: {result}")