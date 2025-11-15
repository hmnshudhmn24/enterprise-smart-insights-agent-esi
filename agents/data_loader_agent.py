import pandas as pd

class DataLoaderAgent:
    def __init__(self, load_tool):
        self.load_tool = load_tool

    def load(self, path):
        print(f"[DataLoader] Loading dataset from: {path}")
        df = self.load_tool.load_csv(path)
        # Basic cleaning
        df = df.dropna()
        print(f"[DataLoader] Loaded {len(df)} rows and {len(df.columns)} columns")
        return df
