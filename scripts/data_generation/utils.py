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

# ----------------------------
# Print Functions
# ----------------------------

def print_banner(title):
    """
    Print a formatted banner.
    """
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_success(message):
    """
    Print a success message.
    """
    print(f"✅ {message}")


# ----------------------------
# Save DataFrame
# ----------------------------

def save_dataframe(df, output_path):
    """
    Save a DataFrame as a CSV file.
    """
    df.to_csv(output_path, index=False)
    print_success(f"Saved: {output_path.name}")


# ----------------------------
# SKU Generator
# ----------------------------

def generate_sku(category, product_id):
    """
    Generate a SKU like ELE-0001 or FAS-0001.
    """
    words = category.replace("&", "").split()

    if len(words) == 1:
        prefix = words[0][:3].upper()
    else:
        prefix = "".join(word[0] for word in words).upper()

        if len(prefix) < 3:
            prefix = (prefix + words[0][:3]).upper()[:3]

    return f"{prefix}-{product_id:04d}"