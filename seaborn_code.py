import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mplcursors

def load_data():
    data = pd.read_csv('C:\\pythonProject\\pythonProject\\Diplom\\data\\data.csv')
    return data

def seaborn_visualization(data):
    plt.figure(figsize=(10, 6))
    hist = sns.histplot(data=data, x='averageRating', kde=True)

    plt.title('Гистограмма среднего рейтинга с KDE')

    # Включаем курсор для отображения аннотаций
    mplcursors.cursor(hist.patches, hover=True).connect("add", lambda sel: sel.annotation.set_text(
        f"{data['title'].iloc[sel.index]}\nЖанр: {data['genres'].iloc[sel.index]}\nID: {data['id'].iloc[sel.index]}"
    ))

    plt.show()
