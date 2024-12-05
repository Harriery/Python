faktoriyel = 1

while True:
    sayi = int(input("Lutfen bir sayi Giriniz"))
    if (sayi<= 0):
        print("Negatif deger girdiniz, Tekrar deger giriniz!!")
    else:
        for i in range(1, sayi+1):
            faktoriyel = faktoriyel * i

            print("Faktoriyel", faktoriyel)
        break

#Faktoriyel 1
#Faktoriyel 2
#Faktoriyel 6
#Faktoriyel 24 seklinde olur. 
# Yani inputta sayi degerine 4 verdigimizde, for dongusu icinde bunu donecek.
# tabi range fonk ile inputta aldigimiz degerin faktoriyelini bulacagiz
#sayi+1  yazmamizdaki maksat, range(1, sayi+1)ile sayi degerine kadar listeleyecek 
# Ama biz istedigimiz sayinin faktoriyelini almak istiyoruz.
#+1 yazmazsak Onr sayi 4 olsaydi, range(1, 4) 1'den baslayacak 4é kadar listeleyecekti 1 2 3 seklinde
# faktoriyel = faktoriyel *i ise; sayi 1 ken faktoriyel degeri 1 = 1 olcak sonra +1 ile 1*2 den 2 olcak  
# taki sayi inputunda girdigimiz degerin faktoriyelini gorene kadar.
# sayi+1 ile input(sayi) degerine 4 girdigimizde range fonk ile (1, 4+1) yani 5 e kadar listeleyecek 1 2 3 4 ve 
# bu degerleri her defasinde kendi degeri yapip 1 artirarak tekrar carpacak ve istenilen degerin faktoriyelini bulacak.
