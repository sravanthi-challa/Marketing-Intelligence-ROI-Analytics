"""
Main entry point for the data generation pipeline.
"""

from utils import print_banner, print_success
from config import GENERATED_DATA_DIR

from generate_date import generate_dim_date


def main():

    print_banner("Marketing Intelligence ROI Analytics")

    print_success("Pipeline initialized.")

    print(f"\nOutput Folder:\n{GENERATED_DATA_DIR}")

    print("\nGenerating Dim_Date...\n")

    df = generate_dim_date()

    print(f"\nRows Generated : {len(df)}")
    print(f"Columns        : {len(df.columns)}")

    print_success("Pipeline completed successfully.")


if __name__ == "__main__":
    main()