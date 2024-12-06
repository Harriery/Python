metin =input("bir metin giriniz: ")
rakamlar = []
for x in metin:             # her bir karakter kontrol edilir.
    if x.isdigit():         #Eger karakter rakamsa 
        rakamlar.append(x)  # rakamlari listeye ekler

print(rakamlar)
print(len(rakamlar))