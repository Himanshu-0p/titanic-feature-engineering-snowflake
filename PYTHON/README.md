# Python Code - Snowpark Pipeline

## Overview
Snowpark Python implementation for feature enhancement and analysis.

## File
- `titanic_vistara_python.py` - Main pipeline (12 steps)

## How to Run

1. Open Snowflake Python Worksheet
2. Set database context:
   - Database: TITANIC_VISTARA_PROJECT
   - Schema: FEATURES
3. Paste code and click Run

## Prerequisites
- Python 3.11
- Pre-installed: pandas, numpy, scikit-learn, snowflake-snowpark-python

## Pipeline Steps
1. Load normalized features
2. Create additional features
3. Save enhanced features
4. Compute statistics
5. Create train/test split
6. Save splits
7. Feature analysis by class
8. Feature analysis by sex
9. Convert to Pandas
10. Compute correlations
11. Save correlations
12. Summary statistics

## Output Tables
- FEATURES_PYTHON_ENHANCED
- TRAIN_DATA_PYTHON
- TEST_DATA_PYTHON
- FEATURE_CORRELATIONS_PYTHON

## Key Correlations
- Sex Survival Rate: 0.543 (strongest)
- Class Survival Rate: 0.334
- Has Cabin: 0.317
