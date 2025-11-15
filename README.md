# Enterprise Smart Insights Agent (ESIA) - Minimal Demo

This repository is a **minimal, self-contained demo** of the Enterprise Smart Insights Agent (ESIA) for the Kaggle Capstone.
It is intentionally lightweight so it can run without cloud deployment or paid LLM access. If you have Gemini/other LLM API access,
you can configure environment variables as described below to use the real LLM.

## What is included
- `main.py` : entrypoint that runs a demo pipeline
- `agents/` : simple agent implementations (orchestrator, data_loader, analysis, dashboard, writer)
- `tools/` : helper tools (load_csv, dashboard generator)
- `memory/` : simple in-memory session & memory bank
- `requirements.txt` : Python deps
- `example_data/sales.csv` : a small example dataset
- `LICENSE` : MIT

## Run locally (Python 3.9+)
1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # on Windows use .venv\Scripts\activate
pip install -r requirements.txt
```

2. (Optional) Configure LLM:
- If you have a Gemini/LLM API, set `LLM_API_KEY` and `LLM_PROVIDER` environment variables.
  ESIA will attempt to use the real LLM; otherwise it falls back to a safe **mock LLM** for demos.

3. Run the demo:
```bash
python main.py example_data/sales.csv
```

You should see the pipeline run and outputs created in `outputs/`.

## Notes
- **DO NOT** commit API keys to GitHub.
- This demo is designed for clarity and reproducibility for the Kaggle writeup. For full production integration with ADK/Gemini/Agent Engine, see the Capstone resources and ADK docs.

