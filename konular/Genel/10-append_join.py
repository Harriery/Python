#1. append Nedir?
# append, listelerle çalışır ve bir listeye yeni bir eleman eklemek için kullanılır.
# Bu yöntem, listeyi yerinde (in-place) günceller, yani orijinal liste değişir.
# Kullanımı:

# Örnek
liste = [1, 2, 3]
liste.append(4)
print(liste)  # Çıktı: [1, 2, 3, 4]
# Anahtar Nokta:
# append sadece tek bir eleman ekler.
# Eğer birden fazla eleman eklemek isterseniz, ya extend kullanırsınız ya da bir döngü ile append yaparsınız.

# 2. join Nedir?
# join, stringlerle çalışır ve birden fazla stringi birleştirmek için kullanılır.
# join, bir liste veya tuple içindeki string elemanları, belirtilen bir ayırıcı (separator) ile birleştirerek yeni bir string oluşturur.
# Bu yöntem orijinal listeyi değiştirmez; sadece yeni bir string döndürür.


# Kullanımı:
# Örnek
kelimeler = ["Merhaba", "dünya"]
cumle = " ".join(kelimeler)
print(cumle)  # Çıktı: "Merhaba dünya"

# join sadece string elemanlar içeren bir iterable (örneğin liste, tuple) ile çalışabilir.
# String elemanları birleştirirken, bir ayırıcı kullanabilirsiniz (örneğin boşluk, virgül, tire).


# Farkları Özetlersek:
# 	                         append	                                join
# Amaç	                 :   Bir listeye yeni eleman eklemek	    String elemanları birleştirmek
# Çalıştığı veri tipi	 :   Liste	                                String (liste, tuple gibi iterable)
# Sonuç                  :   Liste güncellenir	                    Yeni bir string döndürür
# Kullanım Yeri	         :   Listeyi genişletmek	                Metin birleştirme işlemleri
# 
# 
# Birlikte Örnek:
# Aynı yapı üzerinde hem append hem join kullanırsak nasıl farklı davrandıklarını daha iyi görebiliriz.

# Örnek:
# Listeye eleman ekleme (append)
kelimeler = ["Python", "programlama"]
kelimeler.append("dili")
print(kelimeler)  # Çıktı: ['Python', 'programlama', 'dili']

# String birleştirme (join)
cumle = " ".join(kelimeler)
print(cumle)  # Çıktı: "Python programlama dili"