#ogrenciAdi = "neslihan"
#print(ogrenciAdi) 
#print(len(ogrenciAdi))

#print(ogrenciAdi[-1])
#sozluk = ["elma", "armut", 7, 24.5 ]
#print(sozluk)
#print((sozluk)[1])
#sozluk.append('ayva')
#sozluk = sozluk + ["seftali"]
#print (sozluk[-2:])

print("Oyuncu Giris Merkezi")

adi = input("adinizi giriniz")
nickName = input("NIckName giriniz")
yas = int(input("Yasinizi Giriniz"))

kullanici = [adi, nickName, yas]
#print("oyuncu adi", adi , "nick Name" , nickName ,"yasi" , yas)
#print("oyuncu adi: {}\n nick Name: {}\n yasi:{}\n".format (kullanici[0],kullanici[1],kullanici[2]))
if kullanici[2] >= 18:
    print("Siteye Giris Yapabilirsiniz!")
else:
    print("Yasiniz uygun degil!!")