# Lesson 3: Prime numbers
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