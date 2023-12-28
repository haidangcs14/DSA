def kiem_tra_so_chan(a):
    if a % 2 == 0:
        return True
    else:
        return False

a = int(input('Nhập a: '))

if kiem_tra_so_chan(a):
    print(f"{a} là số chẵn.")
else:
    print(f"{a} là số lẻ")