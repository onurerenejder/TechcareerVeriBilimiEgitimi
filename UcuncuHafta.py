"""
Bu derste, NumPy kütüphanesini tüm temel ve orta seviye detaylarıyla 
inceleyeceğiz.

KONULAR:
---------
1.  GİRİŞ: NumPy Nedir? Neden Hızlıdır? (ndarray objesi)
2.  TEMEL ARRAY OLUŞTURMA:
    - Listeden: `np.array()`
    - Fonksiyonlarla: `np.arange()`, `np.zeros()`, `np.ones()`
    - Aralıklar: `np.linspace()`, `np.logspace()`
    - Özel Matrisler: `np.eye()`, `np.diag()`, `np.full()`
3.  RASTGELE SAYI ÜRETİMİ (np.random):
    - Uniform Dağılım: `np.random.rand()`, `np.random.uniform()`
    - Normal Dağılım: `np.random.randn()`
    - Tamsayılar: `np.random.randint()`
    - Karıştırma ve Seçim: `np.random.shuffle()`, `np.random.choice()`
4.  ARRAY ÖZELLİKLERİ VE VERİ TİPLERİ (Attributes & Dtypes):
    - Temel Özellikler: `.shape`, `.ndim`, `.size`, `.dtype`
    - Veri Tipi Değiştirme: `.astype()`
5.  YENİDEN ŞEKİLLENDİRME (Reshaping):
    - `.reshape()`
    - Düzleştirme: `.ravel()`, `.flatten()`
6.  INDEXING VE SLICING (Erişim ve Dilimleme):
    - 1D Array'ler
    - 2D Array'ler (Matrisler) [satır, sütun]
    - Slicing ile Alt Matrisler Oluşturma
    - Slicing'in Kopyalama Davranışı (View vs. Copy)
7.  FANCY INDEXING (Süslü İndeksleme):
    - Liste ile Eleman Seçme
8.  BOOLEAN INDEXING (Koşullu Filtreleme):
    - Tek Koşul
    - Çoklu Koşul (`&`, `|`, `~`)
    - `np.where()` kullanımı
9.  VEKTÖREL OPERASYONLAR (Universal Functions - ufunc):
    - Skaler İşlemler
    - İki Array Arası İşlemler
    - Matematiksel Fonksiyonlar (`np.sqrt`, `np.exp`, `np.log`...)
10. BROADCASTING (Yayınlama):
    - NumPy'ın farklı boyutlardaki array'lerle işlem yapabilme yeteneği
11. İSTATİSTİKSEL OPERASYONLAR (Aggregation):
    - `.sum()`, `.mean()`, `.std()`, `.var()`
    - `.min()`, `.max()`
    - `.argmin()`, `.argmax()` (Indexleri bulma)
    - `.cumsum()`, `.cumprod()` (Kümülatif işlemler)
12. `axis` PARAMETRESİ (Satır/Sütun Bazlı İşlemler):
    - `axis=0` (Sütunlar boyunca)
    - `axis=1` (Satırlar boyunca)
13. MATEMATİKSEL İŞLEMLER VE LİNEER CEBİR:
    - Matris Çarpımı: `.dot()` veya `@` operatörü
    - Determinant, Tıraspoze (Transpose), Ters (Inverse)
14. ARRAY BİRLEŞTİRME VE PARÇALAMA:
    - Birleştirme: `np.concatenate()`, `np.vstack()`, `np.hstack()`
    - Parçalama: `np.split()`, `np.vsplit()`, `np.hsplit()`
"""

# -----------------------------------------------------------------
# --- 1. GİRİŞ: KURULUM VE IMPORT ETME ---
# -----------------------------------------------------------------
# NumPy import
import numpy as np

# Performans karşılaştırması
import time

# Python list ile toplama
python_list = list(range(1000000))
start = time.time()
toplam = sum(python_list)
print(f"Python list: {time.time() - start:.6f} saniye")

