"""
Main entry point for the data generation pipeline.
"""

from config import GENERATED_DATA_DIR
from utils import print_banner, print_success

from generate_date import generate_dim_date
from generate_channel import generate_dim_channel


def main():
    print_banner("Marketing Intelligence ROI Analytics")

    print_success("Pipeline initialized.")

    print(f"\nOutput Folder:\n{GENERATED_DATA_DIR}")

    print("\nGenerating Dimension Tables...\n")

    date_df = generate_dim_date()
    channel_df = generate_dim_channel()

    print(f"\nDim_Date Rows     : {len(date_df)}")
    print(f"Dim_Channel Rows  : {len(channel_df)}")

    print_success("Pipeline completed successfully.")


if __name__ == "__main__":
    main()