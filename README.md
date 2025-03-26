# Tugas Pertemuan 3 Praktikum Machine Learning 
Nama  : Yassar Malik Arrasyid

NIM   : 1227050133

Kelas : G

# Modul 1 : Mengenal Data, Data Collecting
Silahkan unduh data dari Kaggle Dataset dan anda dapat mengunduh data dari data berikut ini: 
https://www.kaggle.com/datasets/halaturkialotaibi/coffee-bean-sales-dataset. 
Buka data yang telah diunduh tersebut dengan menggunakan editor.

![Screenshot (241)](https://github.com/user-attachments/assets/ad856b08-5b07-4fb1-a5c3-e186240767c0)


Silahkan cari data pada sumber dataset kemudian sebutkan jenis data tersebut apakah data tersebut masuk data nominal, ordinal, rasio atau interval 


# Kode yang digunakan untuk import dataset dari kaggle
import kagglehub

path = kagglehub.dataset_download("halaturkialotaibi/coffee-bean-sales-dataset")

print("Path to dataset files:", path)

setelah itu jika dataset berada di folder lain pindahkan ke folder yang akan digunakan misalnya "Tugas Pertemuan 3"

setelah itu kita akan menggunakan kode untuk mendapatkan data data seperti yang di perintahkan di bawah ini 
Silahkan cari data pada sumber dataset kemudian sebutkan jenis data tersebut apakah data tersebut masuk data nominal, ordinal, rasio atau interval 
# Kode yang akan di gunakan untuk menjalankan perintah tersebut
import pandas as pd

df1 = pd.read_csv("DatasetForCoffeeSales2.csv")
print("=== Dataset: Coffee Sales ===")
print(df1.head())
print("\nTipe data setiap kolom:")
print(df1.dtypes)

data_types_1 = {
    "Date": "Interval",
    "Customer_ID": "Nominal",
    "City": "Nominal",
    "Category": "Nominal",
    "Product": "Nominal",
    "Unit Price": "Rasio",
    "Quantity": "Rasio",
    "Sales Amount": "Rasio",
    "Used_Discount": "Nominal",
    "Discount_Amount": "Rasio",
    "Final Sales": "Rasio",
}

print("\nKlasifikasi Jenis Data untuk Coffee Sales:")
for col, dtype in data_types_1.items():
    print(f"{col}: {dtype}")

print("\n" + "="*50 + "\n")

df2 = pd.read_csv("saudi_cities_geocoding.csv")
print("=== Dataset: Saudi Cities Geocoding ===")
print(df2.head())
print("\nTipe data setiap kolom:")
print(df2.dtypes)

data_types_2 = {
    "city": "Nominal",
    "latitude": "Rasio",
    "longitude": "Rasio",
    "country": "Nominal",
    "iso2": "Nominal",
    "admin_name": "Nominal",
    "capital": "Nominal",
    "population": "Rasio",
}

print("\nKlasifikasi Jenis Data untuk Saudi Cities Geocoding:")
for col, dtype in data_types_2.items():
    print(f"{col}: {dtype}")

kode ini di gunakan untuk menampilkan output berupa data data yang berasal dari kedua dataset csv tersebut

# Berikut adalah output yang di hasilkan dari kode tersebut

![image](https://github.com/user-attachments/assets/1d4aaa0e-e87b-471b-9d25-505e1850ffdb)


# Modul 2 : Melakukan analisis data sederhana
Soal : Silahkan gunakan data yang telah diunduh yakni data yang diambil pada Kaggle, yakni data berikut: 
https://www.kaggle.com/datasets/halaturkialotaibi/coffee-bean-sales-dataset. 
Cobalah melakukan analisis data sederhana dengan melakukan hal seperti dibawah ini:

Pada modul 2 ini ada perintah untuk meng analisis data dari dataset tersebut dengan menggunakan kode yang berada di bawah nya
# Berikut adalah kode yang berada dalam perintah tersebut
import pandas as pd

data = pd.read_csv("DatasetForCoffeeSales2.csv")

print(data.head(10))

filtered_data = data.filter(["City", "Category", "Product", "Quantity"])
print(filtered_data.head())

data.sort_values("Quantity", axis=0, ascending=False, inplace=True, na_position="last")
print(data.head())

grp1 = data.groupby('City')
result = grp1['Final Sales'].aggregate('sum')
print("\nTotal Sales per City:\n", result)

# Berikut adalah output dari kode sebelumnya

![image](https://github.com/user-attachments/assets/00496cd2-2102-496b-8cd6-559abf2e15dd)

# Modul 3 : Data Cleaning dan Transformation
Soal : Silahkan unduh dataset yang akan kita gunakan pada tautan berikut : 
https://drive.google.com/file/d/1ZWpS_EKAvbsvuigBXDaH0p01FahpHeh8/view?usp=sharing 
Setelah anda unduh silahkan untuk read dataset tersebut pada google colab anda. Lalu analisis dataset tersebut menggunakan fungsi info() seperti dibawah ini : 

Di dalam modul ini ada perintah untuk menganalisis dataset students.csv dengan menggunakan kode di bawah nya

# Berikut adalah kode dalam perintah tersebut
import pandas as pd

data = pd.read_csv("students.csv")

print(data.head(10))

data.info()

print(data.isna().sum())

data['lunch'] = data['lunch'].fillna(data['lunch'].mode()[0])

data['reading score'] = data['reading score'].fillna(data['reading score'].mean())

data['grade'] = data['grade'].fillna(data['grade'].median())

data.info()

data['reading score'] = data['reading score'].interpolate(method='linear')

data['grade'] = data['grade'].bfill()

data['writing score'] = data['writing score'].ffill()

data.dropna(axis=0, inplace=True)

data.dropna(axis=1, inplace=True)

# Berikut adalah output dari kode di atas

![image](https://github.com/user-attachments/assets/4d065810-a0f3-4104-b571-e123afad2701)