# NumPy array ile toplama
numpy_array = np.array(range(1000000))
start = time.time()
toplam = np.sum(numpy_array)
print(f"NumPy array: {time.time() - start:.6f} saniye")

print("\nNumPy daha hızlı!")
import numpy as np
print(f"NumPy Versiyonu: {np.__version__}")

# NumPy 'ndarray' objesi, C dilinde yazılmış, hafızada bitişik (contiguous)
# bloklarda tutulan bir veri yapısıdır. Python listeleri ise işaretçilerden
# (pointer) oluşur ve veriler hafızada dağınık olabilir.
# NumPy'ın hızı buradan gelir.

# -----------------------------------------------------------------
# --- 2. TEMEL ARRAY OLUŞTURMA ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n2. TEMEL ARRAY OLUŞTURMA\n" + "="*30)

# Python listesinden 1D Array (Vektör)
arr1 = np.array([1, 2, 3, 4, 5])
print(f"1D Array:\n{arr1}")

# Python iç içe listesinden 2D Array (Matris)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:\n{arr2}")

# `np.arange(start, stop, step)`
# Belirtilen aralıkta dizi oluşturur (stop dahil değil)
arr_arange = np.arange(0, 10, 2)
print(f"arange(0, 10, 2):\n{arr_arange}")

# `np.zeros(shape)`
# Belirtilen boyutta sıfırlardan oluşan array
arr_zeros = np.zeros((2, 3)) # 2 satır, 3 sütun
print(f"zeros((2, 3)):\n{arr_zeros}")

# `np.ones(shape)`
# Belirtilen boyutta birlerden oluşan array
arr_ones = np.ones((3, 2))
print(f"ones((3, 2)):\n{arr_ones}")

# `np.linspace(start, stop, num)`
# Başlangıç ve bitiş arasında (ikisi de dahil) 'num' adet eşit aralıklı sayı
arr_lin = np.linspace(0, 1, 5) # 0, 0.25, 0.5, 0.75, 1.0
print(f"linspace(0, 1, 5):\n{arr_lin}")

# `np.logspace(start, stop, num)`
# 10^start ve 10^stop arasında 'num' adet logaritmik aralıklı sayı
arr_log = np.logspace(0, 2, 3) # 10^0, 10^1, 10^2 -> [1., 10., 100.]
print(f"logspace(0, 2, 3):\n{arr_log}")

# `np.full(shape, fill_value)`
# Belirtilen boyutta ve belirtilen değerle doldurulmuş array
arr_full = np.full((2, 4), 7)
print(f"full((2, 4), 7):\n{arr_full}")

# `np.eye(N)`
# N x N boyutlu birim matris (Identity matrix)
arr_eye = np.eye(3)
print(f"eye(3):\n{arr_eye}")

# `np.diag(list)`
# Verilen listeyi bir matrisin köşegenine yerleştirir
arr_diag = np.diag([1, 5, 9])
print(f"diag([1, 5, 9]):\n{arr_diag}")


# -----------------------------------------------------------------
# --- 3. RASTGELE SAYI ÜRETİMİ (np.random) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n3. RASTGELE SAYI ÜRETİMİ\n" + "="*30)
# Sonuçların tekrarlanabilir olması için 'seed' (tohum) ayarlanır
np.random.seed(42) # 42, sektörde bir gelenektir :)

# `np.random.rand(d0, d1, ...)`
# 0 ile 1 arasında uniform dağılımlı sayılar
arr_rand = np.random.rand(2, 3)
print(f"rand(2, 3) (0-1 arası):\n{arr_rand}")

# `np.random.randn(d0, d1, ...)`
# Ortalama 0, Standart Sapma 1 olan normal (gaussian) dağılım
arr_randn = np.random.randn(2, 3)
print(f"randn(2, 3) (Normal dağılım):\n{arr_randn}")

# `np.random.randint(low, high, size)`
# 'low' (dahil) ile 'high' (hariç) arası rastgele tamsayılar
arr_randint = np.random.randint(10, 20, size=(3, 4))
print(f"randint(10, 20, size=(3, 4)):\n{arr_randint}")

