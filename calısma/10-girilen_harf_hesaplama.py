# 1. YONTEM 
metin1 = input("Birinci metni giriniz")
harf1 = input("harf giriniz")
harf_sayisi1 = 0
for karakter in metin1:
    if karakter == harf1:
        harf_sayisi1 += 1  # harf_sayisi1 = harf_sayisi1 + 1 
        
print(harf_sayisi1)

#**********************************************************************
# 2. YONTEM

## eger kullanici harf yerine birden fazla karakter yada sayi girerse bunu kontrol etmek icin;
# Bunu while dongusuyle kontrol ederiz
# cunku kullanici dogru islemi girene kadar islem dongude kalir islemi basa alir.

metin2 = input("Ikinci metni giriniz: ")
harf_sayisi2 = 0
while True:
    harf2 = input("harf giriniz: ")
    if len(harf2) != 1 or not harf2.isalpha():
        print("Hatali islem, Tekrar deneyiniz..")
    else:
        for eleman in metin2:
            if eleman == harf2:
                harf_sayisi2 += 1
        break

print(harf_sayisi2)