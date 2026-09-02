import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw_retail_sales.csv")
print("Original shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates().copy()
df["Date"] = pd.to_datetime(df["Date"])
for col in ["Marketing_Spend", "Avg_Product_Price"]:
    df[col] = df[col].fillna(df[col].median())

print("\nCleaned shape:", df.shape)
print("\nDescriptive statistics:\n", df.describe())

print("\nSales by Product:\n", df.groupby("Product")["Sales"].sum().sort_values(ascending=False))
print("\nSales by Region:\n", df.groupby("Region")["Sales"].sum().sort_values(ascending=False))
print("\nCorrelation:\n", df[["Customers","Marketing_Spend","Discount_Percent","Avg_Product_Price","Sales"]].corr())

print("\nEDA completed successfully.")
