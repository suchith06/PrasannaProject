import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Create PostgreSQL connection
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Read processed data
final_sales = pd.read_csv("data/processed/final_sales.csv")

print("DATA TO LOAD:")
print(final_sales)

# Load into PostgreSQL
final_sales.to_sql(
    "final_sales",
    engine,
    if_exists="replace",
    index=False
)

print("\nData loaded successfully into PostgreSQL!")