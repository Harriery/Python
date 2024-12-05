metin = input("metin giriniz: ") # kelime hesaplama uygulamasi

bolunmus_metin = metin.split() 
print(bolunmus_metin) # ['kelime', 'hesaplama', 'uygulamasi']
print(len(bolunmus_metin)) # 3

metin = "elma,armut,çilek,kiraz"
meyveler = metin.split(',')  # Virgüle göre böl
print(meyveler)