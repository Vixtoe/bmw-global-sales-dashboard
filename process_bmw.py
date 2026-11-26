import pandas as pd

# Load original dataset
df = pd.read_csv("data/BMW sales data (2010-2024).csv")

# Create the revenue metric
df["Total_Revenue"] = df["Price_USD"] * df["Sales_Volume"]

# Rename columns for consistency
df.rename(
    columns={
        "Model": "Vehicle_Model",
    },
    inplace=True,
)

# Save the processed file
output_file = "data/bmw_digital_sales_2010_2024.csv"
df.to_csv(output_file, index=False)
print(f"File saved successfully as {output_file} with {len(df)} rows.")