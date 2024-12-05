birKullanici = "Yasin"
birParola ="1234"

while(True):
    kullaniciAdi = input("Kullanici Adinizi Giriniz..")
    kullaniciParola = input ("Parolanizi Giriniz..")
    if ((kullaniciAdi == birKullanici) and (kullaniciParola == birParola)):
        print(birKullanici, "Hosgeldin!")
        break
    elif((kullaniciAdi != birKullanici) and (kullaniciParola == birParola)):
        print("Kullanici Adi Yanlis..!")
        print("Kullanici Adinizi Unuttuysan 'E' degilse 'H' Basiniz ")
        cevap1 = input()
        if (cevap1 == "E"):
            yeniKullaniciAdi = input("Simdi Yeni bir Kullanici Adi Giriniz")
            birKullanici =yeniKullaniciAdi
            print("Kullanici Adiniz Basariyla Degisti..!")

    elif ((kullaniciAdi == birKullanici) and (kullaniciParola != birParola)):
        print("Sifreniz Yanlis")
        print("Sifrenizi Unuttuysaniz 'E' ye yoksa 'H' ye basiniz ")
        cevap2 =input()
        if (cevap2 == 'E'):
            yeniParola = input("Yeni bir Parola Giriniz")
            birParola = yeniParola
            print("Artik Parolaniz Degisti")
    else:
        print("Tekrar Deneyiniz")
