print("Yapabileceğiniz işlemler: ")
print("+, -, *, /")


ilk_sayi = int(input("İlk sayınızı giriniz: "))
ikinci_sayi = int(input("İkinci sayınızı giriniz: "))
secilen_islem = input("İstediğiniz işlemi seçiniz: ")

if secilen_islem == "+":
    print(f"Sonuç: {ilk_sayi + ikinci_sayi}")
elif secilen_islem == "-":
    print(f"Sonuç: {ilk_sayi - ikinci_sayi}")
elif secilen_islem == "*":
    print(f"Sonuç: {ilk_sayi * ikinci_sayi}")
elif secilen_islem == "/":
    if ikinci_sayi != 0:
        print(f"Sonuç: {ilk_sayi / ikinci_sayi}")
    else :
        print("Hatalı sayı seçimi yaptınız")


