"""
Utility functions used across the data generation pipeline.
"""

import random
import numpy as np
import pandas as pd

from config import RANDOM_SEED

# ----------------------------
# Set Random Seed
# ----------------------------

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


def print_banner(title):
    """Print a formatted banner."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_success(message):
    """Print a success message."""
    print(f"✅ {message}")

def save_dataframe(df, output_path):
    """
    Save a DataFrame as a CSV file.
    """
    df.to_csv(output_path, index=False)
    print_success(f"Saved: {output_path.name}")