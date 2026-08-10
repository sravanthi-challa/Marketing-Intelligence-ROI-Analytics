"""
Generate the Dim_Customer table.
"""

import random
from datetime import timedelta

import pandas as pd

from config import (
    BASE_DIR,
    GENERATED_DATA_DIR,
    ROWS,
    START_DATE,
    END_DATE,
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
# Load Existing Dimensions
# ---------------------------------------

geography_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_geography.csv"
)

channel_df = pd.read_csv(
    GENERATED_DATA_DIR / "dim_channel.csv"
)


# ---------------------------------------
# Lookup IDs
# ---------------------------------------

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
# Customer Name Data
# ---------------------------------------

FIRST_NAMES_MALE = [
    "Aarav",
    "Arjun",
    "Rahul",
    "Rohan",
    "Vikram",
    "Aditya",
    "Karan",
    "Varun",
    "Akash",
    "Siddharth",
    "Manish",
    "Nikhil",
    "Harsh",
    "Vivek",
    "Anil",
]

FIRST_NAMES_FEMALE = [
    "Ananya",
    "Priya",
    "Sneha",
    "Aishwarya",
    "Kavya",
    "Pooja",
    "Neha",
    "Shreya",
    "Divya",
    "Ishita",
    "Meera",
    "Swati",
    "Riya",
    "Nandini",
    "Lakshmi",
]

LAST_NAMES = [
    "Sharma",
    "Reddy",
    "Kumar",
    "Patel",
    "Nair",
    "Rao",
    "Singh",
    "Verma",
    "Iyer",
    "Das",
    "Gupta",
    "Joshi",
    "Mehta",
    "Pillai",
    "Naidu",
]


# ---------------------------------------
# Age Group Function
# ---------------------------------------

def get_age_group(age):
    """
    Return the age group for a given age.
    """

    if 18 <= age <= 25:
        return "18-25"

    if 26 <= age <= 35:
        return "26-35"

    if 36 <= age <= 45:
        return "36-45"

    if 46 <= age <= 55:
        return "46-55"

    return "56-65"


# ---------------------------------------
# Generate One Customer
# ---------------------------------------

def generate_customer(customer_id):
    """
    Generate one realistic customer record.
    """

    # Gender
    gender = random.choice(
        ["Male", "Female"]
    )

    # Name
    if gender == "Male":
        first_name = random.choice(
            FIRST_NAMES_MALE
        )
    else:
        first_name = random.choice(
            FIRST_NAMES_FEMALE
        )

    last_name = random.choice(
        LAST_NAMES
    )

    customer_name = (
        f"{first_name} {last_name}"
    )

    # Age
    age = random.randint(
        18,
        65,
    )

    age_group = get_age_group(age)

    # Geography
    geography_id = random.choice(
        geography_ids
    )

    # Acquisition channel
    acquisition_channel_id = random.choice(
        channel_ids
    )

    # Active status
    is_active = random.random() < 0.90

    # Customer segment
    if not is_active:

        customer_segment = "Inactive"

    else:

        customer_segment = random.choices(
            [
                "Standard",
                "Premium",
                "VIP",
            ],
            weights=[
                70,
                25,
                5,
            ],
            k=1,
        )[0]

    # Registration date
    start = pd.Timestamp(
        START_DATE
    )

    end = pd.Timestamp(
        END_DATE
    )

    days_between = (
        end - start
    ).days

    registration_date = (
        start
        + timedelta(
            days=random.randint(
                0,
                days_between,
            )
        )
    )

    return {
        "Customer_ID": customer_id,
        "Customer_Name": customer_name,
        "Gender": gender,
        "Age": age,
        "Age_Group": age_group,
        "Geography_ID": geography_id,
        "Acquisition_Channel_ID": acquisition_channel_id,
        "Customer_Segment": customer_segment,
        "Registration_Date": registration_date.date(),
        "Is_Active": is_active,
    }


# ---------------------------------------
# Generate Customer Dimension
# ---------------------------------------

def generate_dim_customer():
    """
    Generate the Dim_Customer table.
    """

    customers = []

    for customer_id in range(
        1,
        ROWS["dim_customer"] + 1,
    ):

        customers.append(
            generate_customer(
                customer_id
            )
        )

    df = pd.DataFrame(
        customers
    )

    # -----------------------------------
    # Validation
    # -----------------------------------

    validate_row_count(
        df,
        ROWS["dim_customer"],
    )

    validate_duplicate_primary_key(
        df,
        "Customer_ID",
    )

    validate_null_values(
        df
    )

    # -----------------------------------
    # Additional Validation
    # -----------------------------------

    if not df["Age"].between(
        18,
        65,
    ).all():

        raise ValueError(
            "Customer age must be between 18 and 65."
        )

    # Verify age groups
    expected_age_groups = (
        df["Age"]
        .apply(get_age_group)
    )

    if not (
        expected_age_groups
        == df["Age_Group"]
    ).all():

        raise ValueError(
            "Age_Group does not match Age."
        )

    # Verify Geography IDs
    if not df["Geography_ID"].isin(
        geography_ids
    ).all():

        raise ValueError(
            "Invalid Geography_ID found."
        )

    # Verify Channel IDs
    if not df[
        "Acquisition_Channel_ID"
    ].isin(channel_ids).all():

        raise ValueError(
            "Invalid Acquisition_Channel_ID found."
        )

    # Verify inactive customers
    inactive_check = df[
        ~df["Is_Active"]
    ]["Customer_Segment"]

    if not (
        inactive_check == "Inactive"
    ).all():

        raise ValueError(
            "Inactive customers must have "
            "Customer_Segment = Inactive."
        )

    # -----------------------------------
    # Save CSV
    # -----------------------------------

    output_file = (
        GENERATED_DATA_DIR
        / "dim_customer.csv"
    )

    save_dataframe(
        df,
        output_file,
    )

    print_success(
        "Dim_Customer generated successfully."
    )

    return df