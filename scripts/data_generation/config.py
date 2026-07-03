"""
Project Configuration
ShopSphere Marketing Intelligence
"""

# Random seed for reproducibility
RANDOM_SEED = 42

# Output folder
OUTPUT_FOLDER = "../../data/generated"

# Dataset sizes
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

# Date range
START_DATE = "2025-01-01"
END_DATE = "2025-12-31"