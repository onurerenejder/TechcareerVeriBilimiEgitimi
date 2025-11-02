"""
HAFTA 2: İLERİ PYTHON KAVRAMLARI

Bu derste Python'daki temel yapı taşlarını daha derinlemesine inceleyeceğiz:
1.  Fonksiyonlar (def, return)
2.  Modül Kullanımı (math, random, datetime)
3.  Dosya İşlemleri (txt, json)
4.  Hata Yönetimi (try-except)
5.  Liste Üreticileri (List Comprehensions)
"""

# -----------------------------------------------------------------
# --- 1. Fonksiyonlar (Functions) ---
# -----------------------------------------------------------------
# Kod tekrarını önleyen, belirli bir işi yapmak için tasarlanmış kod bloklarıdır.

# Parametre almayan, değer döndürmeyen
def selamla():
    print("Merhaba, nasılsın?")

selamla()

# Parametre alan (isim)
def selamla_isimle(isim):
    print(f"Merhaba {isim}, nasılsın?")

selamla_isimle("Onur")

# Değer döndüren (return)
def topla(a, b):
    return a + b

# Dönen değeri bir değişkene ata
c = topla(3, 5)
print(f"Toplam (c): {c}")

# Dönen değeri doğrudan kullan
print(f"Toplam (direkt): {topla(5, 10)}")
print(f"Toplam (direkt): {topla(20, 30)}")

# Varsayılan (default) parametre
def carp(a, b=2):
    """
    Bu fonksiyon iki sayıyı çarpar. 
    Eğer 'b' değeri verilmezse, 'a'yı 2 ile çarpar.
    """
    return a * b

print(f"Varsayılan Çarpım (b=2): {carp(4)}")
print(f"Değer Verilen Çarpım: {carp(7, 8)}")


# -----------------------------------------------------------------
# --- 2. Lambda Fonksiyonları ---
# -----------------------------------------------------------------
# Küçük, tek satırlık ve isimsiz fonksiyonlardır.

kare = lambda x: x**2
print(f"Lambda ile Kare: {kare(6)}")

# İki parametreli lambda
toplama_lambda = lambda x, y: x + y
print(f"Lambda ile Toplama: {toplama_lambda(10, 5)}")


# -----------------------------------------------------------------
# --- 3. Fonksiyon Pratiği (Ortalama Hesapla) ---
# -----------------------------------------------------------------

def ortalama_hesapla(notlar):
    """Verilen not listesinin ortalamasını hesaplar."""
    if len(notlar) == 0: # Eğer liste boşsa 0 döndür (Sıfıra bölme hatasını önle)
        return 0
    
    toplam = sum(notlar) # Listenin toplamını al
    adet = len(notlar)   # Listedeki eleman sayısını al
    return toplam / adet

notlar_listesi = [85, 90, 78, 92, 88]
ortalama = ortalama_hesapla(notlar_listesi)
print(f"Ortalama Not: {ortalama}")


# -----------------------------------------------------------------
# --- 4. Modül Kullanımı (import) ---
# -----------------------------------------------------------------
# Hazır fonksiyonları ve kütüphaneleri projemize dahil etme.

# Yöntem 1: Tüm modülü import etme
import math

print(f"Pi Sayısı: {math.pi}")
print(f"16'nın Karekökü: {math.sqrt(16)}")
print(f"5 Faktöriyel: {math.factorial(5)}")
print(f"2'nin 3. kuvveti: {math.pow(2, 3)}")

# Yöntem 2: Modülden belirli bir parçayı import etme (from ... import ...)
import random

sayi = random.randint(1, 100) # 1 ve 100 dahil
print(f"Rastgele Sayı: {sayi}")

# 'datetime' modülünden sadece 'datetime' sınıfını al
from datetime import datetime

print(f"Şu anki tarih ve saat: {datetime.now()}")
print(f"Sadece tarih: {datetime.now().date()}")
print(f"Sadece yıl: {datetime.now().year}")


# -----------------------------------------------------------------
# --- 5. Dosya İşlemleri (File I/O) ---
# -----------------------------------------------------------------
# `with open(...)` bloğu, dosya kapatmayı otomatik yapar.

# --- 5.1. Metin (txt) Dosyaları ---

print("\n--- TXT Dosya İşlemleri ---")
# 'w' (write - yazma): Dosyayı oluşturur veya üzerine yazar (içeriği siler)
# 'encoding='utf-8'' -> Türkçe karakterler (İ,ş,ğ) için şarttır.
try:
    with open('merhaba.txt', 'w', encoding='utf-8') as denemeprojem:
        denemeprojem.write('Merhaba Dünya!\n')
        denemeprojem.write('Python ile dosya işlemleri.\n')
    print("'merhaba.txt' dosyası yazıldı.")

    # 'r' (read - okuma): Dosyayı okur
    with open('merhaba.txt', 'r', encoding='utf-8') as denemeprojem:
        icerik = denemeprojem.read()
        print("Dosyanın içeriği:\n" + icerik)

    # 'a' (append - ekleme): Dosyanın sonuna ekleme yapar (içeriği silmez)
    with open('merhaba.txt', 'a', encoding='utf-8') as denemeprojem:
        denemeprojem.write('Bu satır sona eklendi.\n')
    print("'merhaba.txt' dosyasına ekleme yapıldı.")
    
