grouped = df.groupby('Group').agg({'Score': 'mean', 'Age': 'median'})
print("\nСредний балл и медианный возраст по группам:")
print(grouped)

df['Passed'] = (df['Score'] >= 60).astype(int)
print("\nТаблица с Passed:")
print(df.head())
