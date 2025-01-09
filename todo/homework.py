import json

gorev_id = 1

json_dosya = "c:\\Users\\harri\\Desktop\\Python_Modul_Week_3\\Team1\\yasin\gorevler.json"
def dosya_yukle():
    try:
        with open(json_dosya, "r") as dosya:
           return json.load(dosya)
    except  (FileNotFoundError, json.JSONDecodeError):  # Dosya yoksa veya geçersizse
        return {}

def kaydet(veriler):
        with open(json_dosya, "w", encoding="utf-8") as dosya:
            json.dump(veriler, dosya, ensure_ascii=False, indent=2)

def gorev_ekle():
    todos = dosya_yukle()  # Mevcut görevleri yükle

    # Görev listesini kontrol et
    if "gorevler" not in todos:
        todos["gorevler"] = []  # Eğer görevler listesi yoksa oluştur

    # Görev listesini al
    gorevler = todos["gorevler"]

    # ID'yi otomatik olarak artır
    if gorevler:  # Eğer görevler listesi boş değilse
        gorev_id = int(gorevler[-1]["id"]) + 1  # Son görevin ID'sine bak ve artır
    else:
        gorev_id = 1  # Görev listesi boşsa, ID 1'den başla

    # Yeni görev oluştur
    yeni_gorev = {
        "id": str(gorev_id),  # ID'yi string olarak sakla
        "gorev": input("Yeni bir Todo Ekleyin: "),  # Kullanıcıdan görev al
        "durum": "Bekliyor"  # Varsayılan durum: Bekliyor
    }

    # Yeni görevi listeye ekle
    gorevler.append(yeni_gorev)

    # JSON dosyasına kaydet
    kaydet(todos)
    print(f"{yeni_gorev['id']} ID'li görev eklendi!")

def gorev_tamamla():
    todos = dosya_yukle()
    gorevler = todos["gorevler"]  # "gorevler" anahtarına eriş
    print("Görevler:", gorevler)  # Yapıyı kontrol edin

    gorev_sec = input("Bir Görev ID'si seçiniz: ")

    for gorev in gorevler:
        gorev["id"] = str(gorev["id"])  # ID'yi string'e dönüştür

    for gorev in gorevler:
            if isinstance(gorev, dict):  # gorev'in sözlük olup olmadığını kontrol et
                if gorev["id"] == gorev_sec:
                    gorev["durum"] = "Tamamlandi"
                    print(f"{gorev_sec} ID'li görevin durumu başariyla tamamlandi!")
                    kaydet(todos)  # Güncellenmiş veriyi dosyaya kaydet
                    return
            else:
                print("Beklenmeyen veri formati:", gorev)  # Hatalı veri tipi tespit et
                return
    print("Bu ID'ye sahip bir görev yok!")

def gorev_sil():
    todos = dosya_yukle()  # Görev listesini yükle
    gorevler = todos["gorevler"]  # Görevlerin listesini al
    gorev_sec = input("Silmek istediğiniz Görevin ID'sini seçiniz: ")

    # ID'leri string'e dönüştür
    for gorev in gorevler:
        gorev["id"] = str(gorev["id"])

    # Görev silme işlemi
    for gorev in gorevler:
        if gorev["id"] == gorev_sec:
            silinen_todo = gorev  # Silinen görevi kaydetmek için
            gorevler.remove(gorev)  # Liste üzerinden görevi kaldır

            # Görev silindikten sonra ID'leri yeniden sırala
            for index, gorev in enumerate(gorevler, start=1):
                gorev["id"] = str(index)  # ID'yi yeniden sırala (1'den başlayarak)

            print(f"{silinen_todo['gorev']} görevi başarıyla silindi!")
            kaydet(todos)  # Güncellenmiş veriyi dosyaya kaydet
            return

    # Eğer ID bulunamazsa hata mesajı göster
    print("Bu ID'ye sahip bir görev yok!")
    
def tum_gorevler():
    todos = dosya_yukle()
    if "gorevler" in todos and todos["gorevler"]:
        print("Tum Gorevler Listesi: ")
        for x in todos["gorevler"]:
            print(f"ID: {x['id']}, Gorev: {x['gorev']}, Durum: {x['durum']}")
    else:
        print("Henuz bir Todo  Yok!!")

def tamamlanan_gorevler():
    todos = dosya_yukle()
    gorevler = todos["gorevler"]
    for gorev in gorevler:
        if gorev["durum"] == "Tamamlandi":
            print(gorev)
            kaydet(todos)
            return

    print("Tamamlanan Gorevler")
def bekleyen_gorevler():
    todos = dosya_yukle()
    gorevler = todos["gorevler"]
    for gorev in gorevler:
        if gorev["durum"] == "Bekliyor":
            print(gorev)
            kaydet(todos)
            return
import os
while True:
    os.system("cls")
    print("""
    Gorev Yonetici Uygulamasi :
    1- Yeni Gorev Ekle
    2- Gorevi Tamamla
    3- Gorev sil
    4- Tum Gorevler
    5- Tamamlanan Gorevler
    6- Tamamlanan Gorevler
    """)
    secim = input("Bir Islem Seciniz...")

    if secim == "1":
        gorev_ekle()
    elif secim == "2":
        gorev_tamamla()
    elif secim == "3":
        gorev_sil()
    elif secim == "4":
        tum_gorevler()
    elif secim == "5":
        tamamlanan_gorevler()
    elif secim == "6":
        bekleyen_gorevler()
    
    input("Devam Etmek Icin Enter'e Basiniz..")
