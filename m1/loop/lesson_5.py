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