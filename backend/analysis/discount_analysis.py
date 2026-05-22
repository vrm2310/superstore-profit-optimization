import pandas as pd

df = pd.read_csv("../data/superstore_cleaned.csv")

print("\nAVERAGE DISCOUNT:")
print(df["Discount"].mean())

print("\nDISCOUNT VS PROFIT:")
print(
    df.groupby("Discount")["Profit"]
    .mean()
    .sort_index()
)

print("\nHIGH DISCOUNT ORDERS:")
high_discount = df[df["Discount"] > 0.3]

print(high_discount[[
    "Category",
    "Sub-Category",
    "Sales",
    "Discount",
    "Profit"
]].head(20))

discount_summary = (
    df.groupby("Category")["Discount"]
    .sum()
    .reset_index()
)

discount_summary.to_csv(
    "../outputs/summaries/category_discount_summary.csv",
    index=False
)