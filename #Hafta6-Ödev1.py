#Hafta6-Ödev1-1.Kısım
ogrenci_bilgileri={"emin kaya":{"matematik":"100","kimya":"100","fizik":"100"}
                   ,"yasemin kaya":{"matematik":"100","kimya":"100","fizik":"100"}}
isim=input("Öğrencinin adı soyadını giriniz: ")
bilgi_almak_istediğiniz_dersi_giriniz=input("Hangi Ders: ")
#Hafta6-Ödev1-2.Kısım
ogrenci_bilgileri["emin kaya"]["fizik"]=80
ogrenci_bilgileri["hoca ahmet yesevi"]={"matematik":"50","kimya":"50","fizik":"60"}
if isim in ogrenci_bilgileri and bilgi_almak_istediğiniz_dersi_giriniz in ogrenci_bilgileri[isim]:
        print(ogrenci_bilgileri[isim][bilgi_almak_istediğiniz_dersi_giriniz])
else:
        print("Belirtilen Ders veya Öğrenci bulunamadı!")

yeni_ogrenci_bilgileri=input("Yeni Öğrencinin adını soyadını giriniz: ")
yeni_dersler=input("Hangi dersleri alıyor:").split(",") 
yeni_notlar=input("Aldığı derslerin notlarını sırayla giriniz: ").split(",")
ogrenci_bilgileri[yeni_ogrenci_bilgileri] = {ders: int(notlar) for ders, notlar in zip(yeni_dersler, yeni_notlar)}
print("Güncellenmiş öğrenci bilgileri: ")
print(ogrenci_bilgileri)         

                   