# `np.random.shuffle(array)`
# Array'i yerinde (in-place) karıştırır. Geriye bir şey döndürmez.
a = np.arange(10)
print(f"Shuffle öncesi: {a}")
np.random.shuffle(a)
print(f"Shuffle sonrası: {a}")

# `np.random.choice(array, size, replace=True)`
# Bir array'den rastgele seçim yapar
# `replace=False` -> Bir eleman sadece bir kez seçilebilir
choices = np.random.choice(a, 5, replace=False)
print(f"Rastgele 5 seçim (tekrarsız): {choices}")


# -----------------------------------------------------------------
# --- 4. ARRAY ÖZELLİKLERİ VE VERİ TİPLERİ ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n4. ARRAY ÖZELLİKLERİ VE VERİ TİPLERİ\n" + "="*30)
data = np.random.randint(0, 10, (3, 5))
print(f"Veri:\n{data}")

# `.shape`: Boyut (satır, sütun) -> (3, 5)
print(f"Shape (Boyut): {data.shape}")

# `.ndim`: Boyut sayısı -> 2
print(f"ndim (Boyut sayısı): {data.ndim}")

# `.size`: Toplam eleman sayısı -> 15
print(f"size (Toplam eleman): {data.size}")

# `.dtype`: İçeride tutulan verinin tipi
print(f"dtype (Veri Tipi): {data.dtype}")

# Veri Tipi Belirleme ve Değiştirme
# Oluştururken tipi belirleme (hafıza yönetimi için önemli)
arr_float = np.array([1, 2, 3], dtype=np.float32)
print(f"Float32 Array: {arr_float}, Tipi: {arr_float.dtype}")

# `.astype()`: Varolan bir array'in tipini değiştirme
arr_int = arr_float.astype(np.int64)
print(f"Int64'e dönüştü: {arr_int}, Tipi: {arr_int.dtype}")


# -----------------------------------------------------------------
# --- 5. YENİDEN ŞEKİLLENDİRME (Reshaping) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n5. YENİDEN ŞEKİLLENDİRME\n" + "="*30)
a = np.arange(1, 13) # 12 eleman
print(f"Orijinal 1D Array: {a}")

# `.reshape(yeni_boyut)`
# Toplam eleman sayısı (size) değişmemeli (3*4 = 12)
b = a.reshape(3, 4)
print(f"Reshape (3, 4):\n{b}")

# `-1` kullanımı: Bilinmeyen boyutu NumPy'ın hesaplamasını sağlar
# 12 elemanlı array'i 2 satırlı yap, sütunu sen hesapla (12/2=6)
c = a.reshape(2, -1)
print(f"Reshape (2, -1):\n{c}")

# Düzleştirme (Matrisi tekrar vektöre çevirme)
# `.ravel()`: Orijinal verinin bir "görünümünü" (view) döndürür. Hızlıdır.
d = b.ravel()
print(f"ravel() ile düzleştirme: {d}")

# `.flatten()`: Verinin bir "kopyasını" (copy) döndürür. Daha güvenlidir.
e = b.flatten()
print(f"flatten() ile düzleştirme: {e}")


# -----------------------------------------------------------------
# --- 6. INDEXING VE SLICING (Erişim ve Dilimleme) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n6. INDEXING VE SLICING\n" + "="*30)

# --- 6.1. 1D Array'ler ---
arr1d = np.arange(10, 20)
print(f"\n1D Array: {arr1d}")
print(f"İlk eleman [0]: {arr1d[0]}")
print(f"Son eleman [-1]: {arr1d[-1]}")
print(f"Dilimleme [2:5]: {arr1d[2:5]}") # 2. index'ten 5. (hariç)
print(f"Tersten yazdırma [::-1]: {arr1d[::-1]}")

# --- 6.2. 2D Array'ler (Matrisler) ---
# Format: `array[satır, sütun]` (En çok kullanılan)
# veya `array[satır][sütun]` (Daha yavaş, önerilmez)
arr2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(f"\n2D Array:\n{arr2d}")

