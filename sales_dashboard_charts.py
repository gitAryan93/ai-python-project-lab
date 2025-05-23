import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Product': ['Shoes', 'Bag', 'Shirt', 'Shoes', 'Watch', 'Shirt', 'Bag', 'Watch', 'Shoes', 'Bag'],
    'Category': ['Clothing', 'Accessories', 'Clothing', 'Accessories', 'Clothing', 'Accessories', 'Clothing', 'Accessories', 'Clothing', 'Accessories'],
    'Units_Sold': [10, 5, 8, 7, 3, 9, 4, 6, 12, 5],
    'Price_Per_Unit': [50, 70, 25, 50, 120, 25, 70, 120, 50, 70],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South']
}

df = pd.DataFrame(data)
df['Total_Revenue'] = df['Units_Sold'] * df['Price_Per_Unit']

# Bar Chart: Revenue by Category
category_revenue = df.groupby("Category")["Total_Revenue"].sum()
category_revenue.plot(kind="bar", color="skyblue")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.show()

# Pie Chart: Units Sold by Region
region_units = df.groupby('Region')['Units_Sold'].sum()
region_units.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Unit Sold by Region')
plt.ylabel(' ')
plt.tight_layout()
plt.show()

# Histogram: Price Per Unit
plt.hist(df['Price_Per_Unit'], bins=5, color='green', edgecolor='black')
plt.title('Price Per Unit Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
