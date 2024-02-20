#Hafta5-Ödev1-4.Kısım
isim=(input("İsminizi Giriniz: "))
print("İsim:",isim)
def dogum_günü():
    dogum_yili=int(input("Dogum Yılını Giriniz: "))
    sonuc=2024-dogum_yili
    print("Yaşınız:",sonuc)
    emeklilik=65-sonuc
    if sonuc>=65:
        print("Emekli Oldunuz")
    else:
        print("Emekli Olmanıza Şu Kadar Yıl Kaldı:",emeklilik,isim)
    
dogum_günü()