# Tek eleman (2. satır, 3. sütun -> 60)
print(f"[1, 2] -> {arr2d[1, 2]}")

# Tek satır (1. satırın tamamı)
print(f"[0, :] (veya [0]) -> {arr2d[0, :]}")

# Tek sütun (2. sütunun tamamı)
print(f"[:, 1] -> {arr2d[:, 1]}")

# Alt matris dilimleme (İlk 2 satır ve son 2 sütun)
# [[20, 30], [50, 60]]
alt_matris = arr2d[0:2, 1:3]
print(f"Alt Matris [0:2, 1:3]:\n{alt_matris}")

# --- 6.3. Slicing: View vs. Copy (ÇOK ÖNEMLİ!) ---
# NumPy'da dilimleme (slicing) bir KOPYA (copy) oluşturmaz,
# ana verinin bir GÖRÜNÜMÜNÜ (view) döndürür. Bu, hafızadan tasarruf sağlar.
print("\n--- View vs. Copy ---")
alt_gorunum = arr2d[0:2, 0:2]
print(f"Orijinal alt görünüm:\n{alt_gorunum}")

# Alt görünümde bir değişiklik yapalım
alt_gorunum[0, 0] = 999
print(f"Değiştirilmiş alt görünüm:\n{alt_gorunum}")

# ANA ARRAY DE DEĞİŞİR!
print(f"DEĞİŞİM SONRASI ANA ARRAY:\n{arr2d}") # 10 yerine 999 yazar

# Eğer kopya (copy) isteniyorsa, `.copy()` metodu açıkça çağrılmalıdır
arr2d_kopya = arr2d.copy()
arr2d_kopya[0, 0] = 111 # Sadece kopyayı değiştirir
print(f"Orijinal array (değişmedi):\n{arr2d}")
print(f"Kopya array (değişti):\n{arr2d_kopya}")


# -----------------------------------------------------------------
# --- 7. FANCY INDEXING (Süslü İndeksleme) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n7. FANCY INDEXING\n" + "="*30)
# Bir array'den belirli index'teki elemanları (sırasız olsa bile)
# bir liste veya array kullanarak seçmek.
# Bu işlem her zaman bir KOPYA döndürür (View değil).
f_arr = np.arange(100, 110)
print(f"Fancy Array: {f_arr}")
indexler = [1, 3, 5, 0]
print(f"Seçilenler [1, 3, 5, 0]: {f_arr[indexler]}")

# 2D'de Fancy Indexing
f_arr2d = np.random.randint(10, 100, (4, 4))
print(f"\nFancy 2D Array:\n{f_arr2d}")
# 0. ve 2. satırları al
print(f"0. ve 2. Satırlar:\n{f_arr2d[[0, 2]]}")
# (0,1), (2,3) ve (3,0) koordinatlarındaki elemanları al
print(f"Belirli koordinatlar: {f_arr2d[[0, 2, 3], [1, 3, 0]]}")


# -----------------------------------------------------------------
# --- 8. BOOLEAN INDEXING (Koşullu Filtreleme) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n8. BOOLEAN INDEXING (Filtreleme)\n" + "="*30)
# Veri analizinde filtreleme için en çok kullanılan tekniktir.
b_data = np.random.randint(1, 50, (4, 5))
print(f"Filtre Verisi:\n{b_data}")

# Adım 1: Koşulu oluştur (True/False'lardan oluşan bir matris döner)
kosul = b_data > 30
print(f"Koşul (Veri > 30):\n{kosul}")

# Adım 2: Koşulu uygula (Sadece True olanları 1D bir array olarak döndürür)
print(f"30'dan büyük elemanlar: {b_data[kosul]}")

# Kısa yol (en çok kullanılan):
print(f"30'dan büyükler (kısa yol): {b_data[b_data > 30]}")

