import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/superstore_cleaned.csv")

# Style
sns.set_style("whitegrid")

# ==============================
# 1. Sales by Category
# ==============================

sales_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

sns.barplot(
    x=sales_category.index,
    y=sales_category.values
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig(
    "../outputs/charts/sales_by_category.png"
)

plt.close()

# ==============================
# 2. Profit by Category
# ==============================

profit_category = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

sns.barplot(
    x=profit_category.index,
    y=profit_category.values
)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.tight_layout()

plt.savefig(
    "../outputs/charts/profit_by_category.png"
)

plt.close()

# ==============================
# 3. Discount vs Profit
# ==============================

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit"
)

plt.title("Discount vs Profit")

plt.tight_layout()

plt.savefig(
    "../outputs/charts/discount_vs_profit.png"
)

plt.close()

print("Charts generated successfully.")