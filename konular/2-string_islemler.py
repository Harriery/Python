Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> karakter = "Python ogreniyorum"
>>> print(karakter)
Python ogreniyorum
>>> karakter[0]
'P'
>>> karakter[1]
'y'
>>> karakter[5]
'n'
>>> karakter[-1]
'm'
>>> karakter[-2]
'u'
>>> karakter[-3]
'r'
>>> karakter[0:5]
'Pytho'
>>> karakter[0:6]
'Python'
>>> karakter[3:9]
'hon og'
>>> karakter[7:]
'ogreniyorum'
>>> karakter[:6]
'Python'
>>> len(karakter)
18
>>> len(karakter[:6])
6

metin = "Merhaba"

# Başlangıçtan sonuna kadar her 2. karakteri almak
print(metin[::2])  # Çıktı: "Mrba"

# 2. indeksten sonra her 3. karakteri almak
print(metin[2::3])  # Çıktı: "rb"

liste = [1, 2, 3, 4, 5]
ters_liste = liste[::-1]
print(ters_liste)  # Çıktı: [5, 4, 3, 2, 1]

# [::-1] ifadesi bir string veya listeyi tersine çevirmek için kullanılan kısa bir yazımdır.
# Bu yazım dilimleme (slicing) işlemiyle ilgili olup, adım olarak -1 kullanarak sıralamayı tersine çevirir.