harf = input("Bir harf giriniz: ")

if len(harf) != 1:
    raise ValueError("Lütfen sadece bir harf giriniz!")
if not harf.isalpha():
    raise ValueError("Sadece alfabetik karakter giriniz!")
"""
Ne Zaman raise Kullanılır?
Kendi Hata Durumlarını Tanımlamak İçin:

Programın belirli bir durumla karşılaşmasını istemiyorsan (örneğin, geçersiz giriş, sıfıra bölme gibi), bu durumda hata fırlatabilirsin.
Geliştiriciye Anlamlı Mesajlar Göndermek İçin:

Programın neden çalışmadığını anlaması için açık bir hata mesajı sağlamak.
Özel İş Kuralları:

Örneğin, bir bankacılık uygulamasında, bir hesaptan negatif bakiye çekilmek istendiğinde hata fırlatılabilir.
Test ve Doğrulama:

Kodun düzgün çalışıp çalışmadığını kontrol etmek için özel hata fırlatabilirsin.
Not:
raise, programın normal akışını bozar ve bir hata fırlatır. Eğer bu hatayı yakalamak istiyorsan try-except bloğu ile kullanabilirsin.

"""

try:
    raise ValueError("Bir hata oluştu!")
except ValueError as e:
    print(f"Hata yakalandı: {e}")