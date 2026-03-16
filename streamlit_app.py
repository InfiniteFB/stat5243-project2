from __future__ import annotations

import io
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from core import (
    FeatureSpec,
    SAMPLE_DATASETS,
    apply_feature_engineering,
    build_profile,
    build_summary_stats,
    handle_missing,
    handle_outliers,
    low_cardinality_columns,
    parse_uploaded_file,
    pick_categorical_default,
    pick_dimension_default,
    pick_numeric_default,
    scale_numeric,
    standardize_text_columns,
)


st.set_page_config(page_title="STAT 5243 Project 2 Demo", page_icon="📊", layout="wide")


def load_uploaded_df(uploaded_file) -> pd.DataFrame:
    temp_path = Path(".streamlit_uploads")
    temp_path.mkdir(exist_ok=True)
    target = temp_path / uploaded_file.name
    target.write_bytes(uploaded_file.getbuffer())
    return parse_uploaded_file(target, uploaded_file.name)


def get_source_df() -> pd.DataFrame:
    mode = st.sidebar.radio("Data source", ["Built-in demo", "Upload file"], key="source_mode")
    if mode == "Built-in demo":
        selected = st.sidebar.selectbox("Built-in dataset", list(SAMPLE_DATASETS.keys()), key="demo_dataset")
        return SAMPLE_DATASETS[selected].copy()

    uploaded = st.sidebar.file_uploader("Upload a dataset", type=["csv", "xlsx", "xls", "json", "rds"])
    if uploaded is None:
        return SAMPLE_DATASETS["Sales Performance Demo"].copy()
    return load_uploaded_df(uploaded)


def build_processed_df(source_df: pd.DataFrame) -> pd.DataFrame:
    df = standardize_text_columns(source_df)
    if st.sidebar.toggle("Remove duplicate rows", True):
        df = df.drop_duplicates()
    df = handle_missing(df, st.sidebar.selectbox("Missing values", ["none", "drop", "mean", "median", "mode"], index=2))
    df = handle_outliers(df, st.sidebar.selectbox("Outlier handling", ["none", "cap", "remove"], index=1))
    df = scale_numeric(df, st.sidebar.selectbox("Numeric scaling", ["none", "zscore", "minmax"], index=0))
    if st.sidebar.toggle("One-hot encode categorical columns", False):
        text_cols = list(df.select_dtypes(exclude=["number", "datetime"]).columns)
        if text_cols:
            df = pd.get_dummies(df, columns=text_cols, dummy_na=True)
    return df


def render_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    st.subheader("Feature Engineering")
    numeric_cols = list(df.select_dtypes(include="number").columns)
    specs = st.session_state.setdefault("feature_specs_streamlit", [])
    col1, col2, col3 = st.columns(3)
    with col1:
        op = st.selectbox("Operation", ["sum", "difference", "product", "ratio", "log", "bin"])
        col_a = st.selectbox("Column A", numeric_cols if numeric_cols else list(df.columns))
    with col2:
        col_b = st.selectbox("Column B", numeric_cols if numeric_cols else list(df.columns), disabled=op in {"log", "bin"})
        new_name = st.text_input("New feature name", value="engineered_feature")
    with col3:
        bins = st.slider("Bins", 2, 8, 4)
        if st.button("Add feature"):
            specs.append(FeatureSpec(op, col_a, None if op in {"log", "bin"} else col_b, new_name, bins))
        if st.button("Reset features"):
            specs.clear()

    if specs:
        st.dataframe(pd.DataFrame([vars(spec) for spec in specs]), use_container_width=True)
    return apply_feature_engineering(df, specs)