# Çoklu Koşul: `&` (ve), `|` (veya), `~` (değil - not)
# Python'daki `and`, `or` kullanılmaz! Parantezler zorunludur!
kosul1 = b_data > 20
kosul2 = b_data < 40
print(f"20 ile 40 arasındaki elemanlar:\n{b_data[(kosul1) & (kosul2)]}")
print(f"20'den küçük VEYA 40'tan büyük elemanlar:\n{b_data[~(kosul1 & kosul2)]}") # (Değili)

# `np.where(koşul, doğruysa_bu, yanlışsa_bu)`
# Excel'deki IF fonksiyonu gibidir.
# 20'den büyükse 1, değilse 0 yaz
where_sonuc = np.where(b_data > 20, 1, 0)
print(f"np.where(b_data > 20, 1, 0):\n{where_sonuc}")


# -----------------------------------------------------------------
# --- 9. VEKTÖREL OPERASYONLAR (Universal Functions - ufunc) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n9. VEKTÖREL OPERASYONLAR (ufunc)\n" + "="*30)
v_arr = np.arange(1, 6) # [1, 2, 3, 4, 5]

# Skaler (tekil sayı) ile işlemler (Döngüye gerek yok!)
print(f"v_arr + 100 = {v_arr + 100}")
print(f"v_arr * 3   = {v_arr * 3}")
print(f"v_arr ** 2  = {v_arr ** 2}")

# İki Array arası işlemler (Boyutlar eşleşmeli)
v_arr2 = np.ones(5) * 10 # [10, 10, 10, 10, 10]
print(f"v_arr + v_arr2 = {v_arr + v_arr2}")
print(f"v_arr / v_arr2 = {v_arr / v_arr2}")

# Matematiksel Fonksiyonlar
print(f"Karekök: {np.sqrt(v_arr)}")
print(f"Üstel (e^x): {np.exp(v_arr)}")
print(f"Doğal Log (ln): {np.log(v_arr)}")


# -----------------------------------------------------------------
# --- 10. BROADCASTING (Yayınlama) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n10. BROADCASTING\n" + "="*30)
# NumPy'ın farklı boyutlardaki array'lerle işlem yapabilme yeteneğidir.
# Küçük olan array, büyük olanın boyutuna "yayınlanır" (genişletilir).
matris = np.ones((3, 3)) # 3x3 matris
vektor = np.array([1, 2, 3]) # 1x3 vektör

print(f"Matris:\n{matris}")
print(f"Vektör: {vektor}")

# Vektör [1, 2, 3], 3 satıra da kopyalanarak (yayınlanarak) toplanır
# [[1, 1, 1] + [1, 2, 3]]
# [[1, 1, 1] + [1, 2, 3]]
# [[1, 1, 1] + [1, 2, 3]]
print(f"Matris + Vektör (Broadcasting):\n{matris + vektor}")

# Sütun bazlı broadcasting için vektörün shape'i (3, 1) olmalı
vektor_sutun = np.array([10, 20, 30]).reshape(3, 1)
print(f"\nSütun Vektörü:\n{vektor_sutun}")
print(f"Matris + Sütun Vektörü:\n{matris + vektor_sutun}")


# -----------------------------------------------------------------
# --- 11. İSTATİSTİKSEL OPERASYONLAR (Aggregation) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n11. İSTATİSTİKSEL OPERASYONLAR\n" + "="*30)
stats_data = np.random.randint(1, 100, 10)
print(f"İstatistik Verisi: {stats_data}")

print(f"Toplam (sum): {stats_data.sum()}")
print(f"Ortalama (mean): {stats_data.mean()}")
print(f"Standart Sapma (std): {stats_data.std()}")
print(f"Varyans (var): {stats_data.var()}")
print(f"Minimum (min): {stats_data.min()}")
print(f"Maksimum (max): {stats_data.max()}")

# `.argmin()` ve `.argmax()`: Min/Max değerlerin index'ini verir
print(f"Minimum değerin index'i (argmin): {stats_data.argmin()}")
print(f"Maksimum değerin index'i (argmax): {stats_data.argmax()}")

