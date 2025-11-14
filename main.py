import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ast

url = "data/movies_metadata.csv"

# df = DataFrame
df = pd.read_csv(url)

# print(df.head())
# df.info()
# print(df.describe())
# print(df.isnull().sum())

# print(df[["belongs_to_collection", "homepage", "tagline"]])

# старий варіант
# df["tagline"].fillna("without tagline", inplace=True)

# новий варіант
# df.fillna({"tagline": "without tagline"}, inplace=True)

df["tagline"] = df["tagline"].fillna("without tagline")
# print(df.tagline)

df.homepage = df.homepage.fillna("no homepage")
# print(df.homepage)

df.fillna({"belongs_to_collection": "{}"}, inplace=True)
# print(df.belongs_to_collection)

# df.info()

df.dropna(inplace=True)
# print(df.isnull().sum())
df.info()

#-----------------------------------------------

def extract_genres(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        return [genre["name"] for genre in genres]
    except ValueError:
        return []
# print(extract_genres(df["genres"].value_counts()))
print(df["genres"].apply(extract_genres))
df["genres"] = df["genres"].apply(extract_genres)

all_genres = df['genres'].explode()
genres_counts = all_genres.value_counts()
# print(genres_counts)

# print(genres_counts.index)
# print(genres_counts.values)

plt.figure(figsize=(10,6))

sns.barplot(x=genres_counts.index, y=genres_counts.values)

plt.title("Count film for genres")
plt.xlabel("genres")
plt.ylabel("counts")

plt.xticks(rotation=45)

plt.show()