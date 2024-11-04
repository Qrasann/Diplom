import seaborn as sns
import matplotlib.pyplot as plt
import mplcursors
import pandas as pd
import os

def load_data():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'data.csv')
    data = pd.read_csv(data_path)
    return data

def seaborn_visualizations(data):
    # Гистограмма распределения рейтинга
    plt.figure(figsize=(10, 6))
    sns.histplot(data['averageRating'], kde=True, color='blue')

    plt.title('Гистограмма рейтингов с KDE')
    plt.xlabel('Средний рейтинг')
    plt.ylabel('Количество')

    plt.show()

    plt.figure(figsize=(14, 8))
    boxplot = sns.boxplot(data=data, x='averageRating', y='genres', palette='Set2')
    plt.title('Распределение рейтинга по жанрам')
    plt.yticks([])
    plt.ylabel('Жанры')

    plt.xlabel('Средний рейтинг')

    mplcursors.cursor(boxplot.get_children(), hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(
            f"Жанр: {data['genres'].unique()[sel.target[1]]}\nСредний рейтинг: {sel.target[0]:.2f}"
        )
    )

    plt.show()

    # Корреляционная матрица
    plt.figure(figsize=(10, 8))

    corr_data = data[['averageRating', 'numVotes']].rename(
        columns={'averageRating': 'Средний рейтинг', 'numVotes': 'Количество голосов'}
    ).corr()

    sns.heatmap(corr_data, annot=True, cmap='coolwarm', center=0)
    plt.title('Корреляция рейтинга и количества голосов')
    plt.show()

    # Средний рейтинг по годам
    plt.figure(figsize=(12, 6))
    lineplot = sns.lineplot(x='releaseYear', y='averageRating', data=data, marker='o', color='orange')
    plt.title('Средний рейтинг по годам')
    plt.xlabel('Год')
    plt.ylabel('Средний рейтинг')
    cursor = mplcursors.cursor(lineplot.figure, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(
        f"Год: {int(data['releaseYear'].iloc[sel.target.index])}\n"
        f"Рейтинг: {data['averageRating'].iloc[sel.target.index]:.2f}\n"
        f"Фильм: {data['title'].iloc[sel.target.index]}"
    ))
    plt.show()
"""
    # Violin plot рейтинга по жанрам с аннотациями фильмов
    plt.figure(figsize=(14, 8))

    # Переименовываем столбцы и строим violin plot
    violinplot = sns.violinplot(data=data.rename(columns={'averageRating': 'Средний рейтинг', 'genres': 'Жанры'}),
                                x='Жанры', y='Средний рейтинг', palette='coolwarm')

    # Убираем метки оси x
    violinplot.set_xticklabels(['' for _ in range(len(data['genres'].unique()))])

    # Добавляем аннотации с названием жанра, средним рейтингом и названием фильма
    cursor = mplcursors.cursor(violinplot.figure, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(
        f"Жанр: {data['genres'].iloc[sel.target.index]}\n"
        f"Средний рейтинг: {data['averageRating'].iloc[sel.target.index]:.2f}\n"
        f"Фильм: {data['title'].iloc[sel.target.index]}"
    ))

    plt.title('Распределение рейтингов по жанрам')
    plt.xlabel('Жанры')
    plt.ylabel('Средний рейтинг')
    plt.show()
"""
if __name__ == "__main__":
    data = load_data()
    seaborn_visualizations(data)
