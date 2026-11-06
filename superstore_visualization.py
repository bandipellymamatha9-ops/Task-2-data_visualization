"""
DATA VISUALIZATION & STORYTELLING
Elevate Labs - Data Analyst Internship | Task 2

How to run in Pydroid 3:
1. Install pandas and matplotlib from Pydroid 3's Pip menu.
2. Keep this Python file and superstore_sales.csv in the SAME folder.
3. Open this file in Pydroid 3 and press Run.
4. The script creates a "visualization_output" folder containing charts
   and a short business-insights report.

Dataset: Superstore-style sample sales data (included separately).
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ---------- 1. Load dataset ----------
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "superstore_sales.csv"
OUTPUT_DIR = BASE_DIR / "visualization_output"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "superstore_sales.csv was not found. Keep the CSV file in the same "
        "folder as this Python file."
    )

df = pd.read_csv(DATA_FILE)
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df = df.dropna(subset=["Order_Date", "Sales", "Profit"])

# Add month field for time-based analysis.
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

# ---------- 2. Calculate key business metrics ----------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
average_discount = df["Discount"].mean() * 100
profit_margin = (total_profit / total_sales * 100) if total_sales else 0

monthly_sales = df.groupby("Month")["Sales"].sum().sort_index()
category_summary = df.groupby("Category")[["Sales", "Profit"]].sum().sort_values(
    "Sales", ascending=False
)
region_summary = df.groupby("Region")[["Sales", "Profit"]].sum().sort_values(
    "Sales", ascending=False
)
discount_summary = df.groupby("Discount")["Profit"].mean().sort_index()

best_month = monthly_sales.idxmax()
best_category = category_summary["Sales"].idxmax()
best_region = region_summary["Sales"].idxmax()
lowest_profit_region = region_summary["Profit"].idxmin()

# ---------- 3. Create visualizations ----------
plt.rcParams["figure.figsize"] = (10, 5)
plt.rcParams["axes.titlesize"] = 13
plt.rcParams["axes.labelsize"] = 10

# Chart 1: Monthly sales trend
fig, ax = plt.subplots()
ax.plot(monthly_sales.index, monthly_sales.values, marker="o", linewidth=2)
ax.set_title("Monthly Sales Trend (2024-2025)")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.tick_params(axis="x", rotation=70)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "01_monthly_sales_trend.png", dpi=160)
plt.close(fig)

# Chart 2: Sales and profit by category
fig, ax = plt.subplots()
category_summary.plot(kind="bar", ax=ax)
ax.set_title("Sales and Profit by Product Category")
ax.set_xlabel("Category")
ax.set_ylabel("Amount")
ax.tick_params(axis="x", rotation=0)
ax.grid(axis="y", alpha=0.25)
ax.legend(["Sales", "Profit"])
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "02_category_performance.png", dpi=160)
plt.close(fig)

# Chart 3: Sales by region
fig, ax = plt.subplots()
region_summary["Sales"].sort_values().plot(kind="barh", ax=ax)
ax.set_title("Total Sales by Region")
ax.set_xlabel("Sales")
ax.set_ylabel("Region")
ax.grid(axis="x", alpha=0.25)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "03_regional_sales.png", dpi=160)
plt.close(fig)

# Chart 4: Discount vs profit
fig, ax = plt.subplots()
ax.scatter(df["Discount"] * 100, df["Profit"], alpha=0.45)
ax.set_title("Relationship Between Discount and Profit")
ax.set_xlabel("Discount (%)")
ax.set_ylabel("Profit")
ax.axhline(0, linewidth=1)
ax.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "04_discount_vs_profit.png", dpi=160)
plt.close(fig)

# ---------- 4. Create a KPI summary dashboard ----------
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("SUPERSTORE SALES - BUSINESS OVERVIEW", fontsize=16, fontweight="bold")

# KPI cards
kpis = [
    ("Total Sales", f"{total_sales:,.0f}"),
    ("Total Profit", f"{total_profit:,.0f}"),
    ("Number of Orders", f"{total_orders:,}"),
    ("Average Discount", f"{average_discount:.1f}%")
]
for ax, (label, value) in zip(axes.flat, kpis):
    ax.axis("off")
    ax.text(0.5, 0.62, value, ha="center", va="center",
            fontsize=22, fontweight="bold")
    ax.text(0.5, 0.34, label, ha="center", va="center", fontsize=12)

fig.tight_layout(rect=[0, 0, 1, 0.94])
fig.savefig(OUTPUT_DIR / "05_kpi_dashboard.png", dpi=160)
plt.close(fig)

# ---------- 5. Write storytelling insights ----------
report = f"""
DATA VISUALIZATION & STORYTELLING - BUSINESS INSIGHTS
=====================================================

DATASET OVERVIEW
- Records analysed: {total_orders:,}
- Period: {df['Order_Date'].min().date()} to {df['Order_Date'].max().date()}
- Total sales: {total_sales:,.2f}
- Total profit: {total_profit:,.2f}
- Overall profit margin: {profit_margin:.2f}%
- Average discount: {average_discount:.2f}%

KEY FINDINGS
1. The strongest sales month was {best_month}.
2. {best_category} generated the highest total sales among product categories.
3. {best_region} recorded the highest total sales among regions.
4. {lowest_profit_region} had the lowest total profit and may need closer review.
5. The discount-versus-profit scatter plot helps identify whether larger discounts
   are associated with weaker profit.

BUSINESS RECOMMENDATIONS
- Study the best-performing month and plan inventory and promotions ahead of it.
- Protect profit margins while promoting high-sales product categories.
- Review discount rules, especially where discounts are high but profit is low.
- Investigate the lowest-profit region before increasing its sales promotions.

STORY SUMMARY
Sales performance changes over time and differs across product categories and
regions. The dashboard highlights where sales are strongest, while the discount
analysis reminds the business that higher sales do not always mean higher profit.
Managers should balance revenue growth with profitability.
"""

(OUTPUT_DIR / "business_insights.txt").write_text(report.strip(), encoding="utf-8")

print("Analysis completed successfully!")
print("Total Sales: {:.2f}".format(total_sales))
print("Total Profit: {:.2f}".format(total_profit))
print("Charts and insights saved in:", OUTPUT_DIR)
print("Open 05_kpi_dashboard.png and the four chart images to review your results.")
