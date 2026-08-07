"""
Generate the Dim_Product table.
"""

import random
import pandas as pd

from config import (
    BASE_DIR,
    GENERATED_DATA_DIR,
    ROWS,
    PRODUCT_COUNT,
    MIN_RATING,
    MAX_RATING,
)

from validate import (
    validate_row_count,
    validate_duplicate_primary_key,
    validate_null_values,
)

from utils import (
    save_dataframe,
    print_success,
    generate_sku,
)

# ---------------------------------------
# Product Name Templates
# ---------------------------------------

PRODUCT_SUFFIXES = {
    "Electronics": [
        "Smartphone",
        "Laptop",
        "Wireless Earbuds",
        "Smartwatch",
        "Bluetooth Speaker",
        "Tablet",
        "Gaming Mouse",
        "Monitor",
    ],
    "Fashion": [
        "Running Shoes",
        "Casual T-Shirt",
        "Jeans",
        "Hoodie",
        "Sports Jacket",
        "Sneakers",
    ],
    "Beauty": [
        "Face Serum",
        "Lipstick",
        "Moisturizer",
        "Face Wash",
        "Shampoo",
        "Sunscreen",
    ],
    "Home & Kitchen": [
        "Pressure Cooker",
        "Mixer Grinder",
        "Air Fryer",
        "Water Bottle",
        "Cookware Set",
        "Storage Box",
    ],
    "Sports": [
        "Cricket Bat",
        "Football",
        "Badminton Racket",
        "Yoga Mat",
        "Dumbbell Set",
        "Sports Bag",
    ],
}

# ---------------------------------------
# Load Reference Data
# ---------------------------------------

brands_df = pd.read_csv(
    BASE_DIR / "data" / "reference" / "brands.csv"
)

subcategories_df = pd.read_csv(
    BASE_DIR / "data" / "reference" / "subcategories.csv"
)

price_ranges_df = pd.read_csv(
    BASE_DIR / "data" / "reference" / "price_ranges.csv"
)

# ---------------------------------------
# Create Lookup Dictionaries
# ---------------------------------------

subcategory_lookup = (
    subcategories_df.groupby("Category")["Sub_Category"]
    .apply(list)
    .to_dict()
)

price_lookup = {}

for _, row in price_ranges_df.iterrows():
    price_lookup[row["Category"]] = (
        row["Min_Price"],
        row["Max_Price"],
    )

# ---------------------------------------
# Generate One Product
# ---------------------------------------

def generate_product(product_id):
    """
    Generate one realistic product.
    """

    brand_row = brands_df.sample(1).iloc[0]

    brand = brand_row["Brand_Name"]
    category = brand_row["Category"]

    subcategory = random.choice(
        subcategory_lookup[category]
    )

    suffix = random.choice(
        PRODUCT_SUFFIXES[category]
    )

    product_name = f"{brand} {suffix}"

    sku = generate_sku(category, product_id)

    min_price, max_price = price_lookup[category]

    price = random.randint(min_price, max_price)

    cost = round(
        price * random.uniform(0.55, 0.80),
        2,
    )

    profit_margin = round(
        ((price - cost) / price) * 100,
        2,
    )

    rating = round(
        random.uniform(
            MIN_RATING,
            MAX_RATING,
        ),
        1,
    )

    launch_year = random.randint(2019, 2025)

    is_active = random.random() < 0.95

    return {
        "Product_ID": product_id,
        "SKU": sku,
        "Product_Name": product_name,
        "Brand": brand,
        "Category": category,
        "Sub_Category": subcategory,
        "Price": price,
        "Cost": cost,
        "Profit_Margin": profit_margin,
        "Rating": rating,
        "Launch_Year": launch_year,
        "Is_Active": is_active,
    }

# ---------------------------------------
# Generate Product Dimension
# ---------------------------------------

def generate_dim_product():
    """
    Generate the Product Dimension table.
    """

    products = []

    for product_id in range(1, PRODUCT_COUNT + 1):
        products.append(
            generate_product(product_id)
        )

    df = pd.DataFrame(products)

    validate_row_count(
        df,
        ROWS["dim_product"],
    )

    validate_duplicate_primary_key(
        df,
        "Product_ID",
    )

    validate_null_values(df)

    output_file = (
        GENERATED_DATA_DIR /
        "dim_product.csv"
    )

    save_dataframe(
        df,
        output_file,
    )

    print_success(
        "Dim_Product generated successfully."
    )

    return df