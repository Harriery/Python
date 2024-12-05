# 1. yontem
metin = input("Birinci metni giriniz: ")
ters_metin = ""

for ters in metin:
    ters_metin = ters + ters_metin

print(ters_metin)    # Hala burdamisin ->   nisimadrub alaH

# Bu satır, her seferinde ters karakterini ters_metin adlı string'in başına ekler.
# İlk adımda, ters = 'a'
# İkinci adımda, ters = 'b'
# Üçüncü adımda, ters = 'c'

# 2. yontem
metin = input(" ikinci metni giriniz: ")
ters_metin = ''.join(reversed(metin))  # reversed() kullanımı ve birleştirme
print(ters_metin) # bu kod calisiyor -> royisilac dok ub


# reversed(metin): Metni ters çevirir.
# ''.join(): Ters çevrilmiş karakterleri birleştirip string yapar.

# '' (boş string) burada birleştirici (separator) olarak kullanılır. 
# Yani, join() birleştirirken karakterlerin arasına bir şey eklemeyecek.
# Örn:
# ''.join(['a', 'b', 'c']) → "abc" olur (karakterler arasına bir şey eklenmez).
# Eğer '-'.join(['a', 'b', 'c']) yazsaydık, sonuç "a-b-c" olurdu (karakterler arasına '-' eklenir).