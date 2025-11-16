"""
HAFTA 4: PANDAS (PYTHON DATA ANALYSIS LIBRARY) - VERİ MANİPÜLASYONU

Bu derste, veri analizinin ve manipülasyonunun İsviçre çakısı olan
Pandas kütüphanesini detaylıca inceleyeceğiz.

KONULAR:
---------
1.  PANDAS NEDİR? (NumPy vs Pandas)
2.  TEMEL VERİ YAPILARI:
    - `Series` (1D - Etiketli Vektör)
    - `DataFrame` (2D - Etiketli Tablo)
3.  VERİ OKUMA VE YAZMA:
    - `pd.read_csv()` (En önemlisi)
    - `pd.read_excel()`
    - `df.to_csv()`, `df.to_excel()`
4.  VERİYE İLK BAKIŞ (Data Inspection):
    - `.head()`, `.tail()`
    - `.info()` (ÇOK ÖNEMLİ)
    - `.describe()`
    - `.shape`, `.columns`, `.dtypes`
    - `.value_counts()`
5.  SEÇİM VE İNDEKSLEME (Selection & Indexing):
    - Sütun Seçme
    - `.loc[]` (Label-based - İsimle seçim)
    - `.iloc[]` (Integer-based - Sıra no ile seçim)
6.  KOŞULLU FİLTRELEME (Boolean Indexing):
    - Tek ve Çoklu Koşullar (`&`, `|`)
    - `.isin()`
7.  VERİ MANİPÜLASYONU:
    - Yeni Sütun Ekleme
    - Sütun/Satır Silme (`.drop()`)
    - Değer Değiştirme
8.  EKSİK VERİ YÖNETİMİ (Missing Data):
    - `.isnull()`, `.isna()`
    - `.dropna()` (Eksik verileri silme)
    - `.fillna()` (Eksik verileri doldurma)
9.  GROUPBY VE AGREGASYON (Gruplama ve Özetleme):
    - Split-Apply-Combine konsepti
    - `df.groupby()`
    - `.sum()`, `.mean()`, `.count()`
    - `.agg()` (Çoklu agregasyon)
10. BİRLEŞTİRME VE EKLEME (Merging & Concatenating):
    - `pd.concat()` (Alt alta / Yan yana ekleme)
    - `pd.merge()` (SQL'deki JOIN işlemi)
11. DİĞER FAYDALI OPERASYONLAR:
    - `.sort_values()`
    - `.apply()` (Fonksiyon uygulama)
    - `.unique()`, `.nunique()`
    - String Operasyonları (`.str`)
"""

# -----------------------------------------------------------------
# --- 1. GİRİŞ: KURULUM VE IMPORT ETME ---
# -----------------------------------------------------------------
# !pip install pandas
# !pip install openpyxl # Excel okumak için
import pandas as pd
import numpy as np # Pandas, NumPy üzerine kuruludur ve genellikle birlikte kullanılır

print(f"Pandas Versiyonu: {pd.__version__}")

# Pandas vs NumPy:
# NumPy -> Sayısal hesaplamalar için optimize edilmiştir. Hızlıdır.
# Pandas -> Tablolu (tabular) veriler için optimize edilmiştir.
#          NumPy'ın hızını alır, üzerine 'index' (etiket) ekler.
#          Excel'in yaptığı her şeyi ve daha fazlasını yapar.


# -----------------------------------------------------------------
# --- 2. TEMEL VERİ YAPILARI: Series ve DataFrame ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n2. TEMEL VERİ YAPILARI\n" + "="*30)

# --- 2.1. Series (1D Veri Yapısı) ---
# NumPy array'ine benzeyen, ancak etiketli (index) 1D yapı.
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(f"Pandas Series:\n{s}")
print(f"Series'in değerleri: {s.values}")
print(f"Series'in index'i: {s.index}")
print(f"'b' indexli eleman: {s['b']}")


# --- 2.2. DataFrame (2D Veri Yapısı - Tablo) ---
# En çok kullanacağımız yapı. Excel sayfası gibi düşünebilirsiniz.
# Genellikle bir Python sözlüğünden (dictionary) oluşturulur.
data_dict = {
    'İsim': ['Ahmet', 'Ayşe', 'Mehmet', 'Fatma', 'Ali', 'Zeynep'],
    'Departman': ['IT', 'İK', 'IT', 'Finans', 'Finans', 'İK'],
    'Yaş': [32, 28, 45, 38, 29, 35],
    'Maaş': [15000, 12000, 22000, 18000, 17000, 13000]
}

