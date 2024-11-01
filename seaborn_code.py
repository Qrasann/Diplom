import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os


# Функция для загрузки данных
def load_data():
  # Путь к файлу data.csv в папке data
  data_path = os.path.join(os.path.dirname(__file__), 'data', 'data.csv')

  # Загрузка данных
  data = pd.read_csv(data_path)
  return data


# Функция для визуализации с помощью Seaborn
def seaborn_visualizations(data):
  # Гистограмма распределения рейтинга
  plt.figure(figsize=(10, 6))
  sns.histplot(data['averageRating'], kde=True, color='blue')
  plt.title('Гистограмма рейтингов с KDE')
  plt.show()

  # Коробчатая диаграмма по жанрам
  plt.figure(figsize=(14, 8))
  sns.boxplot(data=data, x='averageRating', y='genres', palette='Set2')
  plt.title('Распределение рейтинга по жанрам')
  plt.show()

  # Heatmap корелляции между рейтингом и количеством голосов
  plt.figure(figsize=(10, 8))
  corr_data = data[['averageRating', 'numVotes']].corr()
  sns.heatmap(corr_data, annot=True, cmap='coolwarm', center=0)
  plt.title('Корреляция рейтинга и количества голосов')
  plt.show()


# Основной блок кода для выполнения
if __name__ == "__main__":
  data = load_data()  # Загружаем данные
  seaborn_visualizations(data)  # Запускаем визуализацию
