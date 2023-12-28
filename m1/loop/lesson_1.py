# Lesson 1: Print multiplication table

for i in range(1, 11):
    print("-----Bảng cửu chương {}-----".format(i))

    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

    print('\n')