import plotly.express as px
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

def plotly_visualizations(data):
    # Scatter-плот средний рейтинг по годам
    fig = px.scatter(data, x='releaseYear', y='averageRating',
                     size='numVotes', color='genres',
                     hover_name='title', title='Распределение рейтингов по годам')
    fig.update_layout(xaxis_title='Год выпуска', yaxis_title='Средний рейтинг')
    fig.show()

    # Bubble Chart количества голосов и рейтинга
    fig = px.scatter(data, x='numVotes', y='averageRating',
                     size='numVotes', color='averageRating', hover_name='title',
                     title='Рейтинг vs. Количество голосов',
                     log_x=True)
    fig.update_layout(xaxis_title='Количество голосов (логарифм)', yaxis_title='Средний рейтинг')
    fig.show()

# Основной блок кода для выполнения
if __name__ == "__main__":
  data = load_data()  # Загружаем данные
  plotly_visualizations(data) # Запускаем визуализацию

