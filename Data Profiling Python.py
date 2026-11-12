# ==============================================================================
# DATA PROFILING SEBELUM VISUALISASI DI GOOGLE LOOKER STUDIO
# Nama: Fadhlul Ikram
# Dataset: df - df.csv
# ==============================================================================

import pandas as pd

# Load dataset langsung dari GitHub Repository
url_dataset = "https://raw.githubusercontent.com/fadhlulikram/tokopaedi-sales-analysis-Looker/refs/heads/main/dataset/df%20-%20df.csv"
df_raw = pd.read_csv(url_dataset)

# 1. Cek struktur awal dan tipe data
print("=== Info Dataset Awal ===")
df_raw.info()

# 2. Ubah tipe data kolom tanggal dari object (teks) menjadi datetime
df_raw['order_date'] = pd.to_datetime(df_raw['order_date'])
df_raw['registered_date'] = pd.to_datetime(df_raw['registered_date'])

print("\n=== Info Dataset Setelah Konversi Tanggal ===")
df_raw.info()

# 3. Cek nilai kosong (null) dan spasi kosong (whitespace)
print("\n=== Cek Nilai Null ===")
print(df_raw.isnull().sum())

print("\n=== Cek Whitespace Kosong pada Kolom Teks ===")
whitespace_check = df_raw.select_dtypes(include='object').apply(lambda col: col.str.strip().eq('').sum())
print(whitespace_check)

# 4. Cek konsistensi penulisan kategori dan metode pembayaran
for col in ['category', 'payment_method', 'day', 'month']:
    print(f"\nNilai unik pada kolom '{col}':")
    print(df_raw[col].unique())

# 5. Cek duplikasi baris penuh dan duplikasi ID Order
print("\nJumlah baris duplikat penuh:", df_raw.duplicated().sum())
print("Jumlah ID Order yang kembar (multi-produk dalam 1 pesanan):", df_raw.duplicated(subset='id').sum())

# Menampilkan contoh pesanan dengan beberapa produk (multi-produk)
dup_ids = df_raw[df_raw.duplicated(subset='id', keep=False)]
print("\n=== Contoh Order ID dengan Multi-Produk ===")
print(dup_ids[['id', 'customer_id', 'order_date', 'sku_id', 'price']].sort_values('id').head(10))

# 6. Cek statistik deskriptif untuk kolom angka (numerik)
print("\n=== Statistik Deskriptif Kolom Numerik ===")
print(df_raw.describe())
