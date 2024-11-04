from matplotlib_code import matplotlib_visualizations
from seaborn_code import seaborn_visualizations
from plotly_code import plotly_visualizations
from data_loader import load_data  

def main():
    data = load_data()  

    print("Визуализация с помощью Matplotlib")
    matplotlib_visualizations(data)

    print("Визуализация с помощью Seaborn")
    seaborn_visualizations(data)

    print("Визуализация с помощью Plotly")
    plotly_visualizations(data)

if __name__ == "__main__":
    main()
