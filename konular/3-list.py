Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
katilimci = ["Yasin", "Utuk", 31, 1.83,"Turkiye"]
katilimci
['Yasin', 'Utuk', 31, 1.83, 'Turkiye']
Katilimci[3]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Katilimci[3]
NameError: name 'Katilimci' is not defined. Did you mean: 'katilimci'?
katilimci[2]
31
katilimci[0]
'Yasin'
katilimci[0:1]
['Yasin']
katilimci[:3]
['Yasin', 'Utuk', 31]
katilimci[:2]
['Yasin', 'Utuk']
>>> katilimci[:-1]
['Yasin', 'Utuk', 31, 1.83]
>>> katilimci[-2]
1.83
>>> katilimci = katilimci + ["Hollanda"]
>>> katilimci
['Yasin', 'Utuk', 31, 1.83, 'Turkiye', 'Hollanda']
>>> len(katilimci)
6
>>> katilimci[:2] = ["Halil", "Dereli"]
>>> katilimci
['Halil', 'Dereli', 31, 1.83, 'Turkiye', 'Hollanda']
>>> katilimci[:2] = ["Yasin", "Utuk"]
>>> katilimci
['Yasin', 'Utuk', 31, 1.83, 'Turkiye', 'Hollanda']
>>> katilimci.append = ["IT"]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    katilimci.append = ["IT"]
AttributeError: 'list' object attribute 'append' is read-only
a
>>> katilimci.append("IT")
>>> katilimci
['Yasin', 'Utuk', 31, 1.83, 'Turkiye', 'Hollanda', 'IT']
>>> ['Yasin', 'Utuk', 31, 1.83, 'Turkiye', 'Hollanda', 'IT']
['Yasin', 'Utuk', 31, 1.83, 'Turkiye', 'Hollanda', 'IT']
>>> katilimci = []
>>> katilimci
[]