df = pd.DataFrame(data_dict)
print(f"\nDataFrame (Personel Tablosu):\n{df}")


# -----------------------------------------------------------------
# --- 3. VERİ OKUMA VE YAZMA (I/O) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n3. VERİ OKUMA VE YAZMA\n" + "="*30)

# Verimizi CSV (Comma-Separated Values) olarak kaydedelim
# `index=False` -> Satır numaralarını (0, 1, 2...) ayrı bir sütun olarak kaydetme
try:
    df.to_csv('personel.csv', index=False, encoding='utf-8')
    print("'personel.csv' dosyası başarıyla yazıldı.")

    # Kaydettiğimiz CSV dosyasını geri okuyalım
    df_okunan = pd.read_csv('personel.csv')
    print("\nCSV'den Okunan DataFrame:\n", df_okunan.head()) # .head() ilk 5 satırı gösterir
except Exception as e:
    print(f"Dosya işlemi hatası (izinler?): {e}")

# Excel işlemleri (openpyxl kütüphanesi gerekir)
import openpyxl
df.to_excel('personel.xlsx', index=False, sheet_name='Personel_Listesi')
df_excel = pd.read_excel('personel.xlsx')
df_excel

# -----------------------------------------------------------------
# --- 4. VERİYE İLK BAKIŞ (Data Inspection) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n4. VERİYE İLK BAKIŞ\n" + "="*30)
# df = df_okunan # Üzerinde çalışmak için okuduğumuz veriyi kullanalım

# `.head(n)`: İlk n satırı gösterir (varsayılan n=5)
print(f"\nİlk 3 Satır (head):\n{df.head(3)}")

# `.tail(n)`: Son n satırı gösterir
print(f"\nSon 2 Satır (tail):\n{df.tail(2)}")

# `.info()`: DataFrame'in yapısı hakkında özet bilgi (ÇOK ÖNEMLİ)
# Sütun adları, boş olmayan (non-null) değer sayısı ve veri tipleri (dtype)
print("\n--- DataFrame Bilgisi (info) ---")
df.info()
print("---------------------------------")

# `.describe()`: Sayısal sütunların temel istatistiksel özetini verir
# (count, mean, std, min, max, %25, %50, %75)
print(f"\nSayısal Özet (describe):\n{df.describe()}")

# `.shape`: Boyut (satır sayısı, sütun sayısı)
print(f"\nShape (Satır, Sütun): {df.shape}")

# `.columns`: Sütun isimlerini listeler
print(f"\nSütunlar: {df.columns}")

# `.dtypes`: Her sütunun veri tipini gösterir
print(f"\nVeri Tipleri:\n{df.dtypes}")

# `.value_counts()`: Kategorik/Tekil sütunların frekansını (dağılımını) gösterir
print(f"\nDepartman Dağılımı (value_counts):\n{df['Departman'].value_counts()}")


# -----------------------------------------------------------------
# --- 5. SEÇİM VE İNDEKSLEME (loc ve iloc) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n5. SEÇİM VE İNDEKSLEME\n" + "="*30)

# --- 5.1. Sütun Seçme ---
# Tek sütun seçme (Sonuç bir 'Series' döner)
isimler_serisi = df['İsim']
print(f"\nİsim Sütunu (Series):\n{isimler_serisi}")

# Birden fazla sütun seçme (Sonuç bir 'DataFrame' döner)
df_secim = df[['İsim', 'Maaş']]
print(f"\nİsim ve Maaş Sütunları (DataFrame):\n{df_secim}")


# --- 5.2. Satır Seçme (loc ve iloc) ---
# .loc[] -> LABEL (İsim/Etiket) bazlı seçim yapar.
# .iloc[] -> INTEGER (Sıra Numarası) bazlı seçim yapar.

print("\n--- .loc ve .iloc ---")
# .iloc[index_no] (Integer Location)
# 0'dan başlar.
print(f"\n0. index'teki satır (iloc[0]):\n{df.iloc[0]}") # Ahmet'in bilgileri

# 1'den 4'e kadar olan satırlar (4 dahil değil!)
print(f"\n1-4 arası satırlar (iloc[1:4]):\n{df.iloc[1:4]}")

