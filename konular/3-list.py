
katilimci = ["Yasin", "Utuk", 31, 1.83,"Turkiye"]
katilimci
['Yasin', 'Utuk', 31, 1.83, 'Turkiye']

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
katilimci[:-1]
['Yasin', 'Utuk', 31, 1.83]
katilimci[-2]
1.83
katilimci = katilimci + ["Hollanda"]
katilimci
['Yasin', 'Utuk', 31, 1.83, 'Turkiye', 'Hollanda']
len(katilimci)
6
katilimci[:2] = ["Halil", "Dereli"]
katilimci
['Halil', 'Dereli', 31, 1.83, 'Turkiye', 'Hollanda']
katilimci[:2] = ["Yasin", "Utuk"]
katilimci
['Yasin', 'Utuk', 31, 1.83, 'Turkiye', 'Hollanda']
katilimci.append = ["IT"]
katilimci.append = ["IT"]

katilimci.append("IT")
katilimci
['Yasin', 'Utuk', 31, 1.83, 'Turkiye', 'Hollanda', 'IT']
['Yasin', 'Utuk', 31, 1.83, 'Turkiye', 'Hollanda', 'IT']
['Yasin', 'Utuk', 31, 1.83, 'Turkiye', 'Hollanda', 'IT']
katilimci = []
katilimci
[]
# list() fonksiyonunu kullanarak liste olusturma:
numbers = list([1,2,3])
#range() fonk olusturarak list olusturma:
number_range = list(range(1, 6)) # [1,2,3,4,5]
#Liste İfadesi ile Liste Oluşturmak (list comprehension)
squared_numbers = [x**2 for x in range(1, 6)]

#Nested List: iç içe geçmiş liste
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
students = [
    ["Alice", 23, "Computer Science"],
    ["Bob", 21, "Mathematics"],
    ["Eve", 22, "Physics"]
]

#****************************************************************************
#List içerisindeki bir elemana nasıl ulaşabiliriz?
my_list = [10, 20, 30, 40, 50]

first_element = my_list[0]  # Listenin ilk elemanını alır (10).
second_element = my_list[1]  # Listenin ikinci elemanını alır (20).
third_element = my_list[2]   # Listenin üçüncü elemanını alır (30).


#Ayrıca, negatif indeksler kullanarak listenin sonundan başlayarak geriye doğru sayabilirsiniz:
last_element = my_list[-1]  # Listenin son elemanını alır (50).
second_last_element = my_list[-2]  # Listenin sondan ikinci elemanını alır (40).

# Eğer belirli bir aralıktaki elemanlara ulaşmak isterseniz, slicing (dilimleme) yöntemini kullanabilirsiniz:
sub_list = my_list[1:4]  # 1. indeksten 3. indekse kadar (3. indeks dahil değil) olan elemanları içeren alt liste.

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# İç içe geçmiş listeye erişim örnekleri
element_1_1 = nested_list[1][1]  # İkinci satırın ikinci elemanı (5)
element_0_2 = nested_list[0][2]  # İlk satırın üçüncü elemanı (3)
element_2_0 = nested_list[2][0]  # Üçüncü satırın ilk elemanı (7)

print(element_1_1)  # Çıktı: 5
print(element_0_2)  # Çıktı: 3
print(element_2_0)  # Çıktı: 7


#********************************************************************
#LISTEYE ELEMAN EKLEME/CIKARMA VE VAR OLAN ELEMANI DEGISTIRME

#  ELEMAN EKLEME:

#1-  append() Metodu: Listenin sonuna yeni bir eleman eklemek için append() metodunu kullanabilirsiniz.

my_list = [1, 2, 3]
my_list.append(4)  # Listenin sonuna 4 ekler.

#2- insert() Metodu: Belirli bir indekse yeni bir eleman eklemek için insert() metodunu kullanabilirsiniz.
my_list = [1, 2, 3]
my_list.insert(1, 5)  # İkinci indekse 5 ekler. my_list = [1,5,2,3]

#extend() Metodu: Bir listeyi diğer bir listeyle birleştirmek ve elemanları eklemek için extend() metodunu kullanabilirsiniz.
my_list = [1, 2, 3]
new_elements = [4, 5, 6]
my_list.extend(new_elements)  # Listenin sonuna [4, 5, 6] ekler.

#**********************************************************************

# ELEMAN CIKARMA:

