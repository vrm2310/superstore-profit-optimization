import pandas as pd

# Load dataset
df = pd.read_csv("../data/superstore_raw.csv", encoding="latin1")

# Basic dataset info
print("\nFIRST 5 ROWS:")
print(df.head())

print("\nDATASET INFO:")
print(df.info())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert order date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create profit margin column
df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100

# Save cleaned dataset
df.to_csv("../data/superstore_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")