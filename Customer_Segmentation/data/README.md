# Data Overview

This folder contains the data files used for the **Customer Segmentation** project.

## Dataset

- **File**: `customer_data.csv`
- **Source**: Synthetic / Example data for demonstration.
- **Description**:
  - **CustomerID**: Unique ID for each customer.
  - **Gender**: Male or Female.
  - **Age**: Age of the customer in years.
  - **AnnualIncome**: Annual income (in thousands of dollars).
  - **SpendingScore**: A 1-100 score indicating the customer’s spending habits (subjective metric).

## Data Cleaning Notes

1. **Missing Values**: This dataset may or may not contain missing values, but you should always check before proceeding.
2. **Duplicates**: Each `CustomerID` should be unique, but double-check for duplicates.
3. **Outliers**: Inspect columns like `Age`, `AnnualIncome`, and `SpendingScore` for potential outliers.

## Usage

You can replace `customer_data.csv` with your actual dataset to perform a real-life customer segmentation analysis. Adjust any preprocessing steps as needed to fit your data’s format and quality.

---

**Disclaimer**: This dataset is for example purposes only. In a production environment, ensure compliance with data protection regulations (e.g., GDPR, HIPAA) when handling sensitive customer information.
