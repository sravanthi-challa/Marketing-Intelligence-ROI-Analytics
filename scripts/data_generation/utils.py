"""
Utility functions for data generation.
"""

import random
import numpy as np
from config import RANDOM_SEED

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


def print_summary(df, table_name):
    """Print a summary after generating a table."""
    print(f"\n{'=' * 50}")
    print(f"{table_name} Generated Successfully")
    print(f"Rows    : {len(df)}")
    print(f"Columns : {len(df.columns)}")
    print(f"{'=' * 50}")