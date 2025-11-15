import pandas as pd

class LoadCSVTool:
    def __init__(self):
        pass

    def load_csv(self, path):
        # Basic CSV loader with automatic parsing
        df = pd.read_csv(path, parse_dates=True)
        return df
