
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "processed" / "cleaned_superstore.csv"
OUTPUT_DIR = BASE_DIR / "reports" / "charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned data
df = pd.read_csv(DATA_FILE)

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

sns.set_theme(style="whitegrid")

# 1. Category-wise sales
category_sales = (
    df.groupby("category", as_index=False)["sales"]
    .sum()
    .sort_values("sales", ascending=False)
)

plt.figure(figsize=(10, 6))
sns.barplot(data=category_sales, x="category", y="sales")
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "category_sales.png", dpi=300)
plt.close()

# 2. Regional sales
region_sales = (
    df.groupby("region", as_index=False)["sales"]
    .sum()
    .sort_values("sales", ascending=False)
)

plt.figure(figsize=(9, 5))
sns.barplot(data=region_sales, x="region", y="sales")
plt.title("Regional Sales Performance")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "regional_sales.png", dpi=300)
plt.close()

# 3. Profit by category
category_profit = (
    df.groupby("category", as_index=False)["profit"]
    .sum()
)

plt.figure(figsize=(10, 6))
sns.barplot(data=category_profit, x="category", y="profit")
plt.axhline(0, linewidth=1)
plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "category_profit.png", dpi=300)
plt.close()

# 4. Sales vs discount
plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=df,
    x="discount",
    y="profit",
    hue="category",
    alpha=0.6
)
plt.axhline(0, linewidth=1)
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "discount_vs_profit.png", dpi=300)
plt.close()

print("Task 5 visualization completed!")
print(f"Charts saved to: {OUTPUT_DIR}")
print(f"Total charts created: 4")