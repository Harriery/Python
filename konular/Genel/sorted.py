# Listelerde: Elemanları sıralar ve sıralanmış bir liste döner.
# Stringlerde: Her bir karakteri sıralar ve bir liste döner. Birleştirmek isterseniz join() kullanabilirsiniz.
# Diğer iterable veri tiplerinde (tuple, set, dictionary) de çalışır.
# Önemli Not:
# sorted() orijinal veriyi değiştirmez, sıralanmış yeni bir liste oluşturur. Eğer veriyi yerinde sıralamak istiyorsanız, listelerde .sort() kullanabilirsiniz.

# sorted() Listede Kullanımı: 
sayilar = [3, 1, 4, 2]
print(sorted(sayilar))  # Çıktı: [1, 2, 3, 4]
print(sayilar)          # Orijinal liste: [3, 1, 4, 2]


sayilar = [3, 1, 4, 2]
print(sorted(sayilar, reverse=True))  # Çıktı: [4, 3, 2, 1]

# sorted() Stringlerde Kullanımı 

kelime = "python"
print(sorted(kelime))        # Çıktı: ['h', 'n', 'o', 'p', 't', 'y']
print("".join(sorted(kelime)))  # Çıktı: "hnopty" (string olarak birleştirdik)
