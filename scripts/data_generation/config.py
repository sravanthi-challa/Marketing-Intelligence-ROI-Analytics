"""
Project Configuration
ShopSphere Marketing Intelligence
"""

from pathlib import Path

# -----------------------------
# Base Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
GENERATED_DATA_DIR = DATA_DIR / "generated"

GENERATED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Random Seed
# -----------------------------

RANDOM_SEED = 42

# -----------------------------
# Date Range
# -----------------------------

START_DATE = "2025-01-01"
END_DATE = "2025-12-31"

# -----------------------------
# Dataset Sizes
# -----------------------------

ROWS = {
    "dim_date": 365,
    "dim_campaign": 20,
    "dim_channel": 6,
    "dim_customer": 10000,
    "dim_product": 1000,
    "dim_geography": 30,
    "dim_device": 6,
    "fact_campaign_performance": 25000,
    "fact_sales": 100000,
    "fact_customer_acquisition": 10000,
}