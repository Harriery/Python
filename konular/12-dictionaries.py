# Dictionary nasıl oluşturulur?
#1. Süslü Parantezler {} ile Dictionary Oluşturma:
person = {
    "name": "Mike",
    "age": 60,
    "email": "mikejones@example.com"
}

#2. dict() Fonksiyonu ile Dictionary Oluşturma:
person = dict(name="John", age=30, email="john@example.com")
print(person) # {'name': 'John', 'age': 30, 'email': 'john@example.com'}

#3. 3. Liste ve Tuple Kullanarak Dictionary Oluşturma:
keys = ["name", "age", "email"]
values = ["John", 30, "john@example.com"]
person = dict(zip(keys, values))

# 4. fromkeys() Metodu ile Anahtarları Değerle İlişkilendirme:
keys = ["name", "age", "email"]
default_value = "N/A"
person = dict.fromkeys(keys, default_value)
# fromkeys() metodu, belirtilen anahtarları belirtilen varsayılan değerle ilişkilendiren bir dictionary oluşturmanızı sağlar.


# NESTED DICTIONARY:

school = {
    "name": "XYZ School",
    "location": "City A",
    "students": {
        "Alice": {
            "age": 16,
            "grade": 11
        },
        "Bob": {
            "age": 17,
            "grade": 12
        }
    }
}
