"""
Generate the Dim_Channel table.
"""

import pandas as pd

from config import BASE_DIR, GENERATED_DATA_DIR
from validate import (
    validate_row_count,
    validate_duplicate_primary_key,
    validate_null_values,
)
from utils import print_success, save_dataframe


def generate_dim_channel():
    """
    Generate the Channel Dimension table.
    """

    reference_file = (
        BASE_DIR /
        "data" /
        "reference" /
        "channels.csv"
    )

    df = pd.read_csv(reference_file)

    # --------------------
    # Validation
    # --------------------

    validate_row_count(df, 6)
    validate_duplicate_primary_key(df, "Channel_ID")
    validate_null_values(df)

    # --------------------
    # Save
    # --------------------

    output_file = GENERATED_DATA_DIR / "dim_channel.csv"

    save_dataframe(df, output_file)

    print_success("Dim_Channel generated successfully.")

    return df