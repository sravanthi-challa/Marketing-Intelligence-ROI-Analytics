"""
Full data quality validation for the
Marketing Intelligence ROI Analytics dataset.
"""

from pathlib import Path

import pandas as pd


# ---------------------------------------
# Project Paths
# ---------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

GENERATED_DATA_DIR = (
    BASE_DIR / "data" / "generated"
)


# ---------------------------------------
# Expected Row Counts
# ---------------------------------------

EXPECTED_ROWS = {
    "dim_date.csv": 365,
    "dim_channel.csv": 6,
    "dim_geography.csv": 30,
    "dim_device.csv": 6,
    "dim_product.csv": 500,
    "dim_campaign.csv": 20,
    "dim_customer.csv": 10000,
    "fact_sales.csv": 100000,
    "fact_campaign_performance.csv": 25000,
    "fact_customer_acquisition.csv": 10000,
}


# ---------------------------------------
# Helper Functions
# ---------------------------------------

def load_table(filename):
    """Load a generated CSV file."""

    path = GENERATED_DATA_DIR / filename

    if not path.exists():
        raise FileNotFoundError(
            f"Missing file: {filename}"
        )

    return pd.read_csv(path)


def check_row_count(
    df,
    filename,
    expected,
):
    """Validate row count."""

    actual = len(df)

    if actual != expected:
        raise ValueError(
            f"{filename}: expected {expected} rows, "
            f"found {actual}."
        )

    print(
        f"✅ {filename}: {actual:,} rows"
    )


def check_primary_key(
    df,
    filename,
    column,
):
    """Validate primary key."""

    if df[column].isnull().any():
        raise ValueError(
            f"{filename}: NULL values found "
            f"in primary key {column}."
        )

    if df[column].duplicated().any():
        raise ValueError(
            f"{filename}: duplicate values found "
            f"in primary key {column}."
        )

    print(
        f"✅ {filename}: {column} is valid"
    )


def check_no_nulls(
    df,
    filename,
):
    """Check for unexpected null values."""

    null_counts = df.isnull().sum()

    null_columns = (
        null_counts[
            null_counts > 0
        ]
    )

    if not null_columns.empty:

        raise ValueError(
            f"{filename}: NULL values found:\n"
            f"{null_columns}"
        )

    print(
        f"✅ {filename}: no NULL values"
    )


def check_foreign_key(
    fact_df,
    fact_column,
    dimension_df,
    dimension_column,
    fact_name,
):
    """Validate a foreign key relationship."""

    invalid_values = (
        ~fact_df[fact_column].isin(
            dimension_df[dimension_column]
        )
    )

    if invalid_values.any():

        count = invalid_values.sum()

        raise ValueError(
            f"{fact_name}: {count} invalid "
            f"values in {fact_column}."
        )

    print(
        f"✅ {fact_name}: {fact_column} → "
        f"{dimension_column}"
    )


# =======================================
# Main Validation
# =======================================

