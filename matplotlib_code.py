import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

def load_data():
    data = pd.read_csv('C:\\pythonProject\\pythonProject\\Diplom\\data\\data.csv')
    return data

def advanced_matplotlib_visualization(data):
    # Подготовка фигуры
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    # Гистограмма
    axs[0, 0].hist(data['averageRating'], bins=30, alpha=0.7, color='blue')
    axs[0, 0].set_title('Гистограмма среднего рейтинга')

    # Ящик с усами для среднего рейтинга
    axs[0, 1].boxplot(data['averageRating'])
    axs[0, 1].set_title('Ящик с усами для среднего рейтинга')

    # Диаграмма рассеяния
    scatter = axs[1, 0].scatter(data['releaseYear'], data['averageRating'], alpha=0.5)
    axs[1, 0].set_title('Средний рейтинг по годам')

    # Включаем курсор для отображения аннотаций
    mplcursors.cursor(scatter, hover=True).connect("add", lambda sel: sel.annotation.set_text(
        f"{data['title'].iloc[sel.index]}\nЖанр: {data['genres'].iloc[sel.index]}\nID: {data['id'].iloc[sel.index]}"
    ))

    # Линейный график
    avg_rating_per_year = data.groupby('releaseYear')['averageRating'].mean()
    axs[1, 1].plot(avg_rating_per_year.index, avg_rating_per_year, marker='o')
    axs[1, 1].set_title('Средний рейтинг по годам')

    plt.tight_layout()
    plt.show()
