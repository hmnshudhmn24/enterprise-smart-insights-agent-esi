import pandas as pd
import numpy as np

class AnalysisAgent:
    def __init__(self):
        pass

    def analyze(self, df):
        print("[Analysis] Running exploratory analysis...")
        results = {}
        # Simple KPIs
        results["row_count"] = len(df)
        results["revenue_sum"] = float(df["revenue"].sum())
        results["units_sum"] = int(df["units"].sum())
        # Top products
        prod = df.groupby("product").agg({"revenue":"sum","units":"sum"}).reset_index()
        results["top_products"] = prod.sort_values("revenue", ascending=False).to_dict(orient="records")
        # Regional breakdown
        reg = df.groupby("region").agg({"revenue":"sum"}).reset_index()
        results["region_summary"] = reg.to_dict(orient="records")
        # Simple anomaly detection: revenue > mean + 2*std
        mean = df["revenue"].mean()
        std = df["revenue"].std()
        anomalies = df[df["revenue"] > mean + 2*std]
        results["anomalies"] = anomalies.to_dict(orient="records")
        print("[Analysis] Done.")
        return results
