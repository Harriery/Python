while True:
    print("\n--- Basit Hesap Makinesi ---")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

    # Kullanıcıdan işlem seçimi alınır
    secim = input("Bir işlem seçin (1-5): ")

    if secim == "5":
        print("Hesap makinesinden çıkılıyor.")
        break  # Programı sonlandır

    # İşlem seçiminin geçerli olup olmadığını kontrol et
    if secim in ["1", "2", "3", "4"]:
        try:
            # Sayı girişlerini al
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))

            # İşlem seçimine göre hesaplama yap
            if secim == "1":
                print("Sonuç:", sayi1 + sayi2)
            elif secim == "2":
                print("Sonuç:", sayi1 - sayi2)
            elif secim == "3":
                print("Sonuç:", sayi1 * sayi2)
            elif secim == "4":
                if sayi2 == 0:
                    print("Hata: 0'a bölme yapılamaz.")
                else:
                    print("Sonuç:", sayi1 / sayi2)
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı girin.")
    else:
        print("Geçersiz seçim, lütfen 1-5 arasında bir değer girin.")
