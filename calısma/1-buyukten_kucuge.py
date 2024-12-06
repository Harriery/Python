liste = [56, 'rmzoe', 86, 97, 'icwxm', 'mpcsn', 'lbgoa', 48, 'qdvch', 'sgzbd', 'ukedp', 32, 41, 'yhkji', 68,
'vnmwt', 52, 'knawt', 53, 74]

int_liste = [x for x in liste if isinstance(x, int)]


#Bir listeyi kucukten buyuge siralarken sorted() kullanilir.
int_sirala_kucukten_buyuge = sorted(int_liste)
print(int_sirala_kucukten_buyuge)  # = [32, 41, 48, 52, 53, 56, 68, 74, 86, 97] 


#Bir listeyi  buyukten kucuge siralarken sorted(x , reserve=True) kullanilir.
#  reserve = True parametrenin siralamanin tersine cevrilmesini saglar.
int_sirala_buyukten_kucuge = sorted(int_liste, reverse=True)
print(int_sirala_buyukten_kucuge) #[97, 86, 74, 68, 56, 53, 52, 48, 41, 32]


# [x for x in ...]: Bu, Python'da liste oluşturma (list comprehension) yöntemidir. int olan elemanları yeni bir listeye koyar.
# for x in liste: Listenin her bir elemanını sırayla alır ve x değişkenine koyar.
# if isinstance(x, int): Her elemanın türünü kontrol eder.
#  Eğer eleman int türündeyse (yani bir sayıysa), bu elemanı alır.