"""
preprocessing.py
----------------
This module contains helper functions for data loading, cleaning, feature selection,
and feature scaling for customer segmentation tasks.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from typing import List, Tuple


def load_data(filepath: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns a Pandas DataFrame.

    :param filepath: Path to the CSV file.
    :return: DataFrame containing the loaded data.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return pd.DataFrame()


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the DataFrame by removing duplicates and rows with missing values.

    :param df: Original DataFrame.
    :return: Cleaned DataFrame.
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def get_numeric_features(df: pd.DataFrame, exclude: List[str] = []) -> List[str]:
    """
    Identifies numeric columns in the DataFrame, excluding specified columns.

    :param df: DataFrame to inspect.
    :param exclude: List of column names to exclude from the result.
    :return: List of numeric column names.
    """
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    return [col for col in numeric_cols if col not in exclude]


def scale_features(df: pd.DataFrame, feature_cols: List[str]) -> pd.DataFrame:
    """
    Scales numerical features using StandardScaler.

    :param df: DataFrame containing the features to be scaled.
    :param feature_cols: List of column names to be scaled.
    :return: DataFrame with scaled features.
    """
    df_scaled = df.copy()
    scaler = StandardScaler()
    df_scaled[feature_cols] = scaler.fit_transform(df_scaled[feature_cols])
    return df_scaled


def preprocess_pipeline(filepath: str, exclude_cols: List[str] = []) -> Tuple[pd.DataFrame, List[str]]:
    """
    Complete preprocessing pipeline: loads, cleans, detects features, and scales.

    :param filepath: Path to the raw CSV file.
    :param exclude_cols: Columns to exclude from feature scaling.
    :return: Tuple of (processed DataFrame, list of scaled feature names).
    """
    df = load_data(filepath)
    if df.empty:
        return df, []

    df_clean = clean_data(df)
    feature_cols = get_numeric_features(df_clean, exclude=exclude_cols)
    df_scaled = scale_features(df_clean, feature_cols)
    return df_scaled, feature_cols
