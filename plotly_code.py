# Импорт библиотек
import plotly.express as px
import pandas as pd
import os

# Функция для загрузки данных
def load_data():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'data.csv')
    data = pd.read_csv(data_path)
    return data

# Функция для визуализации с помощью Plotly
def plotly_visualizations(data):
    # Scatter-плот рейтингов по годам
    fig = px.scatter(data, x='releaseYear', y='averageRating', size='numVotes', color='genres',
                     hover_name='title', title='Распределение рейтингов по годам')
    fig.update_layout(xaxis_title='Год выпуска', yaxis_title='Средний рейтинг')
    fig.show()

    # Bubble Chart количества голосов и рейтинга
    fig = px.scatter(data, x='numVotes', y='averageRating', size='numVotes', color='averageRating',
                     hover_name='title', title='Рейтинг vs. Количество голосов', log_x=True)
    fig.update_layout(xaxis_title='Количество голосов (логарифм)', yaxis_title='Средний рейтинг')
    fig.show()

    # Pie chart распределения жанров
    genre_counts = data['genres'].value_counts().reset_index()
    genre_counts.columns = ['genres', 'counts']  # Переименуем столбцы для удобства
    fig = px.pie(genre_counts, names='genres', values='counts', title='Распределение жанров')
    fig.update_traces(textinfo='percent+label')  # Показываем процент и метки
    fig.show()

    # Boxplot рейтинга по жанрам с названием фильма
    fig = px.box(data, x='genres', y='averageRating', title='Рейтинг по жанрам', hover_data={'title': True})
    fig.update_layout(xaxis_title='Жанры', yaxis_title='Средний рейтинг')
    fig.show()

    # Временной ряд рейтингов
    avg_rating_by_year = data.groupby('releaseYear')['averageRating'].mean().reset_index()
    fig = px.line(avg_rating_by_year, x='releaseYear', y='averageRating', title='Средний рейтинг по годам')
    fig.update_layout(xaxis_title='Год выпуска', yaxis_title='Средний рейтинг')
    fig.show()

# Основной блок кода
if __name__ == "__main__":
    data = load_data()
    plotly_visualizations(data)
