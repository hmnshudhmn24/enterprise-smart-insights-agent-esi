import os
from .data_loader_agent import DataLoaderAgent
from .analysis_agent import AnalysisAgent
from .dashboard_agent import DashboardAgent
from .writer_agent import WriterAgent
from pathlib import Path

OUT_DIR = Path("outputs")
OUT_DIR.mkdir(exist_ok=True)

class OrchestratorAgent:
    def __init__(self, session_service, load_tool):
        self.session = session_service
        self.data_loader = DataLoaderAgent(load_tool)
        self.analysis = AnalysisAgent()
        self.dashboard = DashboardAgent()
        self.writer = WriterAgent()

    def run_pipeline(self, dataset_path):
        # Load & clean
        df = self.data_loader.load(dataset_path)
        self.session.set("last_dataset", str(dataset_path))
        # Analysis
        analysis_results = self.analysis.analyze(df)
        # Dashboard
        chart_paths = self.dashboard.generate(df, analysis_results, out_dir=OUT_DIR)
        # Write report
        summary = self.writer.write_summary(analysis_results, chart_paths)
        # Save summary
        (OUT_DIR / "summary.txt").write_text(summary)
        return {"summary": summary, "charts": chart_paths}
