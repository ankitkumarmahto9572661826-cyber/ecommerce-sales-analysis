
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "processed" / "cleaned_superstore.csv"
OUTPUT_DIR = BASE_DIR / "reports"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(DATA_FILE)

print("========== DATASET OVERVIEW ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nColumn names:")
print(df.columns.tolist())

# KPI calculations
print("\n========== KEY METRICS ==========")
print("Total Sales:", round(df["sales"].sum(), 2))
print("Total Profit:", round(df["profit"].sum(), 2))
print("Total Quantity:", df["quantity"].sum())
print("Average Discount:", round(df["discount"].mean(), 3))

# Category analysis
print("\n========== CATEGORY PERFORMANCE ==========")
category = df.groupby("category").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum"),
    Total_Quantity=("quantity", "sum")
).round(2)

print(category.sort_values("Total_Sales", ascending=False))
category.to_csv(OUTPUT_DIR / "category_analysis.csv")

# Regional analysis
print("\n========== REGIONAL PERFORMANCE ==========")
region = df.groupby("region").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum")
).round(2)

print(region.sort_values("Total_Sales", ascending=False))
region.to_csv(OUTPUT_DIR / "regional_analysis.csv")

# Correlation analysis
print("\n========== CORRELATION ==========")
print(df[["sales", "quantity", "discount", "profit"]].corr().round(3))

# Loss-making categories
print("\n========== LOSS-MAKING SUB-CATEGORIES ==========")
subcategory = df.groupby("sub-category").agg(
    Total_Sales=("sales", "sum"),
    Total_Profit=("profit", "sum")
).round(2)

print(subcategory[subcategory["Total_Profit"] < 0])

# Export summary
print("\nEDA completed. Summary CSV files saved in reports/.")