# Hem satır hem sütun seçme: .iloc[satır_no, sütun_no]
# 1. satır, 2. sütundaki (Yaş) değer
print(f"\n1. satır, 2. sütun (iloc[1, 2]): {df.iloc[1, 2]}") # Ayşe'nin yaşı: 28


# .loc[index_adı] (Location)
# .loc kullanmak için anlamlı bir index'e sahip olmak iyidir.
# 'İsim' sütununu index yapalım:
df_indexed = df.set_index('İsim')
print(f"\nİsim Indexli DataFrame:\n{df_indexed.head()}")

# Artık 'Ahmet' adıyla satır seçebiliriz:
print(f"\nIndex'i 'Ahmet' olan satır (loc['Ahmet']):\n{df_indexed.loc['Ahmet']}")

# Hem satır hem sütun seçme: .loc[index_adı, sütun_adı]
print(f"\n'Mehmet'in 'Maaş'ı (loc['Mehmet', 'Maaş']): {df_indexed.loc['Mehmet', 'Maaş']}")

# .loc ile dilimleme (slicing) yaparken, BİTİŞ DEĞERİ DAHİLDİR!
print(f"\n'Ayşe'den 'Fatma'ya (dahil) (loc['Ayşe':'Fatma']):\n{df_indexed.loc['Ayşe':'Fatma']}")

# Index'i sıfırlama
df_reset = df_indexed.reset_index()
# print(f"\nIndex Sıfırlanmış:\n{df_reset.head()}")


# -----------------------------------------------------------------
# --- 6. KOŞULLU FİLTRELEME (Boolean Indexing) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n6. KOŞULLU FİLTRELEME\n" + "="*30)
# Pandas'ın en güçlü yanlarından biri.

# Yaşı 30'dan büyük olanlar
print(f"\nYaşı > 30 olanlar:\n{df[df['Yaş'] > 30]}")

# Departmanı 'IT' olanlar
print(f"\nDepartmanı 'IT' olanlar:\n{df[df['Departman'] == 'IT']}")

# Maaşı 15000'den az olanların sadece İsim ve Maaş'larını göster
print(f"\nMaaşı < 15000 (İsim ve Maaş):\n{df[df['Maaş'] < 15000][['İsim', 'Maaş']]}")

# --- Çoklu Koşullar ---
# `&` -> VE (and)
# `|` -> VEYA (or)
# Her koşul ayrı parantez `()` içinde olmalıdır!
kosul1 = df['Departman'] == 'IT'
kosul2 = df['Maaş'] > 16000
print(f"\nDepartmanı IT VE Maaşı > 16000:\n{df[kosul1 & kosul2]}")

kosul3 = df['Yaş'] < 30
kosul4 = df['Yaş'] > 40
print(f"\nYaşı < 30 VEYA Yaşı > 40:\n{df[kosul3 | kosul4]}")

# `.isin()` kullanımı (Çoklu VEYA için kısa yol)
# Departmanı 'IT' VEYA 'İK' olanlar
departmanlar = ['IT', 'İK']
print(f"\nDepartmanı IT veya İK olanlar (isin):\n{df[df['Departman'].isin(departmanlar)]}")


# -----------------------------------------------------------------
# --- 7. VERİ MANİPÜLASYONU (Sütun Ekleme/Silme) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n7. VERİ MANİPÜLASYONU\n" + "="*30)

# --- Sütun Ekleme ---
# Varolan sütunlardan yeni sütun türetme
df['Yaş_Maaş_Oranı'] = df['Maaş'] / df['Yaş']
print(f"\nYeni Sütunlu (Yaş_Maaş_Oranı):\n{df.head()}")

# Sabit bir değerle sütun ekleme
df['Şirket'] = 'Kurumsal A.Ş.'
print(f"\nYeni Sütunlu (Şirket):\n{df.head()}")


# --- Sütun/Satır Silme (`.drop()`) ---
# `axis=1` -> Sütun sil
# `inplace=True` -> Değişikliği kalıcı yap (varsayılanı False'tur)
df.drop('Şirket', axis=1, inplace=True)
print(f"\n'Şirket' Sütunu Silindi:\n{df.head()}")

# `axis=0` -> Satır sil (index'e göre)
# 0. index'teki satırı (Ahmet) silelim
df_silinmis = df.drop(0, axis=0)
print(f"\n0. Index'teki Satır Silindi:\n{df_silinmis.head()}")
# print(f"\nOrijinal df değişmedi:\n{df.head()}") # inplace=True demedik


