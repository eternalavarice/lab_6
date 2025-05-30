print("\nКоличество пропусков по столбцам:")
print(df.isnull().sum())

df['Score'].fillna(df['Score'].mean(), inplace=True)

df.dropna(subset=['Group'], inplace=True)

print("\nПропуски после обработки:")
print(df.isnull().sum())
