import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Stil Ayarı:
# Grafiklerimizin daha modern ve estetik görünmesi için hazır bir stil şablonu kullanıyoruz.
# 'seaborn-v0_8-darkgrid' stili, arka plana hafif bir ızgara ekler ve renkleri yumuşatır.
plt.style.use('seaborn-v0_8-darkgrid') 

# =============================================================================
# BÖLÜM 1: GİRİŞ VE TEMEL KAVRAMLAR (STATE-MACHINE ARAYÜZÜ)
# =============================================================================
# Bu yaklaşım "plt." ile başlar. Hızlı ve basit çizimler içindir.
# Mantık şudur: "Elimde tek bir tuval var, verdiğim her komutu o anki tuvale işle."

print("--- BÖLÜM 1: Temel Çizim ---")

# Veri Hazırlığı
gunler = np.array([1, 2, 3, 4, 5, 6, 7])
sicaklik = np.array([20, 22, 21, 25, 30, 28, 24])

# 1. Tuval (Figure) Oluşturma
# figsize=(8, 5) -> Grafiğin boyutunu belirler (Genişlik: 8 inç, Yükseklik: 5 inç).
plt.figure(figsize=(8, 5)) 

# 2. Çizim Komutu (Plot)
# plt.plot(x_ekseni, y_ekseni, özellikler...)
plt.plot(gunler, sicaklik, 
         color='crimson',       # Çizgi Rengi (İsim 'red' veya hex '#ff0000' olabilir)
         linestyle='--',        # Çizgi Stili ('--': kesikli, '-': düz, ':': noktalı)
         linewidth=2,           # Çizgi Kalınlığı
         marker='o',            # İşaretçi (Veri noktalarına 'o' yani daire koyar)
         markersize=10,         # İşaretçinin boyutu
         markerfacecolor='white', # İşaretçinin iç dolgu rengi (beyaz)
         label='Sıcaklık Verisi') # Lejant (Legend) için etiket ismi

# 3. Etiketler ve Başlıklar
plt.title("Haftalık Sıcaklık Değişimi", fontsize=16) # Ana Başlık
plt.xlabel("Günler", fontsize=12)                    # X Ekseni Yazısı
plt.ylabel("Derece (°C)", fontsize=12)               # Y Ekseni Yazısı

# 4. Yardımcı Elemanlar
# loc="upper left" -> Kutucuğu sol üst köşeye yerleştirir.
plt.legend(loc="upper left") 

# alpha=0.5 -> Izgarayı %50 şeffaf yapar ki grafiğin önüne geçmesin.
plt.grid(True, alpha=0.5)    

# 5. Gösterme
# Bu komut yazılana kadar grafik hafızada tutulur, bu komutla ekrana basılır.
plt.show()


# =============================================================================
# BÖLÜM 2: PROFESYONEL YAKLAŞIM (NESNE YÖNELİMLİ - OOP)
# =============================================================================
# Matplotlib'in asıl gücü buradadır. Profesyonel dünyada %90 bu yöntem kullanılır.
# İKİ ANA NESNE VARDIR:
# 1. Figure (fig): Tüm pencere, çerçevenin tamamı (Duvar tablosunun çerçevesi).
# 2. Axes (ax): Grafiğin çizildiği alan (Resmin kendisi).

print("\n--- BÖLÜM 2: Nesne Yönelimli Yaklaşım (Figure & Axes) ---")

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# plt.subplots() bize hem çerçeveyi (fig) hem de resmi (ax) aynı anda verir.
fig, ax = plt.subplots(figsize=(10, 6))

# ARTIK "plt.plot" YOK! "ax.plot" VAR.
# "ax nesnesinin üzerine çiz" diyoruz. Birden fazla grafik olduğunda karışıklığı önler.
ax.plot(x, y1, label='Sinüs', color='blue')
ax.plot(x, y2, label='Kosinüs', color='orange', linestyle='-.')

# AYARLAR (Dikkat: OOP'de komutların başına genelde 'set_' gelir)
ax.set_title("Trigonometrik Fonksiyonlar (OOP Yaklaşımı)") # plt.title yerine
ax.set_xlabel("Radyan")
ax.set_ylabel("Genlik")

# Eksen sınırlarını manuel belirleme (Zoom yapmak gibi)
ax.set_ylim(-1.5, 1.5) # Y ekseni sadece -1.5 ile 1.5 arasını göstersin

