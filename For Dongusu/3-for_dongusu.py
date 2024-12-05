#yeni_liste = [ifade for eleman in mevcut_liste if koşul]

#Temel: [ifade for eleman in liste]
#Koşullu: [ifade for eleman in liste if koşul]
#Koşullu işlem: [ifade1 if şart else ifade2 for eleman in liste]


#Diyelim ki bir sayılar listemiz var ve bu sayıların karesini almak istiyoruz.

#Geleneksel Yöntem:
sayilar = [1, 2, 3, 4, 5]
kareler = []

for x in sayilar:
    kareler.append(x**2)

print(kareler)  # Çıktı: [1, 4, 9, 16, 25]

#Liste Oluşturma (List Comprehension):
sayilar = [1, 2, 3, 4, 5]
kareler = [x**2 for x in sayilar]

print(kareler)  # Çıktı: [1, 4, 9, 16, 25]

#3. Koşullu Liste Oluşturma:
sayilar = [1, 2, 3, 4, 5]
cift_kareler = []

for x in sayilar:
    if x % 2 == 0:  # Çift sayıları seç
        cift_kareler.append(x**2)

print(cift_kareler)  # Çıktı: [4, 16]

#Liste Oluşturma (List Comprehension):
sayilar = [1, 2, 3, 4, 5]
cift_kareler = [x**2 for x in sayilar if x % 2 == 0]

print(cift_kareler)  # Çıktı: [4, 16]

#Daha Karmaşık Bir Örnek:

#Çift sayılarda kare alalım.
#Tek sayılarda küp alalım.
sayilar = [1, 2, 3, 4, 5]
islem = [x**2 if x % 2 == 0 else x**3 for x in sayilar]

print(islem)  # Çıktı: [1, 4, 27, 16, 125]

#Eğer sayı çiftse (x % 2 == 0), x**2 listeye eklenir.
#Eğer sayı tekse, x**3 listeye eklenir.


# ** us alma 
# % bir sayinin baska nir sayiya bolumunden kalani bulmak icin kullanilir. 
# sayi % 2 == 0 cift sayi