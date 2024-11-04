import matplotlib.pyplot as plt
import mplcursors
import os
import pandas as pd

def load_data():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'data.csv')
    data = pd.read_csv(data_path)
    return data

def matplotlib_visualizations(data):
    # Гистограмма распределения рейтинга
    plt.figure(figsize=(12, 6))
    plt.hist(data['averageRating'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Распределение среднего рейтинга фильмов')
    plt.xlabel('Средний рейтинг')
    plt.ylabel('Количество фильмов')
    plt.grid(True)
    plt.show()

    # Визуализация среднего рейтинга по годам
    avg_rating_per_year = data.groupby('releaseYear')['averageRating'].mean()
    plt.figure(figsize=(12, 6))
    line, = plt.plot(avg_rating_per_year.index, avg_rating_per_year, marker='o', color='green')
    plt.title('Изменение среднего рейтинга по годам')
    plt.xlabel('Год выпуска')
    plt.ylabel('Средний рейтинг')
    mplcursors.cursor(line, hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(f"Год: {int(sel.target[0])}\nРейтинг: {sel.target[1]:.2f}")
    )
    plt.show()

    # Диаграмма количества голосов и среднего рейтинга
    plt.figure(figsize=(12, 6))
    scatter = plt.scatter(data['numVotes'], data['averageRating'], alpha=0.5, color='purple')
    plt.title('Распределение количества голосов и среднего рейтинга')
    plt.xlabel('Количество голосов')
    plt.ylabel('Средний рейтинг')
    plt.xscale('log')
    mplcursors.cursor(scatter, hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(
            f"Фильм: {data['title'].iloc[sel.index]}\nГолоса: {data['numVotes'].iloc[sel.index]}\nРейтинг: {data['averageRating'].iloc[sel.index]}"
        )
    )
    plt.show()

    # Показ среднего рейтинга по жанрам
    avg_rating_by_genre = data.groupby('genres')['averageRating'].mean()
    plt.figure(figsize=(12, 6))
    barh = plt.barh(range(len(avg_rating_by_genre)), avg_rating_by_genre, color='salmon')
    plt.title('Средний рейтинг по жанрам')
    plt.xlabel('Средний рейтинг')

    plt.yticks([])

    mplcursors.cursor(barh, hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(
            f"Жанр: {avg_rating_by_genre.index[sel.index]}\nРейтинг: {avg_rating_by_genre[sel.index]:.2f}"
        )
    )
    plt.show()

    # Гистограмма количества фильмов по годам
    movie_count_by_year = data['releaseYear'].value_counts()
    plt.figure(figsize=(12, 6))
    bar = plt.bar(movie_count_by_year.index, movie_count_by_year.values, color='cornflowerblue')
    plt.title('Количество фильмов по годам')
    plt.xlabel('Год')
    plt.ylabel('Количество фильмов')
    mplcursors.cursor(bar, hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(f"Год: {movie_count_by_year.index[sel.index]}\nКоличество: {movie_count_by_year.values[sel.index]}")
    )
    plt.show()

if __name__ == "__main__":
    data = load_data()
    matplotlib_visualizations(data)
