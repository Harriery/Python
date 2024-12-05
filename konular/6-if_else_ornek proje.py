print ("Kullanici Girisi Sorgu Ekrani..")

Akullaniciadi ="Yasin"
Akullaniciparola = "1234"

kullaniciAdi = input("Kullanici Adinizi Giriniz: ")
kullaniciParola = input ("Kullanici Parolanizi Giriniz: ")

if ((Akullaniciadi == kullaniciAdi) and (Akullaniciparola == kullaniciParola)): 
    print("Hosgeldiniz")
elif((Akullaniciadi != kullaniciAdi) and (Akullaniciparola == kullaniciParola)):
    print("Kullanici Adi Dogru Degil..!")
elif((Akullaniciadi == kullaniciAdi) and (Akullaniciparola != kullaniciParola)):
    print("Parolaniz Dogru Degil..!")
else: 
    ("Kayitli Olmayan Kullanici..!!")