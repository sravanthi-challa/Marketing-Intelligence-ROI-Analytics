"""
Generate the Dim_Geography table.
"""

import pandas as pd

from config import BASE_DIR, GENERATED_DATA_DIR, ROWS
from validate import (
    validate_row_count,
    validate_duplicate_primary_key,
    validate_null_values,
)
from utils import print_success, save_dataframe


def generate_dim_geography():
    """
    Generate the Geography Dimension table.
    """

    reference_file = (
        BASE_DIR /
        "data" /
        "reference" /
        "regions.csv"
    )

    df = pd.read_csv(reference_file)

    validate_row_count(df, ROWS["dim_geography"])
    validate_duplicate_primary_key(df, "Geography_ID")
    validate_null_values(df)

    output_file = GENERATED_DATA_DIR / "dim_geography.csv"

    save_dataframe(df, output_file)

    print_success("Dim_Geography generated successfully.")

    return df