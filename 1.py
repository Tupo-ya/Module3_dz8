import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(open('Customers.csv', 'rb'), sep=';')

df = pd.get_dummies(df, columns=['Gender', 'Profession'])

# ? Карта корреляции
print('Карта корреляции:')
correlation_matrix = df.corr()
print(correlation_matrix)

# ? Тепловая карта
print('\n\nПоказана Тепловая карта')
plt.figure(figsize=(16, 6))
heatmap = sns.heatmap(correlation_matrix, vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12);
plt.show()

# ? Тепловая треугольная карта
print('\nПоказана Треугольная тепловая карта')
plt.figure(figsize=(16, 6))
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
heatmap = sns.heatmap(correlation_matrix, mask=mask, vmin=-1, vmax=1, annot=True, annot_kws={'size': 5}, cmap='BrBG')
heatmap.set_title('Triangle Correlation Heatmap', fontdict={'fontsize':18}, pad=16);
plt.show()

# ? Точечная диаграмма
print('\nПоказана Точечная диаграмма')
sns.scatterplot(data=df, x="Family Size", y="Annual Income ($)")
plt.show()