# -----------------------------------------------------------------
# --- 8. EKSİK VERİ YÖNETİMİ (Missing Data) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n8. EKSİK VERİ YÖNETİMİ\n" + "="*30)

# Önce eksik veri (NaN - Not a Number) oluşturalım
df_nan = df.copy() # Orijinali bozmayalım
df_nan.loc[1, 'Maaş'] = np.nan # Ayşe'nin maaşını boş yap
df_nan.loc[3, 'Yaş'] = np.nan # Fatma'nın yaşını boş yap
df_nan.loc[4, 'Departman'] = np.nan # Ali'nin departmanını boş yap
print(f"\nEksik Verili DataFrame:\n{df_nan}")

# Eksik verileri bulma (`.isnull()` veya `.isna()`)
print(f"\nEksik Veri Kontrolü (True/False):\n{df_nan.isnull()}")

# Hangi sütunda kaç adet eksik veri var? (En çok kullanılan)
print(f"\nSütunlardaki Eksik Veri Sayısı:\n{df_nan.isnull().sum()}")

# --- 8.1. Eksik Verileri Silme (`.dropna()`) ---
# `how='any'` -> Bir satırda 1 tane bile NaN varsa o satırı sil
df_temiz = df_nan.dropna(how='any')
print(f"\nEksik Satırlar Silindi (dropna):\n{df_temiz}")

# --- 8.2. Eksik Verileri Doldurma (`.fillna()`) ---
# Maaş sütunundaki NaN değerleri, maaş ortalaması ile doldurma
ortalama_maas = df_nan['Maaş'].mean()
print(f"\nOrtalama Maaş: {ortalama_maas}")
df_nan['Maaş'].fillna(ortalama_maas, inplace=True)
print(f"\nMaaş Eksikleri Dolduruldu (Ortalama):\n{df_nan}")

# Departman (kategorik) veriyi en çok tekrar eden (modus) ile doldurma
modus_departman = df_nan['Departman'].mode()[0] # .mode() bir Series döner
print(f"\nEn Sık Departman: {modus_departman}")
df_nan['Departman'].fillna(modus_departman, inplace=True)
print(f"\nDepartman Eksikleri Dolduruldu (Modus):\n{df_nan}")

# Yaş verisini bir önceki geçerli veriyle doldurma (forward-fill)
df_nan['Yaş'].fillna(method='ffill', inplace=True)
print(f"\nYaş Eksikleri Dolduruldu (ffill):\n{df_nan}")


# -----------------------------------------------------------------
# --- 9. GROUPBY VE AGREGASYON (Gruplama ve Özetleme) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n9. GROUPBY VE AGREGASYON\n" + "="*30)
# SQL'deki GROUP BY veya Excel'deki Pivot Tablo ile aynı mantıktır.
# Adımlar: Split (Böl) - Apply (Uygula) - Combine (Birleştir)

# Departmanlara göre grupla
grup = df.groupby('Departman')

# Departmanlara göre ortalama maaşlar
print(f"\nDepartmanlara Göre Ortalama Maaş:\n{grup['Maaş'].mean()}")

# Departmanlara göre toplam maaş
print(f"\nDepartmanlara Göre Toplam Maaş:\n{grup['Maaş'].sum()}")

# Departmanlardaki kişi sayısı
print(f"\nDepartmanlara Göre Kişi Sayısı:\n{grup['İsim'].count()}")

# Departmanlara göre ortalama yaş
print(f"\nDepartmanlara Göre Ortalama Yaş:\n{grup['Yaş'].mean()}")

# `.agg()` (Aggregate) -> Çoklu özetleme işlemleri için
# Departmanlara göre; maaşın ortalamasını, yaşın maksimumunu
# ve kişi sayısını (isim'i sayarak) al.
df_agg = grup.agg({
    'Maaş': 'mean',
    'Yaş': 'max',
    'İsim': 'count'
})
# Sütunları yeniden adlandırma
df_agg = df_agg.rename(columns={'Maaş': 'Ort_Maaş', 'Yaş': 'Max_Yaş', 'İsim': 'Kişi_Sayısı'})
print(f"\nDetaylı Agregasyon (agg):\n{df_agg}")


# -----------------------------------------------------------------
# --- 10. BİRLEŞTİRME VE EKLEME (Merge & Concat) ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n10. BİRLEŞTİRME VE EKLEME\n" + "="*30)

# --- 10.1. `pd.concat()` (Alt alta veya yan yana ekleme) ---
# NumPy'daki vstack ve hstack gibi
df_parca1 = df.iloc[0:3] # İlk 3 satır
df_parca2 = df.iloc[3:6] # Son 3 satır

# Alt alta birleştirme (axis=0)
df_concat_vertical = pd.concat([df_parca1, df_parca2], axis=0)
print(f"\nConcat (Alt Alta):\n{df_concat_vertical}")

# --- 10.2. `pd.merge()` (SQL JOIN mantığı) ---
# Ortak bir sütun (key) üzerinden iki tabloyu birleştirir.
df_personel = df[['İsim', 'Departman']]
df_gorev = pd.DataFrame({
    'Departman': ['IT', 'İK', 'Finans', 'Pazarlama'],
    'Departman_Yöneticisi': ['Ali Y.', 'Zeynep K.', 'Mehmet B.', 'Ayşe T.']
})

print(f"\nPersonel Tablosu (df_personel):\n{df_personel}")
print(f"\nGörev Tablosu (df_gorev):\n{df_gorev}")

# 'Departman' sütunu üzerinden birleştirme
# `how='inner'` (varsayılan): Sadece iki tabloda da eşleşen kayıtları getir
df_merged = pd.merge(df_personel, df_gorev, on='Departman', how='inner')
print(f"\nMerge (inner join):\n{df_merged}")

# `how='left'`: Sol tablodaki (df_personel) tüm kayıtları getir,
# sağda (df_gorev) karşılığı yoksa NaN bas.
df_merged_left = pd.merge(df_personel, df_gorev, on='Departman', how='left')
# (Pazarlama bizde olmadığı için 'Pazarlama' yöneticisi gelmez)
print(f"\nMerge (left join):\n{df_merged_left}")


# -----------------------------------------------------------------
# --- 11. DİĞER FAYDALI OPERASYONLAR ---
# -----------------------------------------------------------------
print("\n" + "="*30 + "\n11. DİĞER FAYDALI OPERASYONLAR\n" + "="*30)

# --- 11.1. Sıralama (`.sort_values()`) ---
# Maaşa göre azalan (descending) sırada sırala
print(f"\nMaaşa Göre Sıralı (Azalan):\n{df.sort_values(by='Maaş', ascending=False)}")

# --- 11.2. Fonksiyon Uygulama (`.apply()`) ---
# Karmaşık, kendi yazdığımız fonksiyonları sütunlara uygulama

def maas_kategori(maas):
    if maas > 17000:
        return 'Yüksek'
    elif maas > 13000:
        return 'Orta'
    else:
        return 'Düşük'

# 'Maaş' sütunundaki her değere 'maas_kategori' fonksiyonunu uygula
df['Maaş_Kategorisi'] = df['Maaş'].apply(maas_kategori)
print(f"\nApply ile Kategori Eklendi:\n{df[['İsim', 'Maaş', 'Maaş_Kategorisi']]}")

# Lambda fonksiyon ile .apply (kısa yol)
df['Yaş_Kategorisi'] = df['Yaş'].apply(lambda yas: 'Genç' if yas < 35 else 'Kıdemli')
print(f"\nLambda Apply ile Yaş Kategorisi:\n{df[['İsim', 'Yaş', 'Yaş_Kategorisi']]}")

# --- 11.3. Benzersiz Değerler (`.unique()` ve `.nunique()`) ---
# Departman sütunundaki benzersiz (tekil) değerler
print(f"\nBenzersiz Departmanlar: {df['Departman'].unique()}")

# Benzersiz departman sayısı
print(f"\nBenzersiz Departman Sayısı: {df['Departman'].nunique()}")

# --- 11.4. String Operasyonları (`.str`) ---
# 'İsim' sütunundaki tüm harfleri küçültme
print(f"\nİsimler (Küçük Harf):\n{df['İsim'].str.lower()}")

# 'Departman' sütununda 'IT' kelimesini içerenler
print(f"\nDepartmanda 'IT' içerenler:\n{df[df['Departman'].str.contains('IT')]}")


print("\n" + "="*40 + "\nPANDAS KAPSAMLI REHBERİ TAMAMLANDI.\n" + "="*40)