import pandas as pd

# Membaca dataset Coffee Sales
data = pd.read_csv("DatasetForCoffeeSales2.csv")

# Menampilkan 10 baris pertama
print(data.head(10))

# Filter data hanya untuk kolom City, Category, Product, dan Quantity
filtered_data = data.filter(["City", "Category", "Product", "Quantity"])
print(filtered_data.head())

# Sorting Quantity (dari yang paling banyak ke sedikit)
data.sort_values("Quantity", axis=0, ascending=False, inplace=True, na_position="last")
print(data.head())

# Group Total Sales berdasarkan City
grp1 = data.groupby('City')
result = grp1['Final Sales'].aggregate('sum')
print("\nTotal Sales per City:\n", result)
