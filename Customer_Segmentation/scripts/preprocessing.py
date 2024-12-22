"""
preprocessing.py
----------------
This module contains helper functions for data loading, cleaning, and feature scaling.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

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
        print(f"File not found: {filepath}")
        return pd.DataFrame()

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the provided DataFrame by removing duplicates, handling missing values, etc.
    
    :param df: Original DataFrame.
    :return: Cleaned DataFrame.
    """
    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values (example: drop rows with any nulls)
    df = df.dropna()

    # Convert columns to correct data types if necessary
    # e.g. df['AnnualIncome'] = df['AnnualIncome'].astype(int)
    
    return df

def scale_features(df: pd.DataFrame, feature_cols: list) -> pd.DataFrame:
    """
    Scales numerical features using StandardScaler.
    
    :param df: DataFrame containing the features to be scaled.
    :param feature_cols: List of column names to be scaled.
    :return: DataFrame with scaled features.
    """
    df_copy = df.copy()
    
    scaler = StandardScaler()
    df_copy[feature_cols] = scaler.fit_transform(df_copy[feature_cols])
    
    return df_copy
