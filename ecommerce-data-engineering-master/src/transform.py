import pandas as pd


pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

orders = pd.read_csv("data/raw/orders.csv")

print("BEFORE:")
print(orders.dtypes)

orders["order_date"] = pd.to_datetime(orders["order_date"])

print("\nAFTER:")
print(orders.dtypes)
# Load products and order items
products = pd.read_csv("data/raw/products.csv")
order_items = pd.read_csv("data/raw/order_items.csv")

# Join order items with products
sales = order_items.merge(
    products,
    on="product_id",
    how="left"
)

print("\nJOINED SALES DATA:")
print(sales)  
# Calculate revenue for each order item
sales["line_total"] = sales["quantity"] * sales["price"]

print("\nSALES WITH LINE TOTAL:")
print(sales)
# Join sales with orders
sales_orders = sales.merge(
    orders,
    on="order_id",
    how="left"
)

print("\nSALES WITH ORDER DETAILS:")
print(sales_orders)
# Load customer data
customers = pd.read_csv("data/raw/customers.csv")

# Join customer information
final_sales = sales_orders.merge(
    customers,
    on="customer_id",
    how="left"
)

print("\nFINAL SALES DATA:")
print(final_sales)
# -------------------------------
# Apply Business Rules
# -------------------------------

# Rule 1: Keep only completed orders
final_sales = final_sales[
    final_sales["status"] == "Completed"
].copy()

# Rule 2: Quantity must be greater than 0
final_sales = final_sales[
    final_sales["quantity"] > 0
]

# Rule 3: Price must be greater than 0
final_sales = final_sales[
    final_sales["price"] > 0
]

# Rule 4: Recalculate line total
final_sales["line_total"] = (
    final_sales["quantity"] * final_sales["price"]
)

# Rule 5: Remove duplicates
final_sales = final_sales.drop_duplicates()

print("\nFINAL DATA AFTER BUSINESS RULES:")
print(final_sales)
# Reset index after filtering
final_sales = final_sales.reset_index(drop=True)

# Save transformed data
final_sales.to_csv(
    "data/processed/final_sales.csv",
    index=False
)

print("\nProcessed data saved successfully!")