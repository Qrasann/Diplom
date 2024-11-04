import os
import pandas as pd


def load_data():
  data_path = os.path.join(os.path.dirname(__file__), 'data', 'data.csv')

  data = pd.read_csv(data_path)
  return data
