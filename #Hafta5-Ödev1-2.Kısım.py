#Hafta5-Ödev1
def faktoriyel(n):
    faktoriyel_degeri = 1
    for i in range(1, n + 1):
        faktoriyel_degeri *= i
    return faktoriyel_degeri

sayi = int(input("Faktöriyelini Hesaplamak istediğiniz sayıyı girin: "))

sonuc = faktoriyel(sayi)

print("{} sayısının faktöriyeli: {}".format(sayi, sonuc))
