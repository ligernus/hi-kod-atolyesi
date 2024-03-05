#Hafta6-Ödev2-1.Kısım
import numpy as np
a=np.array([1,2,3,4,5,6],dtype="int")
print(a)
print(a.ndim)
print(a.size)
#Hafta6-Ödev2-2.Kısım
iki_boyutlu=np.array([[1,2,3,4],[6,7,8,9]])
print(iki_boyutlu.size)
print(np.shape(iki_boyutlu))
uc_boyutlu=np.array([[[11,12,44],[55,70,99]]])
print(uc_boyutlu.size)
print(np.shape(uc_boyutlu))
#Hafta6-Ödev2-3.Kısım
#İki boyutlu arraydaki 7 elemanına ulaşalım
print(iki_boyutlu[0,3])
#Üç boyutlu arraydaki 5 elemanına ulaşalım
print(uc_boyutlu[0,0,1])
deneme=np.array([[[ 7,  5, 14],[21,  8, 11]],[[ 8,  6, 20],[14,  3,  9]]])
#8 ve 11 i bulalım.
print(deneme[0,1,1])
print(deneme[0,1,2])
#Hafta6-Ödev2-4.Kısım
sifir=np.zeros((5,3),dtype="int")
print(sifir)
bir=np.ones((5,3),dtype="int")
print(bir)
#satır bazında birleştirme
print(np.concatenate([sifir,bir],axis=0))
#sütun bazında birleştirme
print(np.concatenate([sifir,bir],axis=1))