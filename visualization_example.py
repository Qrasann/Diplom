from matplotlib_code import advanced_matplotlib_visualization
from seaborn_code import seaborn_visualization
from plotly_code import plotly_visualization

def main():
    # Загрузка данных
    from matplotlib_code import load_data
    data = load_data()  # Загружаем данные

    print("Визуализация с помощью Matplotlib")
    advanced_matplotlib_visualization(data)

    print("Визуализация с помощью Seaborn")
    seaborn_visualization(data)

    print("Визуализация с помощью Plotly")
    plotly_visualization(data)

if __name__ == "__main__":
    main()
