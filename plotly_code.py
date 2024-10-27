import pandas as pd
import plotly.express as px

def load_data():
    data = pd.read_csv('C:\\pythonProject\\pythonProject\\Diplom\\data\\data.csv')
    return data

def plotly_visualization(data):
    fig = px.scatter(data, x='releaseYear', y='averageRating',
                     color='averageRating',
                     title='Средний рейтинг по годам',
                     labels={'releaseYear': 'Год выпуска', 'averageRating': 'Средний рейтинг'},
                     color_continuous_scale=px.colors.sequential.Viridis,
                     hover_name='title',  # Отображение названия
                     hover_data=['genres', 'id'])  # Отображение жанра и ID

    fig.show()
