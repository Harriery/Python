sonuc = 0
while True:
    sayi = input("Sayiyi giriniz: ")
    kuvvet = input("Ussu giriniz: ")
    if sayi.isdigit() and kuvvet.isdigit():
        sayi = int(sayi)
        kuvvet = int(kuvvet)
        sonuc = sayi ** kuvvet
        
        break
    else:
        print("Lutfen sayi giriniz")
    
print(sonuc)