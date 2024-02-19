#Hafta4-Ödev2-4.Kısım-2
def kullaniciadi_belirle():  
    kk=str(input("Kullanıcı Adını Giriniz: "))
    print("Kullanıcı Adınızı Oluşturdunuz ",kk)
    return kk
   
def sifre_belirle():
    while True:
     kk_sifre=input("Sifrenizi Belirleyiniz: ")
     if 5<len(kk_sifre)<10:
        print("Şifreniz Oluşturuldu")
        return kk_sifre
     else:
        print("şifrenizi tekrardan oluşturun ")

def giris():
     girilen_kk=kullaniciadi_belirle()
     girilen_sifre=sifre_belirle()
     giris_hakki=3
     while giris_hakki>0:
        dogru_kk=input("Kullanici Adini Doğrulamak Adına Tekrar Giriniz: ")
        dogru_sifre=input("Doğru Şifrenizi Doğrulamak Amacıyla Tekrar Giriniz: ")
        if girilen_kk ==dogru_kk and girilen_sifre ==dogru_sifre:
                print("Giriş Başarılı")
                break
        else:
                giris_hakki -=1
                if giris_hakki==0:
                        print("Üç Kez yalnız girdiniz belirli süre sonra tekrar deneyiniz.")
                else:
                        print("Kullanıcı Adınızı veya Şifrenizi yanlış girdiniz.",giris_hakki)
giris()                        
