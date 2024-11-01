# Импорт библиотек
import matplotlib.pyplot as plt
import mplcursors
import os
import pandas as pd


# Функция для загрузки данных
def load_data():
  # Путь к файлу data.csv в папке data
  data_path = os.path.join(os.path.dirname(__file__), 'data', 'data.csv')

  # Загрузка данных
  data = pd.read_csv(data_path)
  return data


# Функция для визуализации с помощью Matplotlib
def matplotlib_visualizations(data):
  # Распределение рейтинга
  plt.figure(figsize=(12, 6))
  plt.hist(data['averageRating'], bins=20, color='skyblue', edgecolor='black')
  plt.title('Распределение среднего рейтинга фильмов')
  plt.xlabel('Средний рейтинг')
  plt.ylabel('Количество фильмов')
  plt.grid(True)
  plt.show()

  # Рейтинг по годам
  plt.figure(figsize=(12, 6))
  avg_rating_per_year = data.groupby('releaseYear')['averageRating'].mean()
  plt.plot(avg_rating_per_year.index, avg_rating_per_year, marker='o', color='green')
  plt.title('Изменение среднего рейтинга по годам')
  plt.xlabel('Год выпуска')
  plt.ylabel('Средний рейтинг')
  plt.grid(True)
  plt.show()

  # Количество голосов и рейтинг
  plt.figure(figsize=(12, 6))
  plt.scatter(data['numVotes'], data['averageRating'], alpha=0.5, color='purple')
  plt.title('Распределение количества голосов и среднего рейтинга')
  plt.xlabel('Количество голосов')
  plt.ylabel('Средний рейтинг')
  plt.grid(True)
  plt.xscale('log')
  plt.show()


# Основной блок кода для выполнения
if __name__ == "__main__":
  data = load_data()  # Загружаем данные
  matplotlib_visualizations(data)  # Запускаем визуализацию