except Exception as e:
    print(f"Dosya hatası oluştu: {e}")


# --- 5.2. JSON (JavaScript Object Notation) Dosyaları ---
# Veri biliminde ve API'lerde çok yaygın kullanılır.
# Python Dictionary (sözlük) yapısına çok benzer.

print("\n--- JSON Dosya İşlemleri ---")
import json 

# Yazılacak Python sözlüğü
kisi = {
    "ad": "Ahmet",
    "soyad": "Yılmaz",
    "yas": 30,
    "hobiler": ["Sinema", "Kitap"]
}

# JSON dosyasına yazma
try:
    with open('kisi.json', 'w', encoding='utf-8') as json_dosya:
        # `json.dump` -> Python dict'i JSON dosyasına yazar
        # `ensure_ascii=False` -> Türkçe karakterleri korur
        # `indent=4` -> Dosyayı 4 boşluklu girintilerle güzel formatlar
        json.dump(kisi, json_dosya, ensure_ascii=False, indent=4)
    print("'kisi.json' dosyası yazıldı.")

    # JSON dosyasından okuma 
    with open('kisi.json', 'r', encoding='utf-8') as json_dosya:
        # `json.load` -> JSON dosyasını okuyup Python dict'ine çevirir
        veri = json.load(json_dosya)
        print("Okunan JSON veri:")
        print(veri)
        print(f"Okunan kişinin adı: {veri['ad']}")
        
except Exception as e:
    print(f"JSON hatası oluştu: {e}")


# -----------------------------------------------------------------
# --- 6. Hata Yönetimi (Try - Except) ---
# -----------------------------------------------------------------
# Programın çökmesini (crash) engelleyen ve hataları yakalayan bloklar.

print("\n--- Try-Except (Sıfıra Bölme) ---")
try:
    sayi1 = int(input("Birinci sayıyı girin (örn: 10): "))
    sayi2 = int(input("İkinci sayıyı girin (örn: 2 veya 0): "))
    sonuc = sayi1 / sayi2
    print(f"Sonuç: {sonuc}")
except ZeroDivisionError:
    # Sadece sıfıra bölme hatasını yakalar
    print("Hata: Bir sayı sıfıra bölünemez.")
except ValueError:
    # Sadece 'int'e çevrilemeyen (örn: "abc") girişleri yakalar
    print("Hata: Lütfen geçerli bir sayı girin.")
except Exception as e:
    # Yukarıdakiler dışındaki tüm hataları yakalar
    print(f"Bilinmeyen bir hata oluştu: {e}")
finally:
    # Hata olsa da olmasa da her zaman çalışır
    print("Sayı bölme işlemi denemesi bitti.")


print("\n--- Try-Except (Dosya Bulunamadı) ---")
try:
    with open('olmayan_dosya.txt', 'r', encoding='utf-8') as dosya:
        icerik = dosya.read()
        print(icerik)
except FileNotFoundError:
    print("Hata: 'olmayan_dosya.txt' isimli dosya bulunamadı.")
except Exception as e:
    print(f"Bilinmeyen bir hata oluştu: {e}")
finally:
    print("Dosya okuma işlemi denemesi tamamlandı.")


# -----------------------------------------------------------------
# --- 7. Liste Üreticileri (List Comprehensions) ---
# -----------------------------------------------------------------
# `for` döngülerini tek satırda yazarak liste oluşturmanın hızlı yolu.

# Yöntem 1: Klasik 'for' döngüsü
cift_sayilar = []
for sayi in range(1, 21):
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)

print(f"Klasik Çift Sayılar: {cift_sayilar}")

# Yöntem 2: List Comprehension (Aynı işi tek satırda yapar)
# [ (yapılacak_iş) for (değişken) in (liste) if (koşul) ]
cift_sayilar2 = [sayi for sayi in range(1, 21) if sayi % 2 == 0]
print(f"List Comp. Çift Sayılar: {cift_sayilar2}")

# Örnek 2: Kareler listesi
kareler = [sayi**2 for sayi in range(1, 11)]
print(f"Kareler: {kareler}")

# Örnek 3: Koşullu atama (if/else)
# (sayi 2'ye bölünüyorsa "Çift", bölünmüyorsa "Tek" yaz)
tek_cift = ["Çift" if sayi % 2 == 0 else "Tek" for sayi in range(1, 11)]
print(f"Tek/Çift Ayrımı: {tek_cift}")

print("\n--- Ders Tamamlandı ---")