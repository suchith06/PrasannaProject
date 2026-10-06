import pandas as pd

# Load processed data
df = pd.read_csv("data/processed/final_sales.csv")


def test_no_null_order_id():
    assert df["order_id"].notnull().all()


def test_no_null_product_id():
    assert df["product_id"].notnull().all()


def test_no_duplicate_rows():
    assert not df.duplicated().any()


def test_quantity_greater_than_zero():
    assert (df["quantity"] > 0).all()


def test_price_greater_than_zero():
    assert (df["price"] > 0).all()


def test_line_total_calculation():
    expected = df["quantity"] * df["price"]
    assert (df["line_total"].round(2) == expected.round(2)).all()


def test_status_completed():
    assert (df["status"] == "Completed").all()