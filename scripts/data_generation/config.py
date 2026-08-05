"""
Project Configuration
Marketing Intelligence ROI Analytics
"""

from pathlib import Path

# ----------------------------
# Project Paths
# ----------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
GENERATED_DATA_DIR = DATA_DIR / "generated"

# Create folder automatically if it doesn't exist
GENERATED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------
# Date Range
# ----------------------------

START_DATE = "2025-01-01"
END_DATE = "2025-12-31"

# ----------------------------
# Random Seed
# ----------------------------

RANDOM_SEED = 42

# ----------------------------
# Planned Dataset Sizes
# ----------------------------

ROWS = {
    "dim_date": 365,
    "dim_channel": 6,
    "dim_geography": 4,
    "dim_device": 6,
    "dim_product": 1000,
    "dim_campaign": 20,
    "dim_customer": 10000,
    "fact_campaign_performance": 25000,
    "fact_sales": 100000,
    "fact_customer_acquisition": 10000,
}