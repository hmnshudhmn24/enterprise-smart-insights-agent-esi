#!/usr/bin/env python3
import sys
from agents.orchestrator_agent import OrchestratorAgent
from tools.load_csv_tool import LoadCSVTool
from memory.session_service import InMemorySessionService
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py path/to/dataset.csv")
        return
    dataset_path = sys.argv[1]
    session_service = InMemorySessionService()
    load_tool = LoadCSVTool()
    orchestrator = OrchestratorAgent(session_service, load_tool)
    output = orchestrator.run_pipeline(dataset_path)
    print("Pipeline finished. Outputs saved to outputs/")
    print("Executive summary:\n")
    print(output["summary"])

if __name__ == '__main__':
    main()
