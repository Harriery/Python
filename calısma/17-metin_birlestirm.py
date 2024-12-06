# Kullanıcıdan iki metin alıyoruz
metin1 = input("Birinci metni giriniz: ")
metin2 = input("İkinci metni giriniz: ")

# Metinleri birleştiriyoruz
birlesik_metin = metin1 + " " + metin2

# Birleştirilen metni kelimelere ayırıyoruz
kelimeler = birlesik_metin.split()

# Her kelimenin son harfini büyük yapıyoruz ve birleştiriyoruz
yeni_metin = " ".join([kelime[:-1] + kelime[-1].upper() for kelime in kelimeler])

# Yeni metni yazdırıyoruz
print("Yeni metin:", yeni_metin)

# [kelime[:-1] + kelime[-1].upper() for kelime in kelimeler]:

# Bu, bir list comprehension (listeyi bir satırda oluşturma) kullanarak, her kelimenin son harfini büyütmek için yazılmış bir ifadedir.

# kelime[:-1]:

# Bu, her kelimenin son harfi hariç tüm harflerini alır.
# Örneğin, "merhaba" kelimesi için kelime[:-1] kısmı "merhab" olur.
# kelime[-1].upper():

# Bu, her kelimenin son harfini alır ve büyük yapar.
# Örneğin, "merhaba" kelimesinin son harfi 'a''yı büyük yaparsak 'A' olur.
# Birleştirme: Bu ikisini birleştiriyoruz: kelime[:-1] + kelime[-1].upper().

# Örneğin, "merhaba" için bu işlem sonucu "merhabA" olur.