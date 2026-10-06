import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load database credentials from .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Connect to PostgreSQL
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Read data from PostgreSQL
query = "SELECT * FROM final_sales;"

df = pd.read_sql(query, engine)
df["order_date"] = pd.to_datetime(df["order_date"])
min_date = df["order_date"].min().date()
max_date = df["order_date"].max().date()

# Dashboard
st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    layout="wide"
)

st.title("E-Commerce Sales Dashboard")
# Sidebar Filters
st.sidebar.header("Filters")


category_options = ["All"] + sorted(
    df["category"].dropna().unique().tolist()
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    category_options,
    key="category_filter"
)


if selected_category != "All":
    df = df[df["category"] == selected_category]
    # State Filter
state_options = ["All"] + sorted(
    df["state"].dropna().unique().tolist()
)
selected_state = st.sidebar.selectbox(
    "Select State",
    state_options,
    key="state_filter"
)


if selected_state != "All":
    df = df[df["state"] == selected_state]
    # Customer Filter
customer_options = ["All"] + sorted(
    df["customer_name"].dropna().unique().tolist()
)

selected_customer = st.sidebar.selectbox(
    "Select Customer",
    customer_options,
    key="customer_filter"
)


if selected_customer != "All":
    df = df[df["customer_name"] == selected_customer]
    # Date Range Filter

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
    key="date_filter"
)

if len(selected_dates) == 2:
    start_date, end_date = selected_dates

    df = df[
        (df["order_date"].dt.date >= start_date) &
        (df["order_date"].dt.date <= end_date)
    ]
   


# Calculate KPIs
total_revenue = df["line_total"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()
average_order_value = total_revenue / total_orders if total_orders > 0 else 0
if df.empty:
    st.warning("No sales data found for the selected filters.")
    st.stop()


# KPI Section
st.subheader("Sales Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"${total_revenue:,.2f}"
)

col2.metric(
    "Total Orders",
    total_orders
)

col3.metric(
    "Total Customers",
    total_customers
)

col4.metric(
    "Average Order Value",
    f"${average_order_value:,.2f}"
)

# Show data
st.subheader("Sales Data")

st.dataframe(df, use_container_width=True)

st.success(f"Successfully loaded {len(df)} rows from PostgreSQL.")
# Revenue by Category
category_revenue = (
    df.groupby("category")["line_total"]
    .sum()
    .reset_index()
)

# Revenue by Product
product_revenue = (
    df.groupby("product_name")["line_total"]
    .sum()
    .reset_index()
    .sort_values("line_total", ascending=False)
)

# Two-column layout
chart1, chart2 = st.columns(2)

with chart1:
    st.subheader("Revenue by Category")
    st.bar_chart(
        category_revenue,
        x="category",
        y="line_total"
    )

with chart2:
    st.subheader("Revenue by Product")
    st.bar_chart(
        product_revenue,
        x="product_name",
        y="line_total"
    )

# Revenue by State
state_revenue = (
    df.groupby("state")["line_total"]
    .sum()
    .reset_index()
    .sort_values("line_total", ascending=False)
)

# Top Customers
customer_revenue = (
    df.groupby("customer_name")["line_total"]
    .sum()
    .reset_index()
    .sort_values("line_total", ascending=False)
)

# Second row of charts
chart3, chart4 = st.columns(2)

with chart3:
    st.subheader("Revenue by State")
    st.bar_chart(
        state_revenue,
        x="state",
        y="line_total"
    )

with chart4:
    st.subheader("Top Customers")
    st.bar_chart(
        customer_revenue,
        x="customer_name",
        y="line_total"
    )
# Monthly Revenue
st.subheader("Monthly Revenue")

df["order_date"] = pd.to_datetime(df["order_date"])

monthly_revenue = (
    df.groupby(df["order_date"].dt.to_period("M"))["line_total"]
    .sum()
    .reset_index()
)

monthly_revenue["order_date"] = monthly_revenue["order_date"].astype(str)

st.line_chart(
    monthly_revenue,
    x="order_date",
    y="line_total"
)
