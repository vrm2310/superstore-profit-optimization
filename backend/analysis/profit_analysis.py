import pandas as pd

df = pd.read_csv("../data/superstore_cleaned.csv")

print("\nTOTAL PROFIT:")
print(df["Profit"].sum())

print("\nAVERAGE PROFIT:")
print(df["Profit"].mean())

print("\nMOST PROFITABLE STATES:")
print(
    df.groupby("State")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nLEAST PROFITABLE STATES:")
print(
    df.groupby("State")["Profit"]
    .sum()
    .sort_values()
    .head(10)
)

print("\nMOST PROFITABLE SUB-CATEGORIES:")
print(
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nLOSS-MAKING SUB-CATEGORIES:")
print(
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values()
    .head(10)
)

summary = (
    df.groupby("Category")["Profit"]
    .sum()
    .reset_index()
)

summary.to_csv(
    "../outputs/summaries/category_profit_summary.csv",
    index=False
)