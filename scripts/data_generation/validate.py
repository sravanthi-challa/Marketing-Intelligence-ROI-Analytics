"""
Validation functions for generated datasets.
"""


def validate_row_count(df, expected_rows):
    """
    Check whether the DataFrame has the expected number of rows.
    """
    if len(df) != expected_rows:
        raise ValueError(
            f"Expected {expected_rows} rows but found {len(df)}."
        )


def validate_duplicate_primary_key(df, primary_key):
    """
    Ensure the primary key contains no duplicate values.
    """
    if df[primary_key].duplicated().any():
        raise ValueError(
            f"Duplicate values found in primary key '{primary_key}'."
        )


def validate_null_values(df):
    """
    Ensure the DataFrame contains no NULL values.
    """
    if df.isnull().sum().sum() > 0:
        raise ValueError(
            "NULL values found in the dataset."
        )