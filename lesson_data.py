import pandas as pd

months = ['jan', 'feb', 'mar', 'apr']
sales = {
    'revenue': [100, 200, 300, 400],
    'items_sold': [23, 43, 54, 65],
    'new_clients': [10, 20, 30, 40]
}

df = pd.DataFrame(data=sales, index=months)
print(df)

# vector = [1, 2, 3]
# print(vector * 2)

# series = pd.Series([1, 2, 3])
# print(series * 2)

# series_str = pd.Series(['a', 'b', 'c'])
# print(series_str[0])

# months = ['jan', 'feb', 'mar', 'apr']
# sales = [100, 200, 300, 400]
# data = pd.Series(data=sales, index=months)
# print(data)
# print(data["feb"])

# print(df.head(2))
# print(df.tail(1))

# print(df['revenue'])

# print(df.info())
# print(df.shape) # розмір таблиці (рядки, стовпчики)
# print(df.columns)
# print(df.describe())
# print(df.dtypes)

df.revenue = ['100', '200', '300', '400']
# print(df)
# print(df.revenue.dtypes)
df.revenue = pd.to_numeric(df.revenue, errors='coerce')
# print(df.describe())
# print(df.revenue.dtypes)

# print(df.loc[['feb', 'apr']])

movies_df = pd.read_csv('data/movies_metadata.csv')
# print(movies_df.to_string())

print(pd.options.display.max_rows)