def render_eda(df: pd.DataFrame) -> None:
    st.subheader("Exploratory Data Analysis")
    numeric_cols = list(df.select_dtypes(include="number").columns)
    all_cols = list(df.columns)
    categorical_cols = low_cardinality_columns(df, max_unique=25)

    default_x = pick_dimension_default(df) or (all_cols[0] if all_cols else None)
    default_y = pick_numeric_default(df, 1) or pick_numeric_default(df, 0) or (all_cols[0] if all_cols else None)

    c1, c2, c3, c4 = st.columns(4)
    plot_type = c1.selectbox("Chart type", ["bar", "line", "histogram", "scatter", "box"])
    x = c2.selectbox("X variable", all_cols, index=all_cols.index(default_x) if default_x in all_cols else 0)
    y_choices = numeric_cols if numeric_cols else all_cols
    y = c3.selectbox("Y variable", y_choices, index=y_choices.index(default_y) if default_y in y_choices else 0)
    metric_choices = ["count"] + numeric_cols
    metric = c4.selectbox("Metric", metric_choices, index=0)

    c5, c6, c7, c8 = st.columns(4)
    agg = c5.selectbox("Aggregation", ["count", "mean", "median", "sum", "max", "min"])
    color = c6.selectbox("Color / group", ["None"] + categorical_cols, index=0 if not pick_categorical_default(df) else (["None"] + categorical_cols).index(pick_categorical_default(df)))
    top_n = c7.slider("Top categories", 5, 30, 12)
    bins = c8.slider("Histogram bins", 10, 60, 25)

    color = None if color == "None" else color

    if plot_type in {"bar", "line"}:
        group_cols = [x] + ([color] if color and color != x else [])
        if metric == "count" or agg == "count":
            grouped = df.groupby(group_cols, dropna=False).size().reset_index(name="value")
        else:
            grouped = df.groupby(group_cols, dropna=False)[metric].agg(agg).reset_index(name="value")
        order = grouped.groupby(x)["value"].sum().sort_values(ascending=False).head(top_n).index
        grouped = grouped[grouped[x].isin(order)]
        fig = px.bar(grouped, x=x, y="value", color=color, barmode="group") if plot_type == "bar" else px.line(grouped, x=x, y="value", color=color, markers=True)
    elif plot_type == "histogram":
        fig = px.histogram(df, x=x, color=color, marginal="box", nbins=bins)
    elif plot_type == "scatter":
        sample_df = df.sample(min(len(df), 4000), random_state=42) if len(df) > 4000 else df
        fig = px.scatter(sample_df, x=x, y=y, color=color)
    else:
        fig = px.box(df, x=color or x, y=y, color=color if color and color != x else None)

    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

    col_left, col_right = st.columns([1.3, 1])
    with col_left:
        st.plotly_chart(fig, use_container_width=True)
    with col_right:
        stats = build_summary_stats(df)
        st.dataframe(stats, use_container_width=True, height=360)
        corr_numeric = df.select_dtypes(include="number")
        if corr_numeric.shape[1] >= 2:
            corr = corr_numeric.corr(numeric_only=True).round(2)
            corr_fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale=["#14324a", "#f4efe6", "#d85f3c"])
            st.plotly_chart(corr_fig, use_container_width=True)


st.title("DataCanvas Studio")
st.caption("Streamlit deployment entrypoint for STAT 5243 Project 2")

with st.sidebar:
    st.markdown("### Workflow")
    st.write("Choose a dataset, clean it, engineer features, explore it, and download the processed result.")

source_df = get_source_df()
processed_df = build_processed_df(source_df)

tab1, tab2, tab3, tab4 = st.tabs(["Guide", "Data", "Feature Engineering", "EDA"])

with tab1:
    st.markdown(
        """
        ### Supported workflow
        - Upload `CSV`, `Excel`, `JSON`, or `RDS`
        - Clean missing values, duplicates, outliers, and scaling
        - Engineer features with arithmetic, ratios, logs, and bins
        - Explore the processed result with interactive Plotly charts
        """
    )

with tab2:
    c1, c2 = st.columns([0.35, 0.65])
    with c1:
        st.subheader("Dataset profile")
        st.dataframe(build_profile(processed_df), use_container_width=True, hide_index=True)
    with c2:
        st.subheader("Processed preview")
        st.dataframe(processed_df.head(100), use_container_width=True, height=420)
        csv_data = processed_df.to_csv(index=False).encode("utf-8")
        st.download_button("Download processed CSV", csv_data, file_name="processed_dataset.csv", mime="text/csv")

with tab3:
    featured_df = render_feature_engineering(processed_df)
    st.subheader("Feature-enhanced preview")
    st.dataframe(featured_df.head(100), use_container_width=True, height=420)

with tab4:
    featured_df = apply_feature_engineering(processed_df, st.session_state.get("feature_specs_streamlit", []))
    render_eda(featured_df)
