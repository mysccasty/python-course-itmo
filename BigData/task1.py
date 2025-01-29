import zipfile
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

with zipfile.ZipFile('recipes_full.zip', 'r') as zip_ref:
    zip_ref.extractall()

df = pd.read_csv('recipes_full/recipes_full_0.csv')

max_steps = df['n_steps'].max()
print(f"Максимальное количество шагов: {max_steps}")

df['submitted'] = pd.to_datetime(df['submitted'])
monthly_reviews = df.groupby(df['submitted'].dt.to_period('M')).size()
print("Количество отзывов по месяцам:\n", monthly_reviews)

most_active_user = df['contributor_id'].value_counts().idxmax()
print(f"Пользователь, отправивший больше всего рецептов: {most_active_user}")

first_recipe = df.loc[df['submitted'].idxmin()]
last_recipe = df.loc[df['submitted'].idxmax()]
print("Самый первый рецепт:")
print(first_recipe)
print("Самый последний рецепт:")
print(last_recipe)

median_ingredients = np.median(df['n_ingredients'])
median_minutes = np.median(df['minutes'])
print(f"Медиана количества ингредиентов: {median_ingredients}")
print(f"Медиана времени приготовления: {median_minutes}")

simplest_recipe = df.sort_values(by=['n_ingredients', 'minutes', 'n_steps']).iloc[0]
print("Самый простой рецепт:")
print(simplest_recipe)

engine = create_engine('sqlite:///recipes_full.db')
df.to_sql('recipes_full', engine, if_exists='replace', index=False)

filtered_df = df[(df['minutes'] < median_minutes) & (df['n_steps'] < df['n_steps'].mean())]
filtered_df.to_csv('filtered_recipes.csv', index=False)