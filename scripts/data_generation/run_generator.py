"""
Main entry point for the data generation pipeline.
"""

from config import GENERATED_DATA_DIR
from utils import print_banner, print_success


def main():
    print_banner("Marketing Intelligence ROI Analytics")

    print_success("Pipeline initialized successfully.")

    print(f"\nOutput Folder:\n{GENERATED_DATA_DIR}")


if __name__ == "__main__":
    main()