#1- pop() Metodu:
#  Belirli bir indeksteki elemanı çıkarmak için pop() metodunu kullanabilirsiniz. Eğer indeks belirtilmezse, son eleman çıkarılır.
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop(2)  # Üçüncü elemanı (3) çıkarır ve çıkarılan elemanı döndürür.
# Sonuç: my_list = [1, 2, 4, 5], popped_element = 3

#2- remove() Metodu:
#  Belirli bir değere sahip olan ilk elemanı çıkarmak için remove() metodunu kullanabilirsiniz.
# Eğer çıkarılacak elemanın değerini biliyorsanız, indeks kullanmadan doğrudan 
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)  # İlk değeri 2 olan elemanı çıkarır.

#3- del Anahtarı
#  ile Çıkarma: del anahtar kelimesini kullanarak belirli bir indeksteki elemanı çıkarabilirsiniz.
codemy_list = [1, 2, 3, 4, 5]
del my_list[1]  # İkinci elemanı (indeks 1) çıkarır.

# Ayrica del metoduyla tum liste de silinir
my_list = [1, 2, 3, 4, 5]
del my_list  # Tüm listeyi siler.
# print(my_list)  # Hata! my_list artık tanımlı değil.

#Lístedeki bir elemanı değiştirme:
my_list = [1, 2, 3, 4, 5]
my_list[0] = 10  # İlk elemanı 10 ile değiştirir.
# print(my_list)  # Sonuç :[10,2,3,4,5]

# LIST METODLARI:

# clear():
# Bir listenin içindeki tüm elemanları kaldırarak listenin boş hale getirir.
my_list = [1, 2, 3, 4, 5]
my_list.clear()  # Tüm elemanları temizler.
print(my_list)   # Çıktı: []

# index():
#  Belirli bir değere sahip ilk elemanın indeksini döndürür.
my_list = [10, 20, 30, 20, 40]
index = my_list.index(20)
# Sonuç: index = 1

#count():
#  Belirli bir değerin listede kaç kez geçtiğini sayar.
my_list = [10, 20, 30, 20, 40]
count = my_list.count(20)
# Sonuç: count = 2

#sort():
#  Listeyi küçükten büyüğe sıralar (listede kalıcı değişiklik yapar).
my_list = [4, 1, 3, 2]
my_list.sort()
# Sonuç: my_list = [1, 2, 3, 4]

# reverse():
#  Listeyi tersine çevirir (listede kalıcı değişiklik yapar).
my_list = [1, 2, 3, 4]
my_list.reverse()
# Sonuç: my_list = [4, 3, 2, 1]


# copy(): Listenin bir kopyasını oluşturur.
my_list = [1, 2, 3]
new_list = my_list.copy()
# Sonuç: new_list = [1, 2, 3]

#sorted():
# Bir listenin öğelerini sıralar ve sıralanmış bir liste döndürür.
my_list = [4, 2, 1, 3, 5]
sorted_list = sorted(my_list)
print(sorted_list)  # Çıktı: [1, 2, 3, 4, 5]

#***************************************************************************
#LIST COMPREHENSIONS:
# List comprehensions (liste anlama yapıları), Python'da listenin daha kısa ve okunabilir bir şekilde oluşturulmasını sağlayan bir yapıdır.
# List comprehension'lar, mevcut bir liste, dizi veya veri kümesi üzerinde döngü işlemleri yaparak yeni bir liste oluşturmanıza olanak tanır.

# new_list = [expression for item in iterable if condition]
# expression: Oluşturulacak yeni elemanın ifadesi.
# item: Iterable (örneğin liste, dizi veya range) içindeki her bir öğe.
# iterable: Üzerinde döngü yapılacak olan veri yapısı.
# condition (isteğe bağlı): Bir koşula bağlı olarak elemanları filtrelemek için kullanılır.

# Örnek 1: Kareler Listesi
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
# squared_numbers: [1, 4, 9, 16, 25]

# Örnek 2: Çift Sayıları Filtreleme:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
# even_numbers: [2, 4, 6, 8, 10]

# Örnek 3: Harf Dizisi Oluşturma:
word = "Python"
letters = [char for char in word]
# letters: ['P', 'y', 't', 'h', 'o', 'n']

#Örnek 4: İç İçe List Comprehension:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# flattened: [1, 2, 3, 4, 5, 6, 7, 8, 9]

