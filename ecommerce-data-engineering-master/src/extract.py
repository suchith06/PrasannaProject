import pandas as pd

# Extract raw datasets
customers = pd.read_csv("data/raw/customers.csv")
products = pd.read_csv("data/raw/products.csv")
orders = pd.read_csv("data/raw/orders.csv")
order_items = pd.read_csv("data/raw/order_items.csv")

# Inspect customers dataset

print("FIRST 5 ROWS:")

print(customers.head())

print("\nSHAPE:")

print(customers.shape)

print("\nCOLUMNS:")

print(customers.columns)

print("\nDATA TYPES:")

print(customers.dtypes)

print("\nMISSING VALUES:")

print(customers.isnull().sum())

print("\nDUPLICATE ROWS:")

print(customers.duplicated().sum())