import kagglehub

# Download latest version
path = kagglehub.dataset_download("halaturkialotaibi/coffee-bean-sales-dataset")

print("Path to dataset files:", path)