def main():

    print("\n" + "=" * 70)
    print(
        "MARKETING INTELLIGENCE ROI ANALYTICS"
    )
    print(
        "FULL DATA QUALITY VALIDATION"
    )
    print("=" * 70)

    # -----------------------------------
    # Load all tables
    # -----------------------------------

    tables = {}

    for filename in EXPECTED_ROWS:

        tables[filename] = load_table(
            filename
        )

    # -----------------------------------
    # 1. Row Count Validation
    # -----------------------------------

    print(
        "\n--- ROW COUNT VALIDATION ---"
    )

    for filename, expected in (
        EXPECTED_ROWS.items()
    ):

        check_row_count(
            tables[filename],
            filename,
            expected,
        )

    # -----------------------------------
    # 2. Primary Key Validation
    # -----------------------------------

    print(
        "\n--- PRIMARY KEY VALIDATION ---"
    )

    primary_keys = {
        "dim_date.csv": "Date_ID",
        "dim_channel.csv": "Channel_ID",
        "dim_geography.csv": "Geography_ID",
        "dim_device.csv": "Device_ID",
        "dim_product.csv": "Product_ID",
        "dim_campaign.csv": "Campaign_ID",
        "dim_customer.csv": "Customer_ID",
        "fact_sales.csv": "Sales_ID",
        "fact_campaign_performance.csv":
            "Campaign_Performance_ID",
        "fact_customer_acquisition.csv":
            "Acquisition_ID",
    }

    for filename, column in (
        primary_keys.items()
    ):

        check_primary_key(
            tables[filename],
            filename,
            column,
        )

    # -----------------------------------
    # 3. NULL Validation
    # -----------------------------------

    print(
        "\n--- NULL VALIDATION ---"
    )

    for filename, df in tables.items():

        check_no_nulls(
            df,
            filename,
        )

    # -----------------------------------
    # 4. Foreign Key Validation
    # -----------------------------------

    print(
        "\n--- FOREIGN KEY VALIDATION ---"
    )

    # Fact Sales

    sales = tables[
        "fact_sales.csv"
    ]

    check_foreign_key(
        sales,
        "Date_ID",
        tables["dim_date.csv"],
        "Date_ID",
        "Fact_Sales",
    )

    check_foreign_key(
        sales,
        "Product_ID",
        tables["dim_product.csv"],
        "Product_ID",
        "Fact_Sales",
    )

    check_foreign_key(
        sales,
        "Customer_ID",
        tables["dim_customer.csv"],
        "Customer_ID",
        "Fact_Sales",
    )

    check_foreign_key(
        sales,
        "Channel_ID",
        tables["dim_channel.csv"],
        "Channel_ID",
        "Fact_Sales",
    )

    check_foreign_key(
        sales,
        "Geography_ID",
        tables["dim_geography.csv"],
        "Geography_ID",
        "Fact_Sales",
    )

    check_foreign_key(
        sales,
        "Device_ID",
        tables["dim_device.csv"],
        "Device_ID",
        "Fact_Sales",
    )

    # Campaign Performance

    campaign_perf = tables[
        "fact_campaign_performance.csv"
    ]

    check_foreign_key(
        campaign_perf,
        "Date_ID",
        tables["dim_date.csv"],
        "Date_ID",
        "Fact_Campaign_Performance",
    )

    check_foreign_key(
        campaign_perf,
        "Campaign_ID",
        tables["dim_campaign.csv"],
        "Campaign_ID",
        "Fact_Campaign_Performance",
    )

    check_foreign_key(
        campaign_perf,
        "Channel_ID",
        tables["dim_channel.csv"],
        "Channel_ID",
        "Fact_Campaign_Performance",
    )

    check_foreign_key(
        campaign_perf,
        "Geography_ID",
        tables["dim_geography.csv"],
        "Geography_ID",
        "Fact_Campaign_Performance",
    )

    # Customer Acquisition

    acquisition = tables[
        "fact_customer_acquisition.csv"
    ]

    check_foreign_key(
        acquisition,
        "Date_ID",
        tables["dim_date.csv"],
        "Date_ID",
        "Fact_Customer_Acquisition",
    )

    check_foreign_key(
        acquisition,
        "Customer_ID",
        tables["dim_customer.csv"],
        "Customer_ID",
        "Fact_Customer_Acquisition",
    )

    check_foreign_key(
        acquisition,
        "Campaign_ID",
        tables["dim_campaign.csv"],
        "Campaign_ID",
        "Fact_Customer_Acquisition",
    )

    check_foreign_key(
        acquisition,
        "Channel_ID",
        tables["dim_channel.csv"],
        "Channel_ID",
        "Fact_Customer_Acquisition",
    )

    check_foreign_key(
        acquisition,
        "Geography_ID",
        tables["dim_geography.csv"],
        "Geography_ID",
        "Fact_Customer_Acquisition",
    )

    # -----------------------------------
    # 5. Business Rule Validation
    # -----------------------------------

    print(
        "\n--- BUSINESS RULE VALIDATION ---"
    )

    # Campaign funnel

    if not (
        campaign_perf["Clicks"]
        <= campaign_perf["Impressions"]
    ).all():

        raise ValueError(
            "Campaign Performance: "
            "Clicks exceed Impressions."
        )

    print(
        "✅ Clicks <= Impressions"
    )

    if not (
        campaign_perf["Leads"]
        <= campaign_perf["Clicks"]
    ).all():

        raise ValueError(
            "Campaign Performance: "
            "Leads exceed Clicks."
        )

    print(
        "✅ Leads <= Clicks"
    )

    if not (
        campaign_perf["Conversions"]
        <= campaign_perf["Leads"]
    ).all():

        raise ValueError(
            "Campaign Performance: "
            "Conversions exceed Leads."
        )

    print(
        "✅ Conversions <= Leads"
    )

    # Customer acquisition

    if not (
        acquisition[
            "Customer_Lifetime_Value"
        ]
        >= acquisition[
            "First_Order_Value"
        ]
    ).all():

        raise ValueError(
            "Customer Acquisition: "
            "LTV is less than First Order Value."
        )

    print(
        "✅ Customer LTV >= First Order Value"
    )

    # One acquisition per customer

    if acquisition[
        "Customer_ID"
    ].duplicated().any():

        raise ValueError(
            "Customer Acquisition: "
            "duplicate Customer_ID found."
        )

    print(
        "✅ One acquisition per customer"
    )

    # -----------------------------------
    # Final Result
    # -----------------------------------

    print("\n" + "=" * 70)

    print(
        "🎉 ALL DATA QUALITY CHECKS PASSED"
    )

    print("=" * 70)


# ---------------------------------------
# Entry Point
# ---------------------------------------

if __name__ == "__main__":
    main()