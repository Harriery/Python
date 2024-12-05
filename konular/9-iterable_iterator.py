# 1. Iterable Nedir?
# Iterable, üzerinde döngüyle gezilebilen bir şeydir. İçindeki elemanları sırasıyla alabileceğimiz bir veri yapısıdır.

# Örnek:
# Bir kitap koleksiyonu düşün.
# Kitaplar rafta sıralı duruyor. Bu koleksiyon, iterable bir yapıdır çünkü bu raftaki kitaplara sırayla bakabiliriz.

# 2. Iterator Nedir?
# Iterator, iterable bir nesneden elemanları teker teker almanızı sağlayan bir araçtır.

# Örnek:
# Bir kitap koleksiyonundan sırayla kitapları alıp incelemek istiyoruz.
# Iterator, kitapları raftan tek tek alan bir mekanizma gibidir.
# Her kitap alındığında, sıradaki kitaba geçilir.

# Nasıl Çalışırlar?
# Iterable, bir koleksiyon gibidir. (örneğin: liste, string, tuple, range)
# Iterator, bu koleksiyondan elemanları sırayla "çekebilen" bir araçtır.
# Bir iterable'ı iterator'a dönüştürmek için Python'da iter() fonksiyonu kullanılır.

# Iterable	                                Iterator
# Döngüyle üzerinde gezilebilir.	        Elemanları birer birer alır.
# Örneğin, listeler, string'ler.	        Örneğin, iter(liste) ile elde edilen şey.
# for döngüsünde direkt kullanılabilir.	    next() fonksiyonuyla eleman alınır.
# İçinde tüm elemanlar durur.	            Her elemanı aldıktan sonra sıradakine geçer.

# Iterable: Bir liste
kitaplar = ["Kitap 1", "Kitap 2", "Kitap 3"]

# Iterator: iter() ile iterator oluşturulur

kitap_iterator = iter(kitaplar)
 #object at 0xXXXXXXXX: Bu, iterator'un bellekteki adresini (memory address) gösterir. 
 # Bu adres Python için önemlidir ama bizim için genellikle kullanışlı değildir.

# Elemanları teker teker sirayla alabiliriz
print(next(kitap_iterator))  # Çıktı: Kitap 1
print(next(kitap_iterator))  # Çıktı: Kitap 2
print(next(kitap_iterator))  # Çıktı: Kitap 3


# Python, for döngüsü içinde iter() ve next() işlemlerini otomatik yapar
for kitap in kitaplar:
    print(kitap)
# Kitap 1
# Kitap 2
# Kitap 3