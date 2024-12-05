# Kullanıcıdan cümle al
cumle = input("Bir cümle girin: ")

# Cümleyi kelimelere ayırir ve bir liste olusturur (boşluklara göre)
kelimeler = cumle.split()

# Her bir kelimenin uzunluğunu hesapla ve bir listeye kaydet
kelime_uzunluklari = [len(kelime) for kelime in kelimeler]

#*******************************************************************
kelime_uzunluklari = []  # Boş bir liste oluştur
for kelime in kelimeler:  # 'kelimeler' listesindeki her bir 'kelime' üzerinde dön
    uzunluk = len(kelime)  # 'kelime'nin uzunluğunu hesapla
    kelime_uzunluklari.append(uzunluk)  # Uzunluğu listeye ekle
# Sonucu ekrana yazdır
print("Her kelimenin uzunluğu:", kelime_uzunluklari)
#******************************************************************
# pythonda ogrenecek cok konu var.
# [8, 9, 3, 4, 4]



metin = "Python öğrenmek eğlenceli"
kelimeler = metin.split()
print(kelimeler)
['Python', 'öğrenmek', 'eğlenceli']

# Cümledeki kelimeler boşluklara göre ayrıldı.
# Sonuç olarak, her kelime bir liste elemanı haline geldi.

metin = "elma,armut,çilek,kiraz"
meyveler = metin.split(',')  # Virgüle göre böl
print(meyveler)