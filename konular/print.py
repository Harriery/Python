Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
3+4
7
7//3
2
>>> isim = "Yasin"
>>> print(isim)
Yasin
>>> soyisim = "UTUK"
>>> print (isim)+ " " + print(soyisim)
Yasin
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print (isim)+ " " + print(soyisim)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
>>> isim + soyisim
'YasinUTUK'
>>> isim + ' ' + soyisim
'Yasin UTUK'
>>> sayi1 = 3
>>> sayi2 = '5'
>>> print(sayi1 + int(sayi2))
8
>>> deger3 = "python"
>>> print(deger + str(sayi1))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(deger + str(sayi1))
NameError: name 'deger' is not defined. Did you mean: 'deger3'?
>>> print(deger3 + str(sayi1))
python3
>>> 
>>> print('Yasin' + 'utuk')
Yasinutuk
>>> print('Yasin', 'Utuk')
Yasin Utuk
>>> sayi3 = 3.14
>>> print (sayi1 + sayi3)
6.140000000000001
>>> floatdeger = "3.14"
>>> print(sayi1 + float(floatdeger))
6.140000000000001
