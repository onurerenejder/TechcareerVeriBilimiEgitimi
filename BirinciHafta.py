"""
HAFTA 1: PYTHON TEMELLERİ VE VERİ YAPILARI

Bu derste Python programlamaya giriş yapacağız. Temel veri tiplerini, 
operatörleri, koşullu ifadeleri, döngüleri ve temel veri yapılarını öğreneceğiz.
"""

# -----------------------------------------------------------------
# --- 1. Temel Veri Tipleri (Variables and Data Types) ---
# -----------------------------------------------------------------
# Python'da verileri saklamak için değişkenleri kullanırız. 
# Her değişkenin bir tipi vardır.

# Integer (Tam Sayı)
sayi = 36 

# Float (Ondalıklı Sayı)
ondalık = 3.14

# String (Metin)
metin = "Merhaba Dünya"

# Boolean (Mantıksal)
dogru_mu = True

print(f"Sayı: {sayi}, Tipi: {type(sayi)}")
print(f"Ondalık: {ondalık}, Tipi: {type(ondalık)}")
print(f"Metin: {metin}, Tipi: {type(metin)}")
print(f"Doğru mu: {dogru_mu}, Tipi: {type(dogru_mu)}")


# -----------------------------------------------------------------
# --- 2. Aritmetik Operatörler (Arithmetic Operators) ---
# -----------------------------------------------------------------
# Sayılar üzerinde matematiksel işlemler yapmak için kullanılırlar.

a = 36
b = 23

print(f"Toplam (a + b): {a + b}")
print(f"Fark (a - b): {a - b}")
print(f"Çarpım (a * b): {a * b}")
print(f"Bölüm (a / b): {a / b}")         # 1.565217391304348 (Her zaman float döner)
print(f"Tam Bölüm (a // b): {a // b}")   # 1 (Sonucun tam sayı kısmı)
print(f"Mod (a % b): {a % b}")           # 13 (Bölümden kalan)
print(f"Üs Alma (a ** 2): {a ** 2}")     # 36'nın karesi


# -----------------------------------------------------------------
# --- 3. String (Metin) İşlemleri ---
# -----------------------------------------------------------------
# Metinler üzerinde birleştirme ve çeşitli metotlar kullanabiliriz.

# String Birleştirme ve f-string
ad = "onur"
soyad = "ejder"

# Yöntem 1: f-string (En modern ve tavsiye edilen yöntem)
print(f"merhaba benim adım {ad} soyadım {soyad}")

# Yöntem 2: + operatörü ile birleştirme
tam_ad = ad + " " + soyad
print(tam_ad)

# String Metotları
metin_ornek = "Python Programlama"

print(f"Orijinal: {metin_ornek}")
print(f"Küçük Harf: {metin_ornek.lower()}")
print(f"Büyük Harf: {metin_ornek.upper()}")
print(f"Değiştir: {metin_ornek.replace('Python', 'Java')}")


# -----------------------------------------------------------------
# --- 4. Koşullu İfadeler (if-elif-else) ---
# -----------------------------------------------------------------
# Programın akışını belirli koşullara göre yönlendirmemizi sağlar.

yas = 80 

if yas < 18: 
    print("Reşit değilsiniz.")
elif yas < 65 :
    print("Reşitsiniz.")
else :
    print("Emeklisiniz.")


# -----------------------------------------------------------------
# --- 5. Döngüler (Loops) ---
# -----------------------------------------------------------------
# Tekrarlı işlemleri otomatikleştirmek için kullanılır.

print("\n--- FOR Döngüsü (range) ---")
# 5.1. `for` Döngüsü
# range(başlangıç, bitiş, adım)
# Not: 'bitiş' değeri dahil değildir.
for i in range(1, 10, 2):  # 1'den başla, 10'a kadar (10 hariç), 2'şer atla
    print("Merhaba", i)  

print("\n--- FOR Döngüsü (liste) ---")
# Bir liste üzerinde gezinme
meyveler = ["elma", "armut", "muz"]

for meyve in meyveler:
    print(meyve)

print("\n--- WHILE Döngüsü ---")
# 5.2. `while` Döngüsü
# Belirli bir koşul doğru olduğu sürece (True) çalışmaya devam eder.
sayi = 0
while sayi < 5:
    print("Sayı:", sayi)
    sayi += 1 # Bu satır olmazsa döngü sonsuza kadar çalışır!

print("\n--- Döngü Pratiği (Tek/Çift) ---")
# 5.3. Döngü Pratiği: Tek/Çift Sayılar
# Mod alma (`%`) operatörünü `if-else` ve `for` döngüsü ile birleştirelim.
for sayi_tekcift in range(1, 21): # 1'den 20'ye kadar (20 dahil)
    if sayi_tekcift % 2 == 0: # Sayının 2'ye bölümünden kalan 0 ise
        print(f"{sayi_tekcift} çifttir.")
    else:
        print(f"{sayi_tekcift} tektir.")


# -----------------------------------------------------------------
# --- 6. Temel Veri Yapıları (Data Structures) ---
# -----------------------------------------------------------------
# Birden fazla veriyi bir arada tutmamızı sağlayan yapılardır.

print("\n--- 6.1. Listeler (Lists) ---")
# Sıralıdır, değiştirilebilir ve farklı veri tiplerini barındırabilir. `[]`
notlar = [85, 90, 78, 92, 88]
print(f"Orijinal liste: {notlar}")

# Eleman ekleme
notlar.append(95)
print(f"Ekleme sonrası: {notlar}")

# Eleman çıkarma
notlar.remove(78)
print(f"Silme sonrası: {notlar}")


print("\n--- 6.2. Sözlükler (Dictionaries) ---")
# Sırasızdır (modern Python'da sıralı), `anahtar-değer` (key-value) çiftleri. `{}`
ogrenci = {
    "ad": "Onur",
    "soyad": "Ejder",
    "yas": 25
}

print(ogrenci)
# Değere anahtar ile erişim
print(f"Öğrencinin adı: {ogrenci['ad']}")


print("\n--- 6.3. Demetler (Tuples) ---")
# Listelere benzer ancak **değiştirilemezler** (immutable). `()`
koordinat = (10, 20)
print(koordinat)

# Elemana erişim
print(f"X koordinatı: {koordinat[0]}")
# Bu kod HATA verir:
# koordinat[0] = 15 # TypeError: 'tuple' object does not support item assignment


print("\n--- 6.4. Kümeler (Sets) ---")
# Sırasızdır ve **benzersiz** (unique) elemanlar içerir. `{}`
benzersiz_kume = {1, 2, 3, 4, 5, 5, 5, 4, 4, 3, 2, 1}

# Tekrarlı elemanlar otomatik olarak kaldırılır
print(benzersiz_kume)