import pandas as pd

df = pd.read_csv("../data/superstore_cleaned.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Month-Year"] = (
    df["Order Date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_sales = (
    df.groupby("Month-Year")["Sales"]
    .sum()
    .reset_index()
)

monthly_sales.to_csv(
    "../outputs/summaries/monthly_sales_summary.csv",
    index=False
)

print(monthly_sales.head())