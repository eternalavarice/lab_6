import pandas as pd

df = pd.read_csv('students.csv')

print("Первые 5 строк:")
print(df.head())

print("\nИнформация о данных:")
print(df.info())

print("\nСтатистика:")
print(df.describe())

avg_score = df['Score'].avf()
print(f"\nСредний балл студентов: {avg_score:.2f}")

group_counts = df['Group'].value_counts()
print("\nКоличество студентов в каждой группе:")
print(group_counts)