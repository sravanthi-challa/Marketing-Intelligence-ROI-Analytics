"""
Generate the Dim_Campaign table.
"""

import random
from datetime import timedelta

import pandas as pd

from config import (
    BASE_DIR,
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
# Load Reference Data
# ---------------------------------------

campaign_types_df = pd.read_csv(
    BASE_DIR / "data" / "reference" / "campaign_types.csv"
)

objectives_df = pd.read_csv(
    BASE_DIR / "data" / "reference" / "campaign_objectives.csv"
)

audience_df = pd.read_csv(
    BASE_DIR / "data" / "reference" / "target_audience.csv"
)

geography_df = pd.read_csv(
    BASE_DIR / "data" / "generated" / "dim_geography.csv"
)

channel_df = pd.read_csv(
    BASE_DIR / "data" / "generated" / "dim_channel.csv"
)


# ---------------------------------------
# Convert Reference Data to Lists
# ---------------------------------------

campaign_types = (
    campaign_types_df["Campaign_Type"]
    .dropna()
    .tolist()
)

objectives = (
    objectives_df["Objective"]
    .dropna()
    .tolist()
)

target_audiences = (
    audience_df["Target_Audience"]
    .dropna()
    .tolist()
)

geography_ids = (
    geography_df["Geography_ID"]
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


# ---------------------------------------
# Campaign Name Templates
# ---------------------------------------

CAMPAIGN_NAMES = [
    "Summer Sale",
    "Winter Sale",
    "Monsoon Offers",
    "Back to School",
    "Black Friday",
    "New Year Bonanza",
    "Diwali Mega Sale",
    "Festival Frenzy",
    "Mega Discount",
    "Flash Deals",
    "Weekend Sale",
    "Super Saver",
    "Grand Launch",
    "Exclusive Offers",
    "Holiday Specials",
    "Customer Appreciation",
    "Referral Rewards",
    "New Collection Launch",
]


# ---------------------------------------
# Generate One Campaign
# ---------------------------------------

def generate_campaign(campaign_id):
    """
    Generate one realistic campaign record.
    """

    campaign_name = (
        random.choice(CAMPAIGN_NAMES)
        + " 2025"
    )

    campaign_type = random.choice(
        campaign_types
    )

    objective = random.choice(
        objectives
    )

    channel_id = random.choice(
        channel_ids
    )

    geography_id = random.choice(
        geography_ids
    )

    # Generate campaign start date
    start_date = (
        pd.Timestamp("2025-01-01")
        + timedelta(
            days=random.randint(0, 300)
        )
    )

    # Campaign duration: 7–90 days
    duration = random.randint(7, 90)

    end_date = (
        start_date
        + timedelta(days=duration)
    )

    # Campaign budget
    budget = random.randint(
        50000,
        1000000,
    )

    # Campaign status
    status = random.choices(
        [
            "Completed",
            "Running",
            "Planned",
        ],
        weights=[
            70,
            20,
            10,
        ],
        k=1,
    )[0]

    return {
        "Campaign_ID": campaign_id,
        "Campaign_Name": campaign_name,
        "Campaign_Type": campaign_type,
        "Objective": objective,
        "Channel_ID": channel_id,
        "Geography_ID": geography_id,
        "Start_Date": start_date.date(),
        "End_Date": end_date.date(),
        "Budget": budget,
        "Target_Audience": random.choice(
            target_audiences
        ),
        "Status": status,
    }


# ---------------------------------------
# Generate Campaign Dimension
# ---------------------------------------

def generate_dim_campaign():
    """
    Generate the Dim_Campaign table.
    """

    campaigns = []

    for campaign_id in range(
        1,
        ROWS["dim_campaign"] + 1,
    ):
        campaigns.append(
            generate_campaign(
                campaign_id
            )
        )

    df = pd.DataFrame(
        campaigns
    )

    # -----------------------------------
    # Validation
    # -----------------------------------

    validate_row_count(
        df,
        ROWS["dim_campaign"],
    )

    validate_duplicate_primary_key(
        df,
        "Campaign_ID",
    )

    validate_null_values(
        df
    )

    # -----------------------------------
    # Save CSV
    # -----------------------------------

    output_file = (
        GENERATED_DATA_DIR
        / "dim_campaign.csv"
    )

    save_dataframe(
        df,
        output_file,
    )

    print_success(
        "Dim_Campaign generated successfully."
    )

    return df