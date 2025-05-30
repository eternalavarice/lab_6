high_score_students = df[df['Score'] > 80]

sorted_students = high_score_students.sort_values(by='Score', ascending=False)
print("\nСтуденты с баллом > 80 (по убыванию):")
print(sorted_students)

oldest = df[df['Age'] == df['Age'].max()]
youngest = df[df['Age'] == df['Age'].min()]
print("\nСамый старший студент:")
print(oldest)
print("\nСамый младший студент:")
print(youngest)
