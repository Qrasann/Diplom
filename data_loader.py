import os
import pandas as pd


def load_data():
  # Путь к файлу data.csv в папке data
  data_path = os.path.join(os.path.dirname(__file__), 'data', 'data.csv')

  # Загрузка данных
  data = pd.read_csv(data_path)
  return data
