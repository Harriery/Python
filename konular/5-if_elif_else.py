"""
 a == b   -> a, b ye esitse
 a!= b    ->  a, b ye esit degilse
 a >= b    -> a, b buyukesitse
 a <= b    -> a, b kucuk esitse
 a and b    a ve b nin ikisininde kosulu sagladigi durumlardaki sorgulama
            a yada b den birisi false olursa calismaz.

a or b      a yada b den birisi o durumu karsilidigi durumlardaki sorgulma

not a       a nin kosulu saglamadigi durumnlardaki sorgulama isleminde kullanilir.
 
 Ama if yapisi aslinda
 if a == b:
   print('yalniz basina bir kosul sorgulmasi yapilabilir')
 elif a <= b:
   print ('elif yalniz basina kullanilmaz')
 elif a >= b:
   print('')
 else:
   print ('hicbir kosulu karsilamiyor, yada gecersiz durumlarda else kullanilir.')


"""
print("Siteye Giris Sorgu Ekrani...")
yas = int(input("Yasinizi Giriniz: "))  

if yas >= 18:
    print("Siteye Girebilirsiniz")
else:
    print("Siteye Giris Icin Yasiniz Uygun Degil..!")    


print("Sinav Sonucu Sorgulama Ekrani..")
sinav = int(input("Sinav Sonucunuzu Giriniz.."))

if sinav >=90:
    print("AA aldiniz..")
elif sinav >=85:
    print("BA aldiniz")
elif sinav >= 80:
    print("BB alsiniz")
else:
    print("Kaldiniz")