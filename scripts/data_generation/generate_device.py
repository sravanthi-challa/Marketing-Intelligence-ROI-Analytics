"""
Generate the Dim_Device table.
"""

import pandas as pd

from config import BASE_DIR, GENERATED_DATA_DIR, ROWS
from validate import (
    validate_row_count,
    validate_duplicate_primary_key,
    validate_null_values,
)
from utils import print_success, save_dataframe


def generate_dim_device():
    """
    Generate the Device Dimension table.
    """

    reference_file = (
        BASE_DIR /
        "data" /
        "reference" /
        "devices.csv"
    )

    df = pd.read_csv(reference_file)

    validate_row_count(df, ROWS["dim_device"])
    validate_duplicate_primary_key(df, "Device_ID")
    validate_null_values(df)

    output_file = GENERATED_DATA_DIR / "dim_device.csv"

    save_dataframe(df, output_file)

    print_success("Dim_Device generated successfully.")

    return df