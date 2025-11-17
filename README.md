# python-for-data
Python for data


📊 Аналіз датасету фільмів із movies_metadata.csv

Ця програма виконує базовий аналіз даних із файлу movies_metadata.csv, очищення даних, обробку жанрів та візуалізацію найпопулярніших жанрів у вигляді барплоту.

📥 1. Завантаження бібліотек та даних

Використовуються основні бібліотеки Python для аналізу та візуалізації даних:

pandas — робота з таблицями

numpy — додаткові операції з масивами

matplotlib і seaborn — графіки

ast — конвертація рядків у Python-структури (для жанрів)

Дані завантажуються з файлу:

df = pd.read_csv("data/movies_metadata.csv")

RangeIndex: 45466 entries, 0 to 45465
Data columns (total 24 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   adult                  45466 non-null  object 
 1   belongs_to_collection  45466 non-null  object 
 2   budget                 45466 non-null  object 
 3   genres                 45466 non-null  object 
 4   homepage               45466 non-null  object 
 5   id                     45466 non-null  object 
 6   imdb_id                45449 non-null  object 
 7   original_language      45455 non-null  object 
 8   original_title         45466 non-null  object 
 9   overview               44512 non-null  object 
 10  popularity             45461 non-null  object 
 11  poster_path            45080 non-null  object 
 12  production_companies   45463 non-null  object 
 13  production_countries   45463 non-null  object 
 14  release_date           45379 non-null  object 
 15  revenue                45460 non-null  float64
 16  runtime                45203 non-null  float64
 17  spoken_languages       45460 non-null  object 
 18  status                 45379 non-null  object 
 19  tagline                45466 non-null  object 
 20  title                  45460 non-null  object 
 21  video                  45460 non-null  object 
 22  vote_average           45460 non-null  float64
 23  vote_count             45460 non-null  float64
dtypes: float64(4), object(20)
memory usage: 8.3+ MB
🧹 2. Первинне очищення даних
Заповнення пропущених значень

tagline → "without tagline"

homepage → "no homepage"

belongs_to_collection → "{}" (порожній словник у рядку)

df["tagline"] = df["tagline"].fillna("without tagline")
df.homepage = df.homepage.fillna("no homepage")
df.fillna({"belongs_to_collection": "{}"}, inplace=True)

Видалення рядків із пропущеними значеннями
df.dropna(inplace=True)

🎬 3. Обробка жанрів

Поле genres містить список жанрів у вигляді рядка Python-словників.
Для конвертації використовується ast.literal_eval().

Функція для вилучення назв жанрів:
def extract_genres(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        return [genre["name"] for genre in genres]
    except ValueError:
        return []

Застосування функції до всього стовпця:
df["genres"] = df["genres"].apply(extract_genres)

Підрахунок усіх жанрів:
all_genres = df['genres'].explode()
genres_counts = all_genres.value_counts()

📈 4. Візуалізація популярності жанрів

Створюється барплот із кількістю фільмів у кожному жанрі:

plt.figure(figsize=(10,6))
sns.barplot(x=genres_counts.index, y=genres_counts.values)
plt.title("Count film for genres")
plt.xlabel("genres")
plt.ylabel("counts")
plt.xticks(rotation=45)
plt.show()

✔️ Результат

Програма:

очищає та структурує дані;

дістає жанри з вкладених структур;

рахує популярність жанрів;

будує наочну діаграму.

Це базовий, але повноцінний pipeline аналізу даних для набору інформації про фільми.