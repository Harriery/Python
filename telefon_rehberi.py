import os
rehber ={
    "Yasin":51653216,
    "Nesli": 65622148
}

#Sozluge erisim icin:
#rehber["key"]
#rehber.get("key")
def ekle():
    ad =input("isim")
    tel =input("telefon")
    rehber.update({ad:tel})
    print(f"{ad} kisisi eklendi")

def ara():
    ad =input("isim").lower()
    for isim, tel in rehber.items():
        if isim.lower() == ad:
           print(tel)
           return
    else:
        print(f"{ad} Isimli bir kullanici yok.")

def sil():
    ad =input("isim")
    if ad in rehber:
        rehber.pop(ad)
        print(f"{ad} Adli kisi rehberden silindi")
        print(rehber)
    else:
        print("Boyle bir Kullanici yok..")
    
def listele():
    print("Isim - Telefon")
    for x in rehber:
        print(x,rehber.get(x))
    print(len(rehber), "Kisi Listelendi.")

while True:
    os.system("cls")    
    print("""
    Telefon Rehberi
    Ekle    -1
    Ara     -2
    Sil     -3
    Listele -4
    """)
    sec = input("Seciniz: ")
    if sec == "1":
        ekle()
    elif sec=="2":
        ara()
    elif sec == "3":
        sil()
    elif sec== "4":
        listele()

    input("Devam etmek icin Enter")