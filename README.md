# STAT 5243 Project 2 Demo

This repository contains a deployable interactive data application for STAT 5243 Project 2. The primary deployment target is the `Python Shiny` app in `app.py`, which preserves the polished interface and interaction model built for the project. A secondary `Streamlit` entrypoint is also included for hosting flexibility.

## Features

- Upload datasets in `CSV`, `Excel`, `JSON`, and `RDS`
- Explore one of two built-in demo datasets when no file is available
- Clean and preprocess data with controls for:
  - missing values
  - duplicate rows
  - outlier handling
  - scaling
  - one-hot encoding
- Create engineered features using arithmetic transforms, ratios, logs, and binning
- Run EDA with:
  - dataset profile
  - summary statistics
  - missing-value chart
  - interactive Plotly visualizations
  - correlation heatmap
- Download the processed dataset as a CSV

## Project Structure

- `app.py`: main Python Shiny application for deployment
- `streamlit_app.py`: optional Streamlit deployment entrypoint
- `core.py`: shared data loading, cleaning, feature engineering, and EDA helpers used by the Streamlit variant
- `requirements.txt`: Python dependencies
- `manifest.json`: generated deployment manifest for Python Shiny
- `.python-version`: pins the Python version for deployment

## Miniforge Environment

This project is set up to run in the existing Miniforge environment named `py311`.

```bash
conda activate py311
python --version
```

## Installation

If the environment does not already have the required packages:

```bash
conda activate py311
python -m pip install -r requirements.txt
```

## Run The Shiny App

```bash
conda activate py311
shiny run --reload app.py
```

By default, Shiny will print a local URL such as `http://127.0.0.1:8000`.

## Optional Streamlit Variant

If you want to run the lighter secondary version instead:

```bash
conda activate py311
streamlit run streamlit_app.py
```

## Deployment

This repository is ready for `Python Shiny` deployment.

### Posit Connect Cloud

1. Push the repo to GitHub
2. Create a new app in Posit Connect Cloud
3. Select this repository and set the app entrypoint to `app.py`
4. Let the platform install `requirements.txt`

### shinyapps.io with rsconnect-python

1. Install `rsconnect-python`
2. Add your shinyapps.io account token and secret
3. Deploy this directory with `app.py` as the entrypoint

For the course report, include the public deployment link.

## GitHub Copilot Model Selection

This repository is used with GitHub Copilot Pro. For guidance on selecting Claude Opus 4.5/4.6 models and enabling Fast Mode in Copilot Chat, VS Code, or JetBrains IDEs, see [COPILOT_MODEL_GUIDE.md](./COPILOT_MODEL_GUIDE.md).

