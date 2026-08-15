"""
Main entry point for the data generation pipeline.
"""

from config import GENERATED_DATA_DIR
from utils import print_banner, print_success

from generate_date import generate_dim_date
from generate_channel import generate_dim_channel
from generate_geography import generate_dim_geography
from generate_device import generate_dim_device
from generate_product import generate_dim_product

from generate_campaign import generate_dim_campaign
from generate_customer import generate_dim_customer
from generate_sales import generate_fact_sales
def main():
    print_banner("Marketing Intelligence ROI Analytics")

    print_success("Pipeline initialized.")

    print(f"\nOutput Folder:\n{GENERATED_DATA_DIR}")

    print("\nGenerating Dimension Tables...\n")

    date_df = generate_dim_date()
    channel_df = generate_dim_channel()
    geography_df = generate_dim_geography()
    device_df = generate_dim_device()
    product_df = generate_dim_product()

    campaign_df = generate_dim_campaign()
    customer_df = generate_dim_customer()
    sales_df = generate_fact_sales()

    print(f"\nDim_Date Rows     : {len(date_df)}")
    print(f"Dim_Channel Rows  : {len(channel_df)}")
    print(f"Dim_Geography Rows : {len(geography_df)}")
    print(f"Dim_Device Rows     : {len(device_df)}")
    print(f"Dim_Product Rows    : {len(product_df)}")

    print(f"Dim_Campaign Rows : {len(campaign_df)}")
    print(f"Dim_Customer Rows : {len(customer_df)}")
    print(f"Fact_Sales Rows : {len(sales_df)}")

    print_success("Pipeline completed successfully.")


if __name__ == "__main__":
    main()