ax.legend()
plt.show()


# =============================================================================
# BÖLÜM 3: TEMEL GRAFİK TÜRLERİ
# =============================================================================
print("\n--- BÖLÜM 3: Grafik Türleri ---")

# --- 3.1. Scatter Plot (Dağılım Grafiği) ---
# İki sayısal değişken arasındaki ilişkiyi (Korelasyon) görmek için kullanılır.
gelir = np.random.randint(20000, 50000, 50)
# Harcama, gelire bağlı olsun ama biraz da rastgelelik (gürültü) ekleyelim
harcama = gelir * 0.6 + np.random.randint(-2000, 2000, 50) 

fig, ax = plt.subplots(figsize=(8, 5))

# alpha=0.6 -> Noktalar üst üste binerse yoğunluğu görebilmek için şeffaflık verilir.
# s=50 -> Noktaların boyutu (size).
ax.scatter(gelir, harcama, color='purple', alpha=0.6, s=50) 

ax.set_title("Gelir vs Harcama İlişkisi (Scatter)")
ax.set_xlabel("Gelir")
ax.set_ylabel("Harcama")
plt.show()


# --- 3.2. Bar Plot (Sütun Grafiği) ---
# Kategorik verileri (Sınıflar, Aylar, Şehirler vb.) kıyaslamak için kullanılır.
kategoriler = ['A Sınıfı', 'B Sınıfı', 'C Sınıfı', 'D Sınıfı']
degerler = [85, 70, 95, 60]

fig, ax = plt.subplots(figsize=(8, 5))
# color listesi vererek her sütunu farklı renk yapabiliriz.
barlar = ax.bar(kategoriler, degerler, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

ax.set_title("Sınıf Ortalamaları (Bar)")

# ax.bar_label -> Sütunların tepesine değerlerini otomatik yazar (Matplotlib 3.4+ özelliği).
# padding=3 -> Yazının çubuktan ne kadar yukarıda olacağı.
ax.bar_label(barlar, padding=3) 
plt.show()


# --- 3.3. Histogram ---
# Bir verinin dağılımını (Frekansını) görmek için kullanılır.
# Örneğin: "Sınıftaki notlar en çok hangi aralıkta yığılmış?"
veri_dagilimi = np.random.randn(1000) # 1000 adet normal dağılımlı (çan eğrisi) sayı

fig, ax = plt.subplots(figsize=(8, 5))
# bins=30 -> Veriyi 30 eşit parçaya (kutuya) böl. 
# Çok az olursa detay kaybolur, çok fazla olursa grafik gürültülü olur.
ax.hist(veri_dagilimi, bins=30, color='teal', edgecolor='black', alpha=0.7)
ax.set_title("Veri Dağılımı (Histogram)")
plt.show()


# =============================================================================
# BÖLÜM 4: ÇOKLU GRAFİKLER (SUBPLOTS)
# =============================================================================
# Tek bir pencerede birden fazla grafik göstermek.
print("\n--- BÖLÜM 4: Alt Grafikler (Subplots) ---")

# nrows=2, ncols=2 -> 2'ye 2'lik bir ızgara oluştur. Toplam 4 grafik.
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# 'ax' artık tek bir nesne değil, 2x2'lik bir listedir (NumPy array).
# Erişim sağlamak için indeks kullanırız: ax[satır, sütun]

# Sol Üst (0,0) - Çizgi
ax[0, 0].plot(x, y1, 'r')
ax[0, 0].set_title("Çizgi Grafiği")

# Sağ Üst (0,1) - Scatter
ax[0, 1].scatter(np.random.rand(50), np.random.rand(50), color='g')
ax[0, 1].set_title("Dağılım Grafiği")

# Sol Alt (1,0) - Bar
ax[1, 0].bar(['X', 'Y', 'Z'], [10, 20, 15], color='b')
ax[1, 0].set_title("Bar Grafiği")

# Sağ Alt (1,1) - Histogram
ax[1, 1].hist(np.random.randn(100), bins=10, color='purple')
ax[1, 1].set_title("Histogram")

# suptitle -> "Super Title". Tüm figürün ana başlığı.
plt.suptitle("Tüm Grafikler Bir Arada", fontsize=20) 

# tight_layout -> Grafikler yan yana geldiğinde yazıların birbirine girmesini engeller.
# Boşlukları otomatik ayarlar.
plt.tight_layout() 
plt.show()


# =============================================================================
# BÖLÜM 5: İLERİ SEVİYE TEKNİKLER
# =============================================================================
print("\n--- BÖLÜM 5: İleri Teknikler ---")

# --- 5.1. Çift Eksen (Twin Axis) ---
# Farklı birimdeki (örn: Derece ve Milimetre) iki veriyi üst üste göstermek.
aylar = np.arange(1, 13)
sicaklik_veri = [5, 7, 12, 16, 20, 25, 29, 28, 22, 16, 10, 6]
yagis_veri = [100, 90, 80, 50, 30, 10, 5, 10, 40, 60, 90, 110]

fig, ax1 = plt.subplots(figsize=(10, 5))

# Sol Eksen (ax1) - Sıcaklık
ax1.plot(aylar, sicaklik_veri, 'r-o', label='Sıcaklık')
ax1.set_xlabel('Aylar')
ax1.set_ylabel('Sıcaklık (°C)', color='red')
# tick_params -> Eksen üzerindeki sayıların rengini değiştirir.
ax1.tick_params(axis='y', labelcolor='red') 

# Sağ Eksen (ax2) - Yağış
# twinx() -> ax1'in X eksenini paylaşan ama Y ekseni bağımsız olan yeni bir eksen yaratır.
ax2 = ax1.twinx() 
ax2.bar(aylar, yagis_veri, alpha=0.3, color='blue', label='Yağış')
ax2.set_ylabel('Yağış (mm)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

plt.title("İstanbul İklim Grafiği (Çift Eksen)")
plt.show()


# --- 5.2. Grafik İçinde Grafik (Inset Plot) ---
# Bir detayı büyütmek (Zoom) için kullanılır.
x = np.linspace(0, 10, 100)
y = np.exp(x)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color='black')
ax.set_title("Ana Grafik")

# add_axes([sol, alt, genişlik, yükseklik])
# Değerler 0 ile 1 arasındadır (Yüzde gibi: %20 soldan, %50 alttan başla...)
ax_ic = fig.add_axes([0.2, 0.5, 0.3, 0.3]) 
ax_ic.plot(x, y, color='red')
ax_ic.set_xlim(0, 2) # Sadece 0-2 arasını göster (Zoom)
ax_ic.set_ylim(0, 10)
ax_ic.set_title("Zoom (0-2 Arası)")
plt.show()


# --- 5.3. Annotation (Not Ekleme) ---
# Grafikteki önemli bir noktayı vurgulamak için ok ve metin ekleme.
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, np.sin(x))

