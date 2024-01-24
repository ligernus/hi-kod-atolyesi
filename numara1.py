#numara1#
x = 3
x_degistir = float(x)
print(x_degistir)
print(type(x_degistir))
y = 4.5
y_degistir = int(y)
print(y_degistir)
print(type(y_degistir))
z = "8"
z_degistir = int(z)
print(z_degistir)
print(type(z_degistir))
a ="12"
a_degistir = float(a)
print(a_degistir)
print(type(a_degistir))
b= "46.8"
b_degistir = int(float(b))
print(b_degistir)
print(type(b_degistir))
#numara2#
emin=22
kaya=35
yasemin=18
if emin == yasemin:
    print(True)
else:
    print(False)
if emin < 35:
    print(True)    
#numara3#
final_notu = float(input("Final Notunu Giriniz: "))
vize_notu = float(input("Vize Notunu Giriniz: "))

toplam_not = final_notu + vize_notu

if toplam_not >= 50:
    print("Dersten Gectiniz")
else:
    print("Kaldiniz")
#numara4#
kullanici_adi = str(input("İsminizi Giriniz: "))
print(kullanici_adi)
kullanici_soyadi =str(input("Soyadini Giriniz: "))
print(kullanici_soyadi)
kullanici_yasi =int(input("Yasinizi Giriniz: "))
print(kullanici_yasi)
kullanici_yasadigi_sehir =str(input("Yasadiginiz Sehiri Yaziniz: "))
print(kullanici_yasadigi_sehir)
kullanici_meslegi =str(input("Meslek Bilgilerinizi Giriniz: "))
print(kullanici_meslegi)
#numara5#
atölye_ismi = "Hi-Kod Veri Bilimi Atölyesi"

# 1. İfadeden her bir kelimeyi seç#
kelimeler = atölye_ismi.split()

# 2. İfadenin tamamını büyük harfe çevir
buyuk_harfler = atölye_ismi.upper()

# 3. İfadenin tamamını küçük harfe çevir
kucuk_harfler = atölye_ismi.lower()

# "0123456789" ifadesindeki çift ve tek sayıları seç
sayilar = "0123456789"
cift_sayilar = sayilar[::2]  
tek_sayilar = sayilar[1::2] 

# Sonuçları yazdır
print("1. İfadeden Her Bir Kelime: ", kelimeler)
print("2. İfadenin Tamami Büyük Harf: ", buyuk_harfler)
print("3. İfadenin Tamami Küçük Harf: ", kucuk_harfler)
print("Çift Sayilar: ", cift_sayilar)
print("Tek Sayilar: ", tek_sayilar)