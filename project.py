import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

print(df.head())

# -------------------
# Data Cleaning
# -------------------
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# -------------------
# Basic Analysis
# -------------------
print(df.describe())

# Total sales by category
if 'Category' in df.columns:
    category_sales = df.groupby('Category')['Sales'].sum()

    category_sales.plot(kind='bar', color='skyblue')
    plt.title("Sales by Category")
    plt.savefig("category_sales.png")
    plt.show()

# Monthly sales (if date exists)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

    monthly_sales = df.groupby(df['Date'].dt.month)['Sales'].sum()

    monthly_sales.plot(kind='line', marker='o')
    plt.title("Monthly Sales Trend")
    plt.savefig("monthly_sales.png")
    plt.show()

# Correlation heatmap
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()

print("Project Completed Successfully!")