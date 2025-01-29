import zipfile
import dask.dataframe as dd

with zipfile.ZipFile('recipes_full.zip', 'r') as zip_ref:
    zip_ref.extractall()

df = dd.read_csv('recipes_full/*.csv', dtype={'minutes': 'float64', 'n_steps': 'float64'})

print(f"Npartitions: {df.npartitions}")
print(f"Типы столбцов:\n{df.dtypes}")

print(df.head(5))

print(df.tail(5))

# Количество строк в каждом блоке
partition_sizes = df.map_partitions(len).compute()
print(partition_sizes)

# Максимум в столбце n_steps и граф вычислений
max_n_steps = df['n_steps'].max()
print(f"Максимум n_steps: {max_n_steps.compute()}")
print(f"{str(max_n_steps.dask)}")

# Преобразуем столбец с датами в формат datetime
df['submitted'] = dd.to_datetime(df['submitted'])

# Группировка по месяцам и подсчет количества отзывов
reviews_by_month = df.groupby(df['submitted'].dt.to_period('M')).size().compute()
print(reviews_by_month)

# Пользователь с наибольшим количеством рецептов
most_active_user = df['contributor_id'].value_counts().idxmax().compute()
print(f"Пользователь, отправивший больше всего рецептов: {most_active_user}")

# Самый первый и самый последний рецепт
first_recipe = df.loc[df['submitted'].idxmin()]
last_recipe = df.loc[df['submitted'].idxmax()]
print("Первый рецепт:\n", first_recipe.head())
print("Последний рецепт:\n", last_recipe.head())

df.to_sql('recipes', 'sqlite:///recipes.db', if_exists='replace', index=False)

# Вычисление медианы времени приготовления и среднего количества шагов
median_minutes = df['minutes'].median_approximate().compute()
mean_n_steps = df['n_steps'].mean().compute()

# Фильтрация рецептов
filtered_df = df[(df['minutes'] < median_minutes) & (df['n_steps'] < mean_n_steps)]

# Сохранение в CSV
filtered_df.to_csv('filtered_recipes.csv', index=False)