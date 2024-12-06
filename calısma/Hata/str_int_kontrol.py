#Yöntem 1: isdigit() Fonksiyonunu Kullanmak
#str sınıfında yer alan isdigit() metodu, string içinde yalnızca rakam olup olmadığını kontrol eder.
#  Eğer string sadece rakamlardan oluşuyorsa,
#True, aksi takdirde False döner.
girdi = input("Bir şey girin: ")

if girdi.isdigit():
    print("Bu bir tam sayı.")
    girdi = int(girdi)  # İsteğe bağlı: String'i tam sayıya çevir
else:
    print("Bu bir metin.")

#*****************************************************************
# Yöntem 2: try-except ile Kontrol Etmek
# Bir string’in int olup olmadığını anlamak için onu int() fonksiyonuna çevirmeyi denenir.
# Eğer bu işlem başarılı olursa, girdi bir tam sayıdır. 
# Hata alırsam, metin (veya int'e çevrilemeyen bir şey) girilmiş demektir.

girdi1 = input("Bir şey girin: ")

try:
    girdi1 = int(girdi1)  # Tam sayıya dönüştürmeyi deniyoruz
    print("Bu bir tam sayı.")
except ValueError:
    print("Bu bir metin.")

#*******************************************************************
# Yöntem 3: isinstance() ile Veri Türünü Doğrudan Kontrol Etmek
# Eğer veri türünü tam olarak kontrol etmek istiyorsan, isinstance() fonksiyonunu kullanabilir.
#  Ama bu yöntem, girdi alınırken zaten tür dönüşümü yapılmışsa işe yarar.

girdi2 = 123  # Örneğin bir sayı girildi (kullanıcıdan int türünde aldığını varsayalım)

if isinstance(girdi2, int):
    print("Bu bir tam sayı.")
elif isinstance(girdi2, str):
    print("Bu bir metin.")

# Fakat bu yöntem input() çıktısı her zaman str olduğu için doğrudan yeterli olmaz; yine int’e dönüştürme denemesi yapmak gerekir.
# yani  girdi2 = int(girdi2) ile yapilabilir.
# ******************************************************************

# 3. Tam Akış (Birleştirme)
# Hem sayı hem de metni kontrol edebileceğin bir akış kurmak için aşağıdaki yöntemi kullanabilirsin:

girdi3 = input("Bir şey girin: ")

if girdi3.isdigit():
    print("Bu bir tam sayı.")
    girdi3 = int(girdi3)  # Tam sayıya dönüştür
else:
    try:
        girdi = float(girdi)  # Eğer ondalıklı sayıysa
        print("Bu bir ondalıklı sayı.")
    except ValueError:
        print("Bu bir metin.")

# isdigit() kolay ve hızlı bir yöntemdir.
# Daha esnek bir kontrol icin (ör. float gibi), try-except kullanmak daha iyi olur.