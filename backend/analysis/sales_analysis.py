import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/superstore_cleaned.csv")

print("\nTOTAL SALES:")
print(df["Sales"].sum())

print("\nAVERAGE SALES:")
print(df["Sales"].mean())

print("\nTOP 10 STATES BY SALES:")
print(
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 CATEGORIES BY SALES:")
print(
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTOP 10 SUB-CATEGORIES BY SALES:")
print(
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

sales_summary = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

sales_summary.to_csv(
    "../outputs/summaries/category_sales_summary.csv",
    index=False
)