# Kümülatif (Birikimli) Toplam/Çarpım
print(f"Kümülatif Toplam (cumsum): {stats_data.cumsum()}")


# -----------------------------------------------------------------
# --- 12. `axis` PARAMETRESİ (Satır/Sütun Bazlı İşlemler) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n12. 'axis' PARAMETRESİ\n" + "="*30)
# NumPy'da en kritik konseptlerden biri.
# `axis=0` -> Sütunlar boyunca (dikey) işlem. (Satırları 'çöktürür')
# `axis=1` -> Satırlar boyunca (yatay) işlem. (Sütunları 'çöktürür')

axis_matris = np.array([[1, 2, 3], [10, 20, 30]])
print(f"Axis Matrisi:\n{axis_matris}")

# Sütunların toplamı (axis=0) -> [1+10, 2+20, 3+30]
print(f"Sütun Toplamları (axis=0): {axis_matris.sum(axis=0)}")

# Satırların toplamı (axis=1) -> [1+2+3, 10+20+30]
print(f"Satır Toplamları (axis=1): {axis_matris.sum(axis=1)}")

# Sütunların ortalaması (axis=0)
print(f"Sütun Ortalamaları (axis=0): {axis_matris.mean(axis=0)}")


# -----------------------------------------------------------------
# --- 13. MATEMATİKSEL İŞLEMLER VE LİNEER CEBİR ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n13. LİNEER CEBİR\n" + "="*30)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Element-wise çarpma (Hadamard Product)
print(f"Element-wise Çarpma (A * B):\n{A * B}")

# Matris Çarpımı (Dot Product)
# Yöntem 1: `.dot()`
print(f"Matris Çarpımı (A.dot(B)):\n{A.dot(B)}")
# Yöntem 2: `@` operatörü (Python 3.5+)
print(f"Matris Çarpımı (A @ B):\n{A @ B}")

# Transpoze (Satır ve sütunların yerini değiştirme)
print(f"A'nın Transpozesi (A.T):\n{A.T}")

# Determinant
print(f"A'nın Determinantı: {np.linalg.det(A)}")

# Ters (Inverse)
print(f"A'nın Tersi (Inverse):\n{np.linalg.inv(A)}")


# -----------------------------------------------------------------
# --- 14. ARRAY BİRLEŞTİRME VE PARÇALAMA ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n14. ARRAY BİRLEŞTİRME VE PARÇALAMA\n" + "="*30)

# --- 14.1. Birleştirme ---
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Dikey Birleştirme (Alt alta)
# `np.concatenate` (axis=0 ile)
print(f"Concatenate (axis=0):\n{np.concatenate((a, b), axis=0)}")
# veya `np.vstack` (Vertical Stack)
print(f"vstack:\n{np.vstack((a, b))}")

# Yatay Birleştirme (Yan yana)
# `np.concatenate` (axis=1 ile)
print(f"Concatenate (axis=1):\n{np.concatenate((a, b), axis=1)}")
# veya `np.hstack` (Horizontal Stack)
print(f"hstack:\n{np.hstack((a, b))}")

# --- 14.2. Parçalama (Splitting) ---
c = np.arange(1, 10) # [1, 2, ..., 9]
print(f"\nParçalanacak Array: {c}")

# 3 eşit parçaya böl
print(f"3 eşit parçaya böl: {np.split(c, 3)}")

# Belirli noktalardan böl (2. ve 5. index'ten)
print(f"Belirli noktalardan böl: {np.split(c, [2, 5])}")

# `vsplit` (dikey) ve `hsplit` (yatay) matrisler için kullanılır
d = np.arange(16).reshape(4, 4)
print(f"\nParçalanacak Matris:\n{d}")
print(f"vsplit (2 eşit parçaya):\n{np.vsplit(d, 2)}")
print(f"hsplit (2 eşit parçaya):\n{np.hsplit(d, 2)}")


