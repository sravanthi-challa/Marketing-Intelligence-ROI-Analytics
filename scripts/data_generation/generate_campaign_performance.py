"""
Generate the Fact_Campaign_Performance table.
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
# Valid Dimension IDs
# ---------------------------------------

date_ids = (
    date_df["Date_ID"]
    .dropna()
    .astype(int)
    .tolist()
)

campaign_ids = (
    campaign_df["Campaign_ID"]
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


# ---------------------------------------
# Generate One Campaign Performance Record
# ---------------------------------------

def generate_campaign_performance(
    performance_id
):
    """
    Generate one realistic campaign
    performance record.
    """

    # Select dimension keys
    date_id = random.choice(date_ids)

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
    # Impressions
    # -----------------------------------

    impressions = random.randint(
        5_000,
        250_000,
    )

    # -----------------------------------
    # Click Through Rate
    # -----------------------------------

    ctr = random.uniform(
        0.01,
        0.08,
    )

    clicks = int(
        impressions * ctr
    )

    # Ensure at least one click
    clicks = max(
        clicks,
        1,
    )

    # -----------------------------------
    # Lead Conversion Rate
    # -----------------------------------

    lead_rate = random.uniform(
        0.05,
        0.30,
    )

    leads = int(
        clicks * lead_rate
    )

    # Ensure leads do not exceed clicks
    leads = min(
        leads,
        clicks,
    )

    # -----------------------------------
    # Conversion Rate
    # -----------------------------------

    conversion_rate = random.uniform(
        0.05,
        0.30,
    )

    conversions = int(
        leads * conversion_rate
    )

    # Ensure conversions do not exceed leads
    conversions = min(
        conversions,
        leads,
    )

    # -----------------------------------
    # Campaign Spend
    # -----------------------------------

    cpm = random.uniform(
        80,
        400,
    )

    spend = round(
        impressions
        / 1000
        * cpm,
        2,
    )

    # -----------------------------------
    # Revenue
    # -----------------------------------

    average_order_value = random.uniform(
        800,
        5_000,
    )

    revenue = round(
        conversions
        * average_order_value,
        2,
    )

    return {
        "Campaign_Performance_ID": performance_id,
        "Date_ID": date_id,
        "Campaign_ID": campaign_id,
        "Channel_ID": channel_id,
        "Geography_ID": geography_id,
        "Impressions": impressions,
        "Clicks": clicks,
        "Leads": leads,
        "Conversions": conversions,
        "Spend": spend,
        "Revenue": revenue,
    }


# ---------------------------------------
# Generate Fact Campaign Performance
# ---------------------------------------

def generate_fact_campaign_performance():
    """
    Generate the Fact_Campaign_Performance table.
    """

    records = []

    for performance_id in range(
        1,
        ROWS["fact_campaign_performance"] + 1,
    ):

        records.append(
            generate_campaign_performance(
                performance_id
            )
        )

    df = pd.DataFrame(
        records
    )

    # -----------------------------------
    # Basic Validation
    # -----------------------------------

    validate_row_count(
        df,
        ROWS["fact_campaign_performance"],
    )

    validate_duplicate_primary_key(
        df,
        "Campaign_Performance_ID",
    )

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
    # Funnel Validation
    # -----------------------------------

    if not (
        df["Clicks"]
        <= df["Impressions"]
    ).all():

        raise ValueError(
            "Clicks cannot exceed impressions."
        )

    if not (
        df["Leads"]
        <= df["Clicks"]
    ).all():

        raise ValueError(
            "Leads cannot exceed clicks."
        )

    if not (
        df["Conversions"]
        <= df["Leads"]
    ).all():

        raise ValueError(
            "Conversions cannot exceed leads."
        )

    # -----------------------------------
    # Measure Validation
    # -----------------------------------

    if not df["Impressions"].gt(
        0
    ).all():

        raise ValueError(
            "Impressions must be greater than zero."
        )

    if not df["Spend"].gt(
        0
    ).all():

        raise ValueError(
            "Spend must be greater than zero."
        )

    if not df["Revenue"].ge(
        0
    ).all():

        raise ValueError(
            "Revenue cannot be negative."
        )

    # -----------------------------------
    # Save CSV
    # -----------------------------------

    output_file = (
        GENERATED_DATA_DIR
        / "fact_campaign_performance.csv"
    )

    save_dataframe(
        df,
        output_file,
    )

    print_success(
        "Fact_Campaign_Performance generated successfully."
    )

    return df