girilen_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_sayilar = []
tek_sayilar = []
for liste in girilen_liste:
    if liste % 2 == 0:
        cift_sayilar.append(liste)
    elif liste % 2 == 1:
        tek_sayilar.append(liste)
        
toplam_cift_sayilar = sum(cift_sayilar)        
print(toplam_cift_sayilar) # 30

toplam_tek_sayilar = sum(tek_sayilar)        
print(toplam_tek_sayilar) # 25