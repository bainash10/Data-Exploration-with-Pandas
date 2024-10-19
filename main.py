import pandas as pd

df = pd.read_csv('train.csv')

# 1. How Big is the Data?
print("Data Shape (Rows, Columns):", df.shape)

# 2. How Does the Data Look Like? (View the first 5 rows)
print("\nFirst 5 Rows of the Data:")
print(df.head())

# 3. What is the Data Type of Columns?
print("\nData Types of Columns:")
print(df.dtypes)

# 4. Are There Any Missing Values?
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# 5. How Does the Data Look Mathematically? (Summary Statistics)
print("\nSummary Statistics of Numerical Columns:")
print(df.describe())

# 6. Are There Duplicate Values?
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

# 7. How is the Correlation Between Columns?
print("\nCorrelation Matrix:")
print(df.corr())


