#Hafta7-Ödev1
import pandas as pd
sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
         "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
         "Fiyat" : [300,180,450,50,700,400,150,80,850,900]}
sozluk_pd=pd.DataFrame(sozluk)
print(sozluk_pd)
# 2.indexte bulunan kategori bulunur. (Sadece kategori bilgisi) 
print(sozluk_pd.loc[2,"Kategori"])
print(sozluk_pd.iloc[2,0])
# 2. indexte bulunan ürün bulunur. (Sadece ürün bilgisi) 
print(sozluk_pd.loc[2,"Ürün"])
print(sozluk_pd.iloc[2,1])
#  4.indexten 9.indexe kadar olan veriler bulunur. (Kategori,ürün,fiyat bilgisi beraber)
print(sozluk_pd.loc[4:8,"Kategori":"Fiyat"])
print(sozluk_pd.iloc[4:9,:])
#iloc son indexi dahil etmez iken loc son indexi dahil eder.
# 1.indexten 6.indexe kadar olan ürünler bulunur. (Sadece ürün bilgisi) 
print(sozluk_pd.loc[1:5,"Ürün"])
print(sozluk_pd.iloc[1:6,1])

#Giyim kategorisinde bulunan ürünler gösterilir. 
print(sozluk_pd[sozluk_pd["Kategori"]=="Giyim"][["Kategori","Ürün"]])
#Ayakkabı kategorisinde bulunan ürünler gösterilir. 
print(sozluk_pd[sozluk_pd["Kategori"]=="Ayakkabı"][["Ürün"]])
#Aksesuar kategorisinde bulunan ürünler gösterilir. 
print(sozluk_pd[sozluk_pd["Kategori"]=="Aksesuar"][["Ürün"]])
#Giyim kategorisinde fiyatı 300'den fazla olan ürünler gösterilir. 
print(sozluk_pd[(sozluk_pd["Kategori"]=="Giyim") & (sozluk_pd["Fiyat"]>300)])
#Ayakkabı kategorisinde fiyatı 600'den az olan ürünler gösterilir.
print(sozluk_pd[(sozluk_pd["Kategori"]=="Ayakkabı") & (sozluk_pd["Fiyat"]<600)])
#Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuar gösterilir.
print(sozluk_pd[(sozluk_pd["Kategori"]=="Aksesuar") & (sozluk_pd["Fiyat"]>100)])