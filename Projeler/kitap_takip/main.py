import json
import os
tracking_list= "c:\\Users\\harri\\Desktop\\Python\\Projeler\\kitap_takibi\tracking_list.json"
kitap_id= 1

def dosya_yukle():
    try:
        with open(tracking_list, "r") as dosya:
            return json.load(dosya)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}        

def dosya_kaydet(veriler):
    with open(tracking_list, "w", encoding ="utf-8") as dosya:
        json.dump(veriler, dosya, indent =2)

def ekle():

    kitaplar =dosya_yukle()

    if "kitap_listesi" not in kitaplar:
        kitaplar["kitap_listesi"] =[]

    kitap_takip =kitaplar["kitap_listesi"]

    if kitap_takip:
        kitap_id = int(kitap_takip[-1]["id"]) +1
    else:
        kitap_id =1

    yeni_kitap = {
        "id": str(kitap_id),
        "kitap_ad": input("Kitap Adi Giriniz.."),
        "Durum": "Kutuphanede"
    }

    kitap_takip.append(yeni_kitap)

    dosya_kaydet(kitaplar)
    print(f"{yeni_kitap['kitap_ad']} Adli Kitap {yeni_kitap['id']} ID ile Basariyla Listeye Kaydedildi..! " )  

def kitap_al():
    print("Kullanici Kitabi Kutuphaneden Basariyla Aldi..")

def kitap_iade():
    print("KKullanici Kitabi Basariyla Kutuphaneye Teslim Etti.")

def arama():
    print("aranilan kitap basariyla Bulundu")

def listele():
    print("Kutuphanedeki Tum Kitaplarin Listesi")


while True:
    os.system("cls")
    print("""
    Kutuphane Kitap Yonetim Sistemi:
        1-Yeni Kitap Ekle
        2-Kitap Odunc Al
        3-Kitap Iade Et
        4-Kitap Ara
        5-Tum kitaplar
        
    """)
    secim = input("Lutden Bir islem Seciniz..")

    if secim == "1":
        ekle()
    elif secim == "2":
        kitap_al()
    elif secim == "3":
        kitap_iade()
    elif secim == "4":
        arama()
    elif secim == "5":
        listele()
    input('Devam Etmek icin Entere Basiniz.')
    