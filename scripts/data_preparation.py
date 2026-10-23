
import pandas as pd
from pathlib import Path

# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Locate the original dataset
csv_file = DATA_DIR / "raw" / "SampleSuperstore.csv"
xlsx_file = DATA_DIR / "raw" / "SampleSuperstore.xlsx"

if csv_file.exists():
    df = pd.read_csv(csv_file)
elif xlsx_file.exists():
    df = pd.read_excel(xlsx_file)
else:
    raise FileNotFoundError(
        "Put SampleSuperstore.csv or "
        "SampleSuperstore.xlsx inside data/raw/"
    )

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Shape ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

print("\n--- Descriptive Statistics ---")
print(df.describe(include="all").T)



# --- Data Cleaning ---

# Remove exact duplicate records
clean_df = df.drop_duplicates().copy()

# Standardize column names
clean_df.columns = (
    clean_df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.lower()
)

# Check missing values after cleaning
print("\n--- Missing Values After Cleaning ---")
print(clean_df.isnull().sum())

# Verify duplicate rows
print("\n--- Duplicates After Cleaning ---")
print(clean_df.duplicated().sum())

# Create output folder if needed
from pathlib import Path

output_dir = Path("data") / "processed"
output_dir.mkdir(parents=True, exist_ok=True)

# Save cleaned dataset
output_file = output_dir / "cleaned_superstore.csv"
clean_df.to_csv(output_file, index=False)

print("\nOriginal rows:", len(df))
print("Cleaned rows:", len(clean_df))
print("Rows removed:", len(df) - len(clean_df))
print("Saved to:", output_file)