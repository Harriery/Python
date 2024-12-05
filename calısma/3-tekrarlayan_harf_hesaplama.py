# Kullanıcıdan bir cümle al
cumle = input("Bir cümle girin: ")

# Boş bir sözlük oluştur
harf_sayilari = {}

# Cümledeki her bir harf üzerinde dön
for harf in cumle:
    if harf != " ":  # Boşlukları sayma
        if harf in harf_sayilari:  # Harf sözlükte zaten varsa
            harf_sayilari[harf] += 1  # Sayısını 1 artır
        else:
            harf_sayilari[harf] = 1  # Sözlüğe ekle ve sayısını 1 yap

# Sonucu ekrana yazdır
print("Her harfin tekrar sayısı:", harf_sayilari)




#Bir sözlükteki bir anahtara karşılık gelen değere erişmek için köşeli parantezler [] kullanılır.
harf_sayilari = {'a': 2, 'b': 3, 'c': 1}
# 'a' anahtarı, 2 değerine sahiptir.

harf_sayilari.get(harf, 0) + 1

# harf_sayilari.get(harf, 0): 
# harf anahtarını sözlükte arar. Eğer harf anahtarı sözlükte yoksa, 0 döndürür. 
# Eğer anahtar varsa, o harfin mevcut sayısını döndürür.

# harf_sayilari[harf] = harf_sayilari.get(harf, 0) + 1: 
# Eğer harf anahtarı sözlükte varsa, o harfin sayısını 1 artırır. 
# Eğer yoksa, ilk defa görüldüğü için sayıyı 1 yapar.