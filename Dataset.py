import pandas as pd

# Buka dataset
df = pd.read_csv("DatasetForCoffeeSales2.csv")

# Menampilkan contoh data
print(df.head())

# Mengecek tipe data pada setiap kolom
print(df.dtypes)
