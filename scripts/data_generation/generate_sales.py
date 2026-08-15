"""
Generate the Fact_Sales table.
"""

import random

import pandas as pd

from config import (
    GENERATED_DATA_DIR,
    ROWS,
)

from validate import (
    validate_row_count,
    validate_duplicate_primary_key,
    validate_null_values,
)

from utils import (
    save_dataframe,
    print_success,
)


# ---------------------------------------
# Load Existing Dimension Tables
# ---------------------------------------

date_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_date.csv"
)

customer_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_customer.csv"
)

product_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_product.csv"
)

channel_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_channel.csv"
)

geography_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_geography.csv"
)

device_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_device.csv"
)


# ---------------------------------------
# Create Lookup Dictionaries
# ---------------------------------------

product_lookup = (
    product_df
    .set_index("Product_ID")
    .to_dict("index")
)


# ---------------------------------------
# Valid Dimension IDs
# ---------------------------------------

date_ids = (
    date_df["Date_ID"]
    .dropna()
    .astype(int)
    .tolist()
)

customer_ids = (
    customer_df["Customer_ID"]
    .dropna()
    .astype(int)
    .tolist()
)

product_ids = (
    product_df["Product_ID"]
    .dropna()
    .astype(int)
    .tolist()
)

channel_ids = (
    channel_df["Channel_ID"]
    .dropna()
    .astype(int)
    .tolist()
)

geography_ids = (
    geography_df["Geography_ID"]
    .dropna()
    .astype(int)
    .tolist()
)

device_ids = (
    device_df["Device_ID"]
    .dropna()
    .astype(int)
    .tolist()
)


# ---------------------------------------
# Payment Methods
# ---------------------------------------

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery",
    "Wallet",
]

PAYMENT_WEIGHTS = [
    35,
    20,
    15,
    10,
    10,
    10,
]


# ---------------------------------------
# Discount Options
# ---------------------------------------

DISCOUNT_OPTIONS = [
    0,
    5,
    10,
    15,
    20,
    25,
    30,
]

DISCOUNT_WEIGHTS = [
    30,
    20,
    20,
    12,
    8,
    6,
    4,
]


# ---------------------------------------
# Quantity Options
# ---------------------------------------

QUANTITY_OPTIONS = [
    1,
    2,
    3,
    4,
    5,
]

QUANTITY_WEIGHTS = [
    65,
    20,
    8,
    5,
    2,
]


# ---------------------------------------
# Generate One Sales Transaction
# ---------------------------------------

def generate_sale(sales_id):
    """
    Generate one realistic sales transaction.
    """

    # Select dimension keys
    date_id = random.choice(date_ids)

    customer_id = random.choice(
        customer_ids
    )

    product_id = random.choice(
        product_ids
    )

    channel_id = random.choice(
        channel_ids
    )

    geography_id = random.choice(
        geography_ids
    )

    device_id = random.choice(
        device_ids
    )

    # Get product information
    product = product_lookup[
        product_id
    ]

    unit_price = float(
        product["Price"]
    )

    product_cost = float(
        product["Cost"]
    )

    # Quantity
    quantity = random.choices(
        QUANTITY_OPTIONS,
        weights=QUANTITY_WEIGHTS,
        k=1,
    )[0]

    # Discount
    discount_percent = random.choices(
        DISCOUNT_OPTIONS,
        weights=DISCOUNT_WEIGHTS,
        k=1,
    )[0]

    # Gross sales amount
    gross_amount = (
        quantity * unit_price
    )

    # Discount amount
    discount_amount = round(
        gross_amount
        * discount_percent
        / 100,
        2,
    )

    # Final sales amount
    sales_amount = round(
        gross_amount
        - discount_amount,
        2,
    )

    # Cost
    cost_amount = round(
        quantity * product_cost,
        2,
    )

    # Profit
    profit_amount = round(
        sales_amount
        - cost_amount,
        2,
    )

    # Payment method
    payment_method = random.choices(
        PAYMENT_METHODS,
        weights=PAYMENT_WEIGHTS,
        k=1,
    )[0]

    return {
        "Sales_ID": sales_id,
        "Date_ID": date_id,
        "Customer_ID": customer_id,
        "Product_ID": product_id,
        "Channel_ID": channel_id,
        "Geography_ID": geography_id,
        "Device_ID": device_id,
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Discount_Percent": discount_percent,
        "Discount_Amount": discount_amount,
        "Sales_Amount": sales_amount,
        "Cost_Amount": cost_amount,
        "Profit_Amount": profit_amount,
        "Payment_Method": payment_method,
    }


# ---------------------------------------
# Generate Fact Sales
# ---------------------------------------

def generate_fact_sales():
    """
    Generate the Fact_Sales table.
    """

    sales = []

    for sales_id in range(
        1,
        ROWS["fact_sales"] + 1,
    ):

        sales.append(
            generate_sale(
                sales_id
            )
        )

    df = pd.DataFrame(
        sales
    )

    # -----------------------------------
    # Validation
    # -----------------------------------

    validate_row_count(
        df,
        ROWS["fact_sales"],
    )

    validate_duplicate_primary_key(
        df,
        "Sales_ID",
    )

    validate_null_values(
        df
    )

    # -----------------------------------
    # Business Rule Validation
    # -----------------------------------

    if not df["Quantity"].ge(1).all():
        raise ValueError(
            "Quantity must be at least 1."
        )

    if not df[
        "Discount_Percent"
    ].between(0, 30).all():

        raise ValueError(
            "Discount_Percent must be "
            "between 0 and 30."
        )

    if not df[
        "Sales_Amount"
    ].gt(0).all():

        raise ValueError(
            "Sales_Amount must be greater than 0."
        )

    if not df[
        "Cost_Amount"
    ].gt(0).all():

        raise ValueError(
            "Cost_Amount must be greater than 0."
        )

    # -----------------------------------
    # Validate Foreign Keys
    # -----------------------------------

    if not df["Date_ID"].isin(
        date_ids
    ).all():

        raise ValueError(
            "Invalid Date_ID found."
        )

    if not df["Customer_ID"].isin(
        customer_ids
    ).all():

        raise ValueError(
            "Invalid Customer_ID found."
        )

    if not df["Product_ID"].isin(
        product_ids
    ).all():

        raise ValueError(
            "Invalid Product_ID found."
        )

    if not df["Channel_ID"].isin(
        channel_ids
    ).all():

        raise ValueError(
            "Invalid Channel_ID found."
        )

    if not df["Geography_ID"].isin(
        geography_ids
    ).all():

        raise ValueError(
            "Invalid Geography_ID found."
        )

    if not df["Device_ID"].isin(
        device_ids
    ).all():

        raise ValueError(
            "Invalid Device_ID found."
        )

    # -----------------------------------
    # Validate Profit Calculation
    # -----------------------------------

    calculated_profit = (
        df["Sales_Amount"]
        - df["Cost_Amount"]
    ).round(2)

    if not (
        calculated_profit
        == df["Profit_Amount"]
    ).all():

        raise ValueError(
            "Profit_Amount calculation is incorrect."
        )

    # -----------------------------------
    # Save CSV
    # -----------------------------------

    output_file = (
        GENERATED_DATA_DIR
        / "fact_sales.csv"
    )

    save_dataframe(
        df,
        output_file,
    )

    print_success(
        "Fact_Sales generated successfully."
    )

    return df
