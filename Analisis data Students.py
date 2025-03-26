import pandas as pd

# Membaca dataset
data = pd.read_csv("students.csv")

# Menampilkan 10 baris pertama
print(data.head(10))

# Menampilkan informasi dataset
data.info()

# Mengecek jumlah missing value pada setiap kolom
print(data.isna().sum())

# Mengisi missing value pada fitur 'lunch' dengan modus (mode)
data['lunch'] = data['lunch'].fillna(data['lunch'].mode()[0])

# Mengisi missing value pada fitur 'reading score' dengan mean
data['reading score'] = data['reading score'].fillna(data['reading score'].mean())

# Mengisi missing value pada fitur 'grade' dengan median
data['grade'] = data['grade'].fillna(data['grade'].median())

# Menampilkan kembali informasi dataset setelah handling missing value
data.info()

# Alternatif metode handling missing value

# Interpolasi nilai yang hilang secara linear pada 'reading score'
data['reading score'] = data['reading score'].interpolate(method='linear')

# Menggunakan backward fill tanpa warning
data['grade'] = data['grade'].bfill()

# Menggunakan forward fill tanpa warning
data['writing score'] = data['writing score'].ffill()

# Menghapus baris dengan nilai NaN
data.dropna(axis=0, inplace=True)

# Menghapus kolom jika lebih dari 50% nilainya adalah NaN
data.dropna(axis=1, inplace=True)
