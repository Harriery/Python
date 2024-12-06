# YONTEM 1
toplam = 0
while True:
    sayi1 = int(input("Birinci sayiyi giriniz: "))
    sayi2= int(input("Ikinci sayiyi giriniz: "))
    kucuk_sayi = min(sayi1, sayi2)
    buyuk_sayi = max(sayi1, sayi2)
    liste =  list(range(kucuk_sayi +1, buyuk_sayi))
    if sayi1 != 
    for sayi in liste:
        toplam += sayi
    break
print(liste)
print(toplam)




# min() Fonksiyonu:
# Birden fazla sayı ya da değer arasından en küçük olanı bulur.
# kucuk_sayi = min(sayi1, sayi2) min(3, 7) 

# max() Fonksiyonu:
# Birden fazla sayı ya da değer arasından en büyük olanı bulur.
# buyuk_sayi = max(sayi1, sayi2)

# liste =  list(range(kucuk_sayi +1, buyuk_sayi)) 
# list() fonk listeye cevirir 
#range(start, stop):
# start: Hangi sayıdan başlayacağını belirtir.
# stop: Hangi sayıya kadar gideceğini belirtir (dahil değil).
# Eğer iki sayı arasındaki değerleri dahil etmek istiyorsak, stop değerini büyük_sayı + 1 yaparız.

# print(range(3, 8))  # Çıktı: range(3, 8)
# print(list(range(3, 8)))  # Çıktı: [3, 4, 5, 6, 7]

