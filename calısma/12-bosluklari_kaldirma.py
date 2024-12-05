metin = input("Bir metin giriniz: ")

son_metin = ""

for karakter in metin:
    if karakter != " ":
        son_metin += karakter
    

print(son_metin)
#Bu metni kontrol et
#Bumetnikontrolet



# strip(): Baş ve sondaki boşlukları kaldırır.
# lstrip(): Sadece baştaki boşlukları kaldırır.
# rstrip(): Sadece sondaki boşlukları kaldırır.


#****************************
# son_metin += karakter           ->   sona ekleme yapar. 
# merhaba  -> cikti:merhaba

# son_metin = karakter + son_metin  -> her yeni karakteri bir onceki karakterin basina ekler.
# merhaba  -> abahrem 

# += operatörü, metni sondan ekler ve böylece sıralı bir metin oluşturur.
# = karakter + son_metin operatörü, her yeni karakteri başına ekler ve bu da metni tersine çevirmiş olur.