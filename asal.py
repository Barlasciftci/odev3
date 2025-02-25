def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5)+1):
        if sayi % i == 0:
            return False
    return True


sayi = int(input("Ilk sayinizi giriniz: "))
if asal_mi(sayi):
    print(f"Bu sayı asaldır {sayi}")
else:
    print(f"Bu sayı asal değildir {sayi}")