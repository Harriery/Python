def sayi_okunusu(sayi):
    # Sayıyı string'e dönüştürüp basamak sayısını hesaplıyoruz
    sayi_str = str(sayi)

    # Sözlükler
    birler_basamagi = {
        "0": "sıfır", "1": "bir", "2": "iki", "3": "üç", "4": "dört",
        "5": "beş", "6": "altı", "7": "yedi", "8": "sekiz", "9": "dokuz"
    }
    onlar_basamagi = {
        "1": "on", "2": "yirmi", "3": "otuz", "4": "kırk", "5": "elli",
        "6": "altmış", "7": "yetmiş", "8": "seksen", "9": "doksan"
    }

    # Sayının uzunluğuna göre işlem
    okunus = []
    uzunluk = len(sayi_str)

    if uzunluk == 2:  # İki basamaklı sayılar
        if sayi_str[0] != "0":  # Onlar basamağı sıfır değilse
            okunus.append(onlar_basamagi[sayi_str[0]])
        if sayi_str[1] != "0":  # Birler basamağı sıfır değilse
            okunus.append(birler_basamagi[sayi_str[1]])
    elif uzunluk == 1:  # Tek basamaklı sayılar
        okunus.append(birler_basamagi[sayi_str[0]])
    else:
        return "Sadece 1 veya 2 basamaklı sayılar destekleniyor!"

    # Okunuşu birleştirip döndürüyoruz
    return " ".join(okunus)


# Kullanıcıdan sayıyı alıyoruz
sayi = int(input("Bir sayı giriniz (1 veya 2 basamaklı): "))

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



# 7 / 3 = 2.333333
# 7 // 3 = 2