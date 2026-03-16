# STAT 5243 Project 2 Demo

This repository contains a deployable `Streamlit` web application for STAT 5243 Project 2. The app lets users upload a dataset, clean and preprocess it, engineer new features, explore the data through interactive visualizations, and export the processed result.

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

- [streamlit_app.py](/Users/yedoubleeagles/BaiduNetdiskWorkspace/columbia/2026%20Spring/STAT%205243/p2/streamlit_app.py): main Streamlit deployment entrypoint
- [core.py](/Users/yedoubleeagles/BaiduNetdiskWorkspace/columbia/2026%20Spring/STAT%205243/p2/core.py): shared data loading, cleaning, feature engineering, and EDA helpers
- [app.py](/Users/yedoubleeagles/BaiduNetdiskWorkspace/columbia/2026%20Spring/STAT%205243/p2/app.py): earlier Python Shiny prototype retained for reference
- [requirements.txt](/Users/yedoubleeagles/BaiduNetdiskWorkspace/columbia/2026%20Spring/STAT%205243/p2/requirements.txt): Python dependencies
- [report.md](/Users/yedoubleeagles/BaiduNetdiskWorkspace/columbia/2026%20Spring/STAT%205243/p2/report.md): short report draft that can be adapted for submission

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

## Run The App

```bash
conda activate py311
streamlit run streamlit_app.py
```

By default, Streamlit will print a local URL such as `http://127.0.0.1:8501`.

## Deployment

This repository is ready for `Streamlit Community Cloud` deployment:

1. Push the repo to GitHub
2. Create a new app in Streamlit Community Cloud
3. Select this repository and set the main file path to `streamlit_app.py`
4. Let Streamlit install `requirements.txt`

For the course report, include the public deployment link.

## Notes For Submission

- Add team member names and contributions to the report before submitting
- The deployed app entrypoint is `streamlit_app.py`
- The repository also keeps the earlier Shiny prototype in case you want to compare UI approaches or reuse pieces later
