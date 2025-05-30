import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
plt.hist(df['Score'], bins=10, edgecolor='black')
plt.title('Распределение баллов студентов')
plt.xlabel('Score')
plt.ylabel('Количество студентов')
plt.grid(True)
plt.show()

group_means = df.groupby('Group')['Score'].mean()

plt.figure(figsize=(8, 4))
group_means.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Средний балл по группам')
plt.xlabel('Группа')
plt.ylabel('Средний балл')
plt.grid(axis='y')
plt.show()
