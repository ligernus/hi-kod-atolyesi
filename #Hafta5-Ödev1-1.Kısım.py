#Hafta5-Ödev1
pi = float(input("Pi Değerini Giriniz: "))
yaricap = float(input("Yarıçap Değerini Giriniz: "))

def dairenin_alani():
    alan = pi * (yaricap ** 2)
    print("Dairenin alanı:", alan)

dairenin_alani()
