sayi = input("Bir Sayi Giirniz")

toplam= 0
for rakam in sayi:
    if rakam.isdigit():             # Eğer rakam sayısal bir karakterse
        toplam += int(rakam)        # Rakamı tam sayıya dönüştürüp toplama ekle
    else:
        print("hata")

print(toplam)       

# isdigit() bir string metodu olup, bir string'in sadece rakamlardan oluşup oluşmadığını kontrol eder.
#  Eğer string'deki tüm karakterler rakam ise True döner, 
# aksi takdirde False döner.
# y = "hello"
# print(isinstance(y, str))  ->  True çünkü y bir string




#isinstance() fonksiyonu, bir nesnenin belirli bir türde (class) olup olmadığını kontrol eder.
# Yani, bir nesnenin (örneğin bir değişkenin) belirli bir türde olup olmadığını sorgular.