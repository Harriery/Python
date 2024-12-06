def sayi_okunusu(sayi):
    # Sayıyı string'e dönüştürüp her basamağını tek tek alınir
    sayi_str = str(sayi)
    
    # Basamağa karşılık gelen kelimeler
    basamak_kelimeleri = {
        "0": "sıfır", "1": "bir", "2": "iki", "3": "üç", "4": "dört",
        "5": "beş", "6": "altı", "7": "yedi", "8": "sekiz", "9": "dokuz"
    }
    okunus =[]
    # Her basamağı okuyor ve karşılık gelen kelimeleri listeye ekliyoruz
    for basamak in sayi_str:
        okunus.append(basamak_kelimeleri[basamak])
    
    # Listeyi birleştirip sonucu döndürüyoruz
    return " ".join(okunus)

# Kullanıcıdan sayıyı alıyoruz
sayi = int(input("Bir sayı giriniz: "))

# Sayının okunuşunu yazdırıyoruz
print("Sayının okunuşu:", sayi_okunusu(sayi))


# def: fonksiyon tanımlamak için kullanılan anahtar kelimedir.
# Fonksiyonlar belirli işlemleri gruplar ve bu işlemleri tekrar kullanabiliriz


def toplama(a, b):
    return a + b

sonuc = toplama(3, 5)
print(sonuc)  # Çıktı: 8


def cikti():
    print("Fonksiyon calisiyor")
cikti() # Fonksiyon calisiyor