# annotate(Metin, Ok_Ucu_Konumu, Metin_Konumu, Ok_Stili)
ax.annotate('Maksimum Nokta', 
            xy=(1.57, 1),           # Okun ucunun değeceği koordinat
            xytext=(3, 1.2),        # Yazının duracağı koordinat
            arrowprops=dict(facecolor='black', shrink=0.05)) # Ok özellikleri

plt.title("Grafik Üzerine Not Ekleme")
plt.show()


# --- 5.4. Isı Haritası (Heatmap) ---
# Matris şeklindeki verileri renklerle ifade etmek.
veri_matrisi = np.random.rand(10, 10)

fig, ax = plt.subplots(figsize=(6, 6))
# imshow -> Matrisi resme dönüştürür.
# cmap='viridis' -> Renk haritası (Koyu mor düşük, sarı yüksek değer).
im = ax.imshow(veri_matrisi, cmap='viridis') 

# colorbar -> Yan tarafa renk skalasını ekler.
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("Değer Skalası", rotation=-90, va="bottom")

ax.set_title("Korelasyon Matrisi / Isı Haritası")
ax.grid(False) # Heatmap'te ızgara çizgileri görüntüyü bozar, kapatıyoruz.
plt.show()


# =============================================================================
# BÖLÜM 6: KAYDETME (EXPORT)
# =============================================================================
print("\n--- BÖLÜM 6: Kaydetme ---")

# fig.savefig komutu grafiği bilgisayara kaydeder.
# dpi=300 -> Çözünürlük (Dots Per Inch). 300 baskı kalitesidir.
# bbox_inches='tight' -> Grafiğin kenarındaki gereksiz beyaz boşlukları otomatik kırpar.

fig.savefig('benim_grafigim.png', dpi=300, bbox_inches='tight')
