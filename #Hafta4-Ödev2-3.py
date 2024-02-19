#Hafta4-Ödev2-3.Kısım
kk=str(input("Kullanıcı Adını Giriniz: "))
print("Kullanıcı Adınızı Oluşturdunuz ",kk)
def sifre_belirle():
    while True:
     kk_sifre=input("Sifrenizi Belirleyiniz: ")
     if 5<len(kk_sifre)<10:
        print("Şifreniz Oluşturuldu")
        break
     else:
        print("şifrenizi tekrardan oluşturun ")
sifre_belirle()