import pandas as pd

# Create Sample Sales Data
data = {
    'Product': ['Shoes', 'Bag', 'Shirt', 'Shoes', 'Watch', 'Shirt', 'Bag', 'Watch', 'Shoes', 'Bag'],
    'Category': ['Clothing', 'Accessories', 'Clothing', 'Clothing', 'Accessories', 'Clothing', 'Accessories', 'Accessories', 'Clothing', 'Accessories'],
    'Units_Sold': [10, 5, 8, 7, 3, 9, 4, 6, 12, 5],
    'Price_Per_Unit': [50, 70, 25, 50, 120, 25, 70, 120, 50, 70],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South']
}

df = pd.DataFrame(data)

# Step Add Calculated Column: Total Revenue per sale
df['Total_Revenue'] = df['Units_Sold'] * df['Price_Per_Unit']

# Step Basic Analysis
print("===== Sales Dashboard Summary =====")
print("Total Units Sold:", df['Units_Sold'].sum())
print("Total Revenue: $", df['Total_Revenue'].sum())

# Step Top Performing Product
product_sales = df.groupby('Product')['Units_Sold'].sum()
top_product = product_sales.idxmax()
print("Top Selling Product:", top_product)

# Step Revenue by Category
category_revenue = df.groupby('Category')['Total_Revenue'].sum()
print("\nRevenue by Category:\n", category_revenue)

# Step Sales by Region
region_units = df.groupby('Region')['Units_Sold'].sum()
print("\nUnits Sold by Region:\n", region_units)

# Optional: Preview Data
print("\nRaw Data Preview:\n", df)
