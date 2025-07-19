# pandas_basics.py
import pandas as pd

# 1. Create the DataFrame
data = {
    "Name": ["John", "Zaid", "Sam"],
    "Age": [32, 29, 27],
    "GPA": [3.9, 3.2, 3.7]
}
df = pd.DataFrame(data)

# 2. Basic Exploration
print("Full DataFrame:\n", df)
print("\nFirst row:\n", df.head(1))
print("\nLast row:\n", df.tail(1))
print("\nColumns:", df.columns.tolist())
print("Shape:", df.shape)
print("Data types:\n", df.dtypes)

# 3. Accessing Data
print("\nName column:\n", df["Name"])
print("\nName and GPA columns:\n", df[["Name", "GPA"]])
print("\nSecond row:\n", df.iloc[1])

# 4. Filtering
high_gpa = df[df["GPA"] > 3.5]
print("\nStudents with GPA > 3.5:\n", high_gpa)

# 5. Add Column
df["Graduated"] = [True, False, True]
print("\nWith Graduated column:\n", df)

# 6. Drop Column
df_dropped = df.drop("Age", axis=1)
print("\nWithout Age column:\n", df_dropped)

# 7. Sorting
sorted_df = df.sort_values(by="GPA", ascending=False)
print("\nSorted by GPA:\n", sorted_df)

# 8. Descriptive Stats
print("\nSummary Stats:\n", df.describe())
