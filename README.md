# STAT 5243 Project 2 Demo

This repository contains a polished `Python Shiny` web application for STAT 5243 Project 2. The app lets users upload a dataset, clean and preprocess it, engineer new features, explore the data through interactive visualizations, and export the processed result.

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

- [app.py](/Users/yedoubleeagles/BaiduNetdiskWorkspace/columbia/2026%20Spring/STAT%205243/p2/app.py): main Shiny application
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
shiny run --reload app.py
```

By default, Shiny will print a local URL such as `http://127.0.0.1:8000`.

## Deployment

You can deploy the app to a platform that supports Python Shiny, such as:

- [Posit Connect Cloud](https://connect.posit.cloud/)
- [shinyapps.io](https://www.shinyapps.io/) if you adapt the deployment workflow for Python Shiny
- a generic container or cloud VM

For the course report, include the deployment link and a short description of the supported workflow.

## Notes For Submission

- Add team member names and contributions to the report before submitting
- If your instructor strongly prefers `R Shiny`, this project can be used as the demo/prototype while the report explicitly notes that the implementation is in Python Shiny
- If needed, I can also convert this version into an `R Shiny` structure later
