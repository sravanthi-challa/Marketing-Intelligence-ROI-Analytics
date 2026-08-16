"""
Generate the Fact_Customer_Acquisition table.
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
# Load Dimension Tables
# ---------------------------------------

date_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_date.csv"
)

customer_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_customer.csv"
)

campaign_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_campaign.csv"
)

channel_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_channel.csv"
)

geography_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_geography.csv"
)


# ---------------------------------------
# Prepare Lookup Data
# ---------------------------------------

date_ids = (
    date_df["Date_ID"]
    .astype(int)
    .tolist()
)

customer_ids = (
    customer_df["Customer_ID"]
    .astype(int)
    .tolist()
)

campaign_ids = (
    campaign_df["Campaign_ID"]
    .astype(int)
    .tolist()
)

channel_ids = (
    channel_df["Channel_ID"]
    .astype(int)
    .tolist()
)

geography_ids = (
    geography_df["Geography_ID"]
    .astype(int)
    .tolist()
)


# ---------------------------------------
# Generate One Acquisition Record
# ---------------------------------------

def generate_customer_acquisition(
    acquisition_id,
    customer_id,
):
    """
    Generate one customer acquisition record.
    """

    # -----------------------------------
    # Acquisition Date
    # -----------------------------------

    date_id = random.choice(
        date_ids
    )

    # -----------------------------------
    # Marketing Dimensions
    # -----------------------------------

    campaign_id = random.choice(
        campaign_ids
    )

    channel_id = random.choice(
        channel_ids
    )

    geography_id = random.choice(
        geography_ids
    )

    # -----------------------------------
    # Acquisition Cost
    # -----------------------------------

    acquisition_cost = round(
        random.uniform(
            100,
            1500,
        ),
        2,
    )

    # -----------------------------------
    # First Order Value
    # -----------------------------------

    first_order_value = round(
        random.uniform(
            500,
            10000,
        ),
        2,
    )

    # -----------------------------------
    # Customer Lifetime Value
    # -----------------------------------

    lifetime_multiplier = random.uniform(
        1.5,
        5.0,
    )

    customer_lifetime_value = round(
        first_order_value
        * lifetime_multiplier,
        2,
    )

    return {
        "Acquisition_ID": acquisition_id,
        "Date_ID": date_id,
        "Customer_ID": customer_id,
        "Campaign_ID": campaign_id,
        "Channel_ID": channel_id,
        "Geography_ID": geography_id,
        "Acquisition_Cost": acquisition_cost,
        "First_Order_Value": first_order_value,
        "Customer_Lifetime_Value": customer_lifetime_value,
    }


# ---------------------------------------
# Generate Fact Table
# ---------------------------------------

def generate_fact_customer_acquisition():
    """
    Generate the Fact_Customer_Acquisition table.
    """

    records = []

    # One acquisition record per customer
    for acquisition_id, customer_id in enumerate(
        customer_ids,
        start=1,
    ):

        records.append(
            generate_customer_acquisition(
                acquisition_id,
                customer_id,
            )
        )

    df = pd.DataFrame(
        records
    )

    # -----------------------------------
    # Row Count Validation
    # -----------------------------------

    validate_row_count(
        df,
        ROWS["fact_customer_acquisition"],
    )

    # -----------------------------------
    # Primary Key Validation
    # -----------------------------------

    validate_duplicate_primary_key(
        df,
        "Acquisition_ID",
    )

    # -----------------------------------
    # Null Validation
    # -----------------------------------

    validate_null_values(
        df
    )

    # -----------------------------------
    # Foreign Key Validation
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

    if not df["Campaign_ID"].isin(
        campaign_ids
    ).all():

        raise ValueError(
            "Invalid Campaign_ID found."
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

    # -----------------------------------
    # Customer Uniqueness Validation
    # -----------------------------------

    if df["Customer_ID"].duplicated().any():

        raise ValueError(
            "A customer has more than one "
            "acquisition record."
        )

    # -----------------------------------
    # Business Rule Validation
    # -----------------------------------

    if not df["Acquisition_Cost"].gt(
        0
    ).all():

        raise ValueError(
            "Acquisition cost must be greater than zero."
        )

    if not df["First_Order_Value"].gt(
        0
    ).all():

        raise ValueError(
            "First order value must be greater than zero."
        )

    if not (
        df["Customer_Lifetime_Value"]
        >= df["First_Order_Value"]
    ).all():

        raise ValueError(
            "Customer lifetime value cannot be "
            "less than first order value."
        )

    # -----------------------------------
    # Save CSV
    # -----------------------------------

    output_file = (
        GENERATED_DATA_DIR
        / "fact_customer_acquisition.csv"
    )

    save_dataframe(
        df,
        output_file,
    )

    print_success(
        "Fact_Customer_Acquisition generated successfully."
    )

    return df