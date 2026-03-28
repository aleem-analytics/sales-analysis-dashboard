import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales.csv")

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Create Month column
df["Month"] = df["Date"].dt.month

# Basic summary
print(df.head())
print("Total Revenue:", df["Revenue"].sum())
print("Average Revenue:", df["Revenue"].mean())

# Grouped analysis
product_sales = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
region_sales = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
monthly_sales = df.groupby("Month")["Revenue"].sum()

# Print clean output
print("\n--- Revenue by Product ---")
print(product_sales.to_string())

print("\n--- Revenue by Region ---")
print(region_sales.to_string())

print("\n--- Monthly Revenue ---")
print(monthly_sales.to_string())

# Save charts

product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("product_chart.png")
plt.close()

region_sales.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("region_chart.png")
plt.close()

monthly_sales.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_chart.png")
plt.close()