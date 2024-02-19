#Hafta4-Ödev2-4.Kısım-1
def kullaniciadi_belirle():  
    kk=str(input("Kullanıcı Adını Giriniz: "))
    print("Kullanıcı Adınızı Oluşturdunuz ",kk)
kullaniciadi_belirle()    
def sifre_belirle():
    while True:
     kk_sifre=input("Sifrenizi Belirleyiniz: ")
     if 5<len(kk_sifre)<10:
        print("Şifreniz Oluşturuldu")
        return kk_sifre
     else:
        print("şifrenizi tekrardan oluşturun ")
sifre_belirle()
def giris():
        girilen_kk=kullaniciadi_belirle()
        girilen_sifre=sifre_belirle()
        dogru_kk=girilen_kk
        dogru_sifre=girilen_sifre
        if girilen_kk ==dogru_kk and girilen_sifre ==dogru_sifre:
                print("Giriş Başarılı")
        else:
                print("Kullanıcı Adınızı veya Şifrenizi yanlış girdiniz.")
giris()                        
