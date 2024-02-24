#Hafta5-Ödev2-1.Kısım
#1#
liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
print("3. indexdeki ifade: {}".format(liste[3]))
#2#
liste=["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
for i in range(len(liste)):
    if liste[i]=="False":
        break
    print("{} .indexdeki ifade: {}".format(i,liste[i]))
#3#
for i in range(len(liste)):
    if liste[i]=="4.7":
        break
    print("{} .indexdeki ifade: {}".format(i,liste[i]))    
#4#    
alt_liste=liste[2:6]
print(alt_liste)
#5#
yeni_list=liste[4:8]
print(yeni_list)