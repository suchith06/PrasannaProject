# E-Commerce Data Engineering Pipeline

An end-to-end data engineering project that extracts raw e-commerce data from CSV files, transforms and validates the data using Python and Pandas, loads the processed data into PostgreSQL, performs SQL analysis, and visualizes business insights through an interactive Streamlit dashboard.

## Project Architecture

CSV Files
   ↓
Python Extraction
   ↓
Data Transformation & Validation
   ↓
Processed Dataset
   ↓
PostgreSQL
   ↓
SQL Analysis
   ↓
Streamlit Dashboard

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- SQL
- Streamlit
- Pytest
- python-dotenv
- Git & GitHub

## Project Structure

```text
ecommerce-data-engineering/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── orders.csv
│   │   ├── order_items.csv
│   │   └── products.csv
│   └── processed/
│       └── final_sales.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── sql/
│   ├── create_tables.sql
│   └── analysis.sql
│
├── dashboard/
│   └── app.py
│
├── tests/
│   └── test_data.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ETL Pipeline

### 1. Extract

Raw customer, order, order-item, and product data is extracted from CSV source files.

### 2. Transform

Python and Pandas are used to:

- Merge datasets
- Clean and validate records
- Handle data types
- Calculate line totals
- Prepare the final analytical dataset

### 3. Load

The transformed dataset is loaded into PostgreSQL for persistent storage and downstream analytics.

## Data Quality Testing

Automated tests are implemented using Pytest to validate:

- Null order IDs
- Null product IDs
- Duplicate records
- Quantity greater than zero
- Price greater than zero
- Line-total calculations
- Completed order status

Current test result:

```text
7 passed
```

## Dashboard

The Streamlit dashboard connects to PostgreSQL and provides:

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value
- Revenue by Category
- Revenue by Product
- Revenue by State
- Top Customers
- Monthly Revenue
- Category filtering
- State filtering
- Customer filtering
- Date-range filtering

## Run the ETL Pipeline

```bash
python src/pipeline.py
```

## Run Tests

```bash
pytest -v
```

## Run the Dashboard

```bash
streamlit run dashboard/app.py
```

Then open the local Streamlit URL displayed in the terminal.

## Environment Variables

Database credentials are stored in a local `.env` file rather than hard-coded into the application.

Example:

```text
DB_HOST=your_host
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
```

**Do not commit the `.env` file to GitHub.**

## Key Learning Outcomes

This project demonstrates practical experience with:

- Building an end-to-end ETL pipeline
- Data transformation using Pandas
- PostgreSQL database integration
- SQL-based data analysis
- Data-quality validation and automated testing
- Environment-variable management
- Interactive analytics dashboard development
- Structuring a production-style Python data engineering project