# Set Nedir?
# Python'da Set, benzersiz ve sırasız (unordered) elemanların koleksiyonunu tutan bir veri yapısıdır.
#  Set'ler matematiksel kümelerin kavramlarına dayanır ve her elemanın yalnızca bir defa bulunabileceği bir yapıya sahiptir.
#  Set'lerde indeksleme veya sıralama gibi kavramlar bulunmaz.

# Set:
#- Benzersiz Elemanlar
#- Sirasizdir
#- Degistirilebilir
#- Eleman kontrolu Yapilabilir.

# Set Olusturma:
#1- {} ile 
#2- set() ile liste, tuole, string gibi yapilari set'e cevirir.
#

# SET ICINDEKI ELEMANLARA ULASMAK: *********
#Set'lerde elemanlara indeks numarası veya sıralama ile erişmek mümkün değildir 
# çünkü set'ler sırasız (unordered) veri yapılarıdır.


### Elemanın Set İçinde Olup Olmadığını Kontrol Etme: ********

#Bir elemanın set içinde olup olmadığını in operatörü ile kontrol edebilirsiniz:

my_set = {1, 2, 3, 4, 5}
element_to_check = 3

if element_to_check in my_set:
    print(f"{element_to_check} set içinde bulunuyor.")
else:
    print(f"{element_to_check} set içinde bulunmuyor.")

# FOR ILE SET ICINDE GEZINME:
# for element in my_set:
#     print(element)

#**********************************************************************
# SET METODLARI

#1-  add(): 
# Bir eleman eklemek için kullanılır.
my_setim = {1, 2, 3}
my_setim.add(4)
print(my_setim, "add kullanimi") # -> {1, 2, 3, 4}

# 2- remove(): 
# Belirtilen bir elemanı set içinden kaldırmak için kullanılır.
#  Eğer eleman set içinde yoksa KeyError hatası verir.
# my_setim = {1, 2, 3, 4}
my_setim.remove(4) 
print(my_setim, "remove kullanimi") #  {1, 2, 3}

# 3- discard():
#  Belirtilen bir elemanı set içinden kaldırmak için kullanılır.
#  Eğer eleman set içinde yoksa hata vermez.
my_setim = {1, 2, 3, 4, 5}
my_setim.discard(5)
print(my_setim, "discard kullanimi") # {1, 2, 3, 4}


# 4- pop():
#  Set içinden rastgele bir elemanı çıkarır ve bu elemanı döndürür.
#  Set boşsa KeyError hatası verir.
my_setim = {1, 2, 3, 4, 5, 6}
popped_element = my_setim.pop()
print("pop kullanimi ile guncel my_setim: ", my_setim, ) #  {2, 3, 4, 5, 6}
print("pop metorduyla kaldirilan eleman: ", popped_element, ) # cikarilan eleman 1 ama baska bir elemanda olabilir.

# 5- clear():
# Set'in içindeki tüm elemanları kaldırır ve boş bir set oluşturur.
my_set = {1, 2, 3}
my_set.clear()


# 6- union():
#  İki veya daha fazla set'in birleşimini döndürür.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("union metodu kullanimi: ", union_set) # {1, 2, 3, 4, 5}

# 7- intersection(): 
# İki veya daha fazla set'in kesişimini döndürür.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print("intersection kullanimi ile kesisen elemanlar: ", intersection_set) # {3, 4}

# 8- difference():
# Bir set ile diğer setler arasındaki farkı döndürür.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print("difference kullanimi:", difference_set) # {1, 2}

# 9- symmetric_difference():
#  İki set arasındaki simetrik farkı (her iki sette de bulunmayan elemanlar) döndürür.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)
print("symmetric_difference kullanimi: ", symmetric_difference_set) # {1, 2, 5}

# 10- update():
#  Bir seti başka bir setle günceller veya diğer iterable veri yapılarından gelen elemanlarla günceller.
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6, 7 }
set1.update(set2)  # set1'i set2 ile günceller
print("update metodu kullanimi ile set1 : ", set1) # {1, 2, 3, 4, 5, 6, 7}

# 11- intersection_update():
#  Bir seti, diğer set ile olan kesişimine günceller.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)  # set1'i set2 ile kesişime günceller
print("intersection_update kullanimi ile set1 : ", set1) # {3}

# 12- difference_update(): 
# Bir seti, diğer set ile olan farkına günceller.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set1.difference_update(set2)  # set1'i set2 ile farkına günceller
print("difference_update kulllanimi ile set1 son hali: ",set1) #{1, 2}

#13- symmetric_difference_update():
#  Bir seti, diğer set ile olan simetrik farkına günceller.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)  # set1'i set2 ile simetrik farkına günceller
print("symmetric_difference_update", set1) # {1, 2, 4, 5}

#14- issubset(): ********
# Bir setin başka bir setin alt kümesi olup olmadığını kontrol eder.

set1 = {1, 2}
set2 = {1, 2, 3, 4}
is_subset = set1.issubset(set2)  # True

#15- issuperset(): *****
#  Bir setin başka bir setin üst kümesi olup olmadığını kontrol eder. 
set1 = {1, 2, 3, 4}
set2 = {1, 2}
is_superset = set1.issuperset(set2)  # True

#16-isdisjoint():
# İki setin kesişiminin boş olup olmadığını kontrol eder.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
is_disjoint = set1.isdisjoint(set2)  # True


# SET'LERDE FOR KULLANIMI:
my_set = {10, 20, 30, 40, 50}

# For döngüsü kullanarak set içindeki elemanları gezmek
for element in my_set:
    print(element)

# SET'LERDE BUILT-IN FONKSIYONLARI:
#1- len():
#  Bir setin eleman sayısını döndürür.
my_set = {1, 2, 3, 4, 5}
length = len(my_set) # 5

#2- max(): Bir setin en büyük elemanını döndürür.
my_set = {10, 5, 25, 30}
max_element = max(my_set) # {30}

#3- min(): Bir setin en küçük elemanını döndürür.
my_set = {10, 5, 25, 30}
min_element = min(my_set)

#4- sum(): Bir setin elemanlarının toplamını hesaplar.
my_set = {10, 5, 25, 30}
sorted_list = sorted(my_set)

#5-sorted(): Bir setin elemanlarını küçükten büyüğe sıralayarak bir liste olarak döndürür.
my_set = {10, 5, 25, 30}
sorted_list = sorted(my_set)

#6- any():
#  Bir setin içindeki elemanlardan en az biri True veya True değerine çevrilebilecekse True,
#  aksi halde False döndürür.
bool_set = {False, False, True}
any_true = any(bool_set)  # True

#7- all():
#  Bir setin içindeki elemanların hepsi True ise veya True değerine çevrilebiliyorsa True,
#  aksi halde False döndürür.
bool_set = {False, False, True}
all_true = all(bool_set)  # False
