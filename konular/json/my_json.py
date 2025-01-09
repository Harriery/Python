# Json: her yazilim dilinin anladigi ortak bir data veri turu.
#Json modulu import edilir. ve altina yazilan srt degerdeki dict de burada kullanilmaya calisilir.

# dict: person ={"name": "Ali", "languages": ["phyton", "Java script"] }
# result = person
# print(result)   # {'name': 'Ali', 'languages': ['phyton', 'Java script']}
# print(result["name"])   # Ali
# print(result["languages"]) # ['phyton', 'Java script']
# print(result["languages"][0])  # phyton 
# print(type(result))     # class 'dict'

# eger ben yukardaki sozluk yapisini bir json yapisi olarak gorebilmem icin,
# bu yapinin bir string yapi olmasi gerekir.
# person =' {"name": "Ali", "languages": ["phyton", "Java script"] '

# bu yapiyi calistirmak istersek string oldugu icin calismaz. Hata verir
person =' {"name": "Ali", "languages": ["phyton", "Java script"] '
#   print(result["name"]) calismaz  yukardaki sozluk degil bir str.

# Iste json veri turu de str bir yapidir. Veriler yukardaki gibi saklanir.
# json modulu ile bu yapiyi kullanabiliriz. en yukariya json import yazilir

# Json string to Dict
import json
person_srt ='{"name": "Ali", "languages": ["phyton", "Java script"] }'  # str veri 
result = json.loads(person_srt)  # json srt verisini pyhtonda kullanabilecegimiz bir dict cevirdik.
print(result)   # {'name': 'Ali', 'languages': ['phyton', 'Java script']}
print(type(result)) # class 'dict'
print(result["name"])   # Ali       # artik dict old icin icindeki keylerle verilere de ulasabilirim.


# Json dosyasindan verilere erisme:
with open("c:/Users/harri/Desktop/python/konular/json/person.json") as file:    
    data = json.load(file)
    print(data)     # {'name': 'Hasan', 'languages': ['phyton', 'C#']}
    print(data["name"]) # Hasan

#***************************************************************
# json.load(): Dosyadan JSON okuma.
# json.load(file): JSON verisini bir dosyadan okur.
# Eğer JSON veriniz bir dosyada ise, json.load() kullanmalısınız.

# json.loads(): String'den JSON okuma.
# json.loads(string): JSON verisini bir string'den okur.
# Eğer JSON veriniz bir string formatında (örneğin bir API'den alındıysa) ise, json.loads() kullanmalısınız.
#*************************************************************

# Dict to Json uygun str bir veriye Donusturme ve farkli json dosyasina yazma:
person_dict ={
   "name": "Veli",
   "languages": ["Pyhton", "Java"],  
   
}

dict_to_str = json.dumps(person_dict) 
print(dict_to_str) # {"name": "Veli", "languages": ["Pyhton", "Java"]}
print(type(dict_to_str))    # class 'str' 
#print(dict_to_str["name"])  # Hata verir. Srt veriyi dict gibi okuyamaz.

# Json dosyasina veri kaydetme/gonderme:
with open("c:/Users/harri/Desktop/python/konular/json/person.json", "w") as f:
    json.dump(person_dict,f)

#*****************************************************************
# json.dump(): JSON verisini farkli bir json dosyasina yazar.
# json.dump() kullanmalısınız eğer JSON verisini dosyaya yazmak istiyorsanız.


# json.dumps(): JSON verisini string olarak döndürür.
# json.dumps() kullanmalısınız eğer JSON verisini string olarak almak veya manipüle etmek istiyorsanız 
# (örneğin, bir API'ye gönderme, ekrana yazdırma).
#*****************************************************************