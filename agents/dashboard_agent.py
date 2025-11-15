import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

class DashboardAgent:
    def __init__(self):
        pass

    def generate(self, df, analysis_results, out_dir=Path("outputs")):
        out_dir.mkdir(exist_ok=True)
        chart_paths = []
        # Revenue by region
        reg = df.groupby("region").agg({"revenue":"sum"}).reset_index()
        p1 = out_dir / "revenue_by_region.png"
        reg.plot(kind="bar", x="region", y="revenue", legend=False)
        plt.title("Revenue by Region")
        plt.tight_layout()
        plt.savefig(p1)
        plt.clf()
        chart_paths.append(str(p1))
        # Top products chart
        prod = df.groupby("product").agg({"revenue":"sum"}).reset_index()
        p2 = out_dir / "top_products.png"
        prod.plot(kind="bar", x="product", y="revenue", legend=False)
        plt.title("Top Products by Revenue")
        plt.tight_layout()
        plt.savefig(p2)
        plt.clf()
        chart_paths.append(str(p2))
        return chart_paths
