# Project 2 Report

## Application Overview

Our application, **DataCanvas Studio**, is an interactive web tool for dataset uploading, cleaning, preprocessing, feature engineering, and exploratory data analysis. The app was designed to help users work with tabular data through a guided interface rather than writing code manually. Users can either upload their own dataset or start from one of the built-in demo datasets included in the application.

The application supports multiple file formats, including CSV, Excel, JSON, and RDS. After loading a dataset, users can inspect a raw preview and view a dataset profile that summarizes the number of rows, columns, missing values, duplicate rows, and the balance between numeric and categorical variables.

## Functionalities And How To Use The App

The app is organized into several tabs. The **Guide** tab introduces the workflow and explains the main capabilities. In the **Data Source** tab, users choose between built-in datasets and uploaded files. In the **Cleaning** tab, users can select how to handle missing values, duplicate rows, outliers, scaling, and optional one-hot encoding for categorical variables. These settings update the processed preview dynamically so users can immediately see the impact of each transformation.

The **Feature Engineering** tab allows users to create new variables through arithmetic operations, ratios, logarithmic transformation, and numeric binning. This makes it possible to generate informative variables without editing the source file. The **EDA** tab provides summary statistics, a missing-value chart, an interactive Plotly visualization panel, and a correlation heatmap. Users can also filter the displayed dataset before plotting, which supports more targeted exploration. Finally, the **Export** tab summarizes the current dataset state and allows users to download the processed result as a CSV file.

Deployment link: `ADD_DEPLOYED_LINK_HERE`

## Team Contributions

- Team Member 1: designed and implemented the upload, cleaning, and preprocessing workflow
- Team Member 2: implemented feature engineering and interactive EDA components
- Team Member 3: refined the user interface, documentation, deployment, and final testing
