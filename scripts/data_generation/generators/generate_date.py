"""
Generate Dim_Date table.
"""

import pandas as pd
from config import START_DATE, END_DATE, OUTPUT_FOLDER

def generate_dim_date():
    dates = pd.date_range(start=START_DATE, end=END_DATE)

    df = pd.DataFrame({
        "Date_ID": dates.strftime("%Y%m%d").astype(int),
        "Full_Date": dates,
        "Day": dates.day,
        "Month": dates.month,
        "Month_Name": dates.strftime("%B"),
        "Quarter": dates.quarter,
        "Year": dates.year,
        "Weekday": dates.strftime("%A"),
        "Is_Weekend": dates.weekday >= 5
    })

    output_path = f"{OUTPUT_FOLDER}/dim_date.csv"
    df.to_csv(output_path, index=False)

    print(f"Generated {len(df)} records.")
    print(f"Saved to: {output_path}")

    return df


if __name__ == "__main__":
    generate_dim_date()