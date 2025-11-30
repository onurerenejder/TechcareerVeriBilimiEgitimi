# 🎓  Veri Bilimi ve Yapay Zeka Bootcamp'i (6 Hafta)

Bu depo,sıfırdan ileri seviyeye **Python ile Veri Bilimi ve Makine Öğrenmesi** eğitiminin tüm ders notlarını, kaynak kodlarını ve proje dosyalarını içermektedir.

Eğitim, sadece kod yazmayı değil; **istatistiksel düşünmeyi, veri manipülasyon sanatını, görsel hikaye anlatıcılığını ve makine öğrenmesi algoritmalarının matematiksel temellerini** kapsamaktadır.

---

## 📚 Detaylı Müfredat ve Kazanımlar

### **Hafta 1: Python Programlama Temelleri**
Yazılım dünyasına güçlü bir giriş ve algoritmik düşünme yapısının oturtulması.
* **Core Python:** Değişkenler, Dinamik Tiplendirme, Bellek Yönetimi.
* **Veri Tipleri:** `int`, `float`, `str`, `bool` ve dönüşüm fonksiyonları.
* **Operatörler:** Aritmetik, Karşılaştırma, Mantıksal ve Atama operatörleri.
* **String Manipülasyonu:** Indexing, Slicing, f-Strings, `.split()`, `.strip()`, `.replace()`.
* **Kullanıcı Etkileşimi:** `input()` fonksiyonu ve Tip Dönüşümleri (Type Casting).

### **Hafta 2: İleri Seviye Python ve Algoritmalar**
Modüler, tekrar kullanılabilir ve hatasız kod yazma teknikleri.
* **Akış Kontrolü:** `if-elif-else` blokları ve `nested` (iç içe) koşullar.
* **Döngüler:** `for` ve `while` döngüleri, `break`, `continue` ifadeleri.
* **Veri Yapıları (Collections):** * Listeler (Lists) ve Metotları (`append`, `pop`, `sort`).
    * Sözlükler (Dictionaries - Key/Value yapısı).
    * Demetler (Tuples) ve Kümeler (Sets).
* **Fonksiyonel Programlama:** `def` ile fonksiyon tanımlama, parametreler, `return`, `docstring` ve `lambda` fonksiyonları.
* **Comprehensions:** List Comprehension ile tek satırda döngü mantığı.
* **Hata Yönetimi:** `try-except-finally` blokları ile exception handling.
* **Dosya İşlemleri (I/O):** `.txt` ve `.json` dosyaları ile okuma/yazma/loglama.
* **Modüller:** `math`, `random`, `datetime` kütüphaneleri.

### **Hafta 3: NumPy ile Yüksek Performanslı Hesaplama**
Veri biliminin matematiksel motoru olan NumPy ile vektörel işlemler.
* **Array Mimarisi:** Python List vs NumPy Array (Hız ve Hafıza farkı).
* **Array Oluşturma:** `np.array`, `arange`, `zeros`, `ones`, `linspace`, `eye`.
* **Rastgelelik:** `np.random` modülü (rand, randn, randint) ve `seed` mantığı.
* **Yapısal Analiz:** `.shape`, `.ndim`, `.size`, `.dtype`.
* **Manipülasyon:** `.reshape()`, `.flatten()`, `.ravel()`.
* **İndeksleme:** Slicing, Fancy Indexing ve **Boolean Indexing** (Koşullu seçim).
* **Matematiksel İşlemler:** Vektörel (Element-wise) operasyonlar, Broadcasting.
* **İstatistik:** `.mean()`, `.std()`, `.var()`, `.min()`, `.max()`, `argmax/argmin`.

### **Hafta 4: Pandas ile Veri Analizi ve Manipülasyonu**
Veriyi yapılandırma, temizleme ve analiz etme sanatı.
* **Veri Yapıları:** `Series` (1D) ve `DataFrame` (2D) mimarisi.
* **Veri Okuma/Yazma:** CSV, Excel, JSON formatları ile I/O işlemleri.
* **Veri Keşfi (EDA):** `.head()`, `.info()`, `.describe()`, `.value_counts()`, `.corr()`.
* **Seçim İşlemleri:** `.loc[]` (Label-based) ve `.iloc[]` (Integer-based) kullanımı.
* **Filtreleme:** Çoklu koşullu sorgular (`&`, `|`) ve `.isin()` metodu.
* **Veri Temizliği:** Eksik Veri (`NaN`) tespiti, silme (`dropna`) ve doldurma (`fillna`) stratejileri (Mean/Mode Imputation).
* **İleri Manipülasyon:** `apply()` ile fonksiyon uygulama, `map()`, String operasyonları (`.str`).
* **Gruplama ve Özetleme:** `groupby()` mantığı (Split-Apply-Combine) ve `.agg()` fonksiyonları.
* **Tablo Birleştirme:** `merge()` (SQL Join mantığı) ve `concat()` işlemleri.

### **Hafta 5: Matplotlib ile İleri Seviye Veri Görselleştirme**
Veriden içgörü çıkarma ve profesyonel raporlama.
* **Mimari:** Pyplot (State-machine) vs **Object-Oriented Interface (OOP)** (`Figure` ve `Axes` nesneleri).
* **Temel Grafikler:** Line, Bar, Scatter, Histogram, Pie Chart.
* **Grafik Özelleştirme:** Renk paletleri, Marker'lar, Line styles, Grid sistemleri.
* **Çoklu Grafikler:** `subplots` ve `GridSpec` ile dashboard tasarımı.
* **İleri Teknikler:** * Çift Eksen kullanımı (`twinx`).
    * Grafik içine grafik ekleme (Inset Plots).
    * `Annotation` ile veri üzerine not alma ve oklar.
    * `Heatmap` (Isı haritası) ile korelasyon analizi.
* **Dışa Aktarma:** Grafikleri yüksek çözünürlükte (`dpi`) kaydetme.

### **Hafta 6: Makine Öğrenmesi (Machine Learning) - Master Class**
Scikit-Learn ile uçtan uca (End-to-End) model geliştirme ve yapay zeka temelleri.

#### **A. Teorik Temeller**
* Denetimli (Supervised) vs Denetimsiz (Unsupervised) Öğrenme.
* Bias-Variance Dengesi, Overfitting (Ezberleme) ve Underfitting.
* **Veri Ön İşleme:**
    * Train/Test Split (Eğitim/Sınav ayrımı mantığı).
    * Feature Scaling: `StandardScaler` ve `MinMaxScaler` farkı.
    * Encoding: `LabelEncoder` kullanımı.

#### **B. Regresyon Modelleri (Sayısal Tahmin)**
* **Linear Regression:** En küçük kareler yöntemi ve doğrusal ilişkiler.
* **Decision Tree Regressor:** Karar ağacı yapısı ve bilgi kazanımı.
* **Random Forest Regressor:** Bagging, Ensemble mantığı ve kolektif öğrenme.
* **SVR (Support Vector Regressor):** Marjin ve kernel trick.
* **Değerlendirme:** MSE, RMSE, MAE ve R2 Score (Açıklayıcılık katsayısı).

#### **C. Sınıflandırma Modelleri (Kategori Tahmini)**
* **Logistic Regression:** Sigmoid fonksiyonu ve olasılık hesaplama.
* **KNN (K-Nearest Neighbors):** Mesafe temelli (Öklid) sınıflandırma.
* **SVM (Support Vector Machines):** Hyperplane ve sınıf ayrıştırma.
* **Random Forest Classifier:** Sınıflandırmada topluluk oylaması.
* **Değerlendirme:** * **Confusion Matrix:** TP, TN, FP, FN analizi.
    * **Metrikler:** Accuracy, Precision, Recall, F1-Score.
    * **Raporlama:** `classification_report` okuma ve yorumlama.

#### **D. Model Optimizasyonu ve İleri Teknikler**
* **GridSearchCV:** Hiperparametre optimizasyonu ile en iyi model ayarlarının bulunması.
* **Cross Validation (CV):** K-Fold çapraz doğrulama ile model güvenilirliği.

---

## 💻 Teknoloji Yığını (Tech Stack)

Eğitim boyunca aşağıdaki kütüphaneler ve araçlar kullanılmıştır:

* **Dil:** Python 3.10+
* **Analiz:** `pandas`, `numpy`
* **Görselleştirme:** `matplotlib`, `seaborn`
* **Makine Öğrenmesi:** `scikit-learn`
* **Ortam:** Jupyter Notebook / VS Code


## 👨‍🏫 Eğitmen

**[Onur Eren Ejder]**
*Yazılım Mühendisi / Eğitmen*

Bu içerik,Techcareer.net bir eğitim programı kapsamında hazırlanmış olup, teorik bilginin pratik uygulamalarla pekiştirilmesini hedeflemektedir.
