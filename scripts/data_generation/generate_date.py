"""
Generate the Dim_Date table.
"""

import pandas as pd

from config import (
    START_DATE,
    END_DATE,
    GENERATED_DATA_DIR,
    ROWS
)

from validate import (
    validate_row_count,
    validate_duplicate_primary_key,
    validate_null_values
)

from utils import print_success


def generate_dim_date():
    """
    Generate the Date Dimension table.
    """

    dates = pd.date_range(
        start=START_DATE,
        end=END_DATE,
        freq="D"
    )

    df = pd.DataFrame({
        "Date_ID": dates.strftime("%Y%m%d").astype(int),
        "Full_Date": dates,
        "Day": dates.day,
        "Month": dates.month,
        "Month_Name": dates.strftime("%B"),
        "Quarter": dates.quarter,
        "Year": dates.year,
        "Weekday": dates.strftime("%A"),
        "Is_Weekend": dates.weekday >= 5
    })

    # -----------------------
    # Validation
    # -----------------------

    validate_row_count(df, ROWS["dim_date"])
    validate_duplicate_primary_key(df, "Date_ID")
    validate_null_values(df)

    # -----------------------
    # Save CSV
    # -----------------------

    output_file = GENERATED_DATA_DIR / "dim_date.csv"

    df.to_csv(output_file, index=False)

    print_success("Dim_Date generated successfully.")

    return df