# SQL Code - Feature Engineering Pipeline

## Overview
Complete SQL implementation for feature engineering on Titanic dataset in Snowflake.

## Files
- `titanic_vistara_sql.sql` - Main pipeline (10 steps)
- `verify_project.sql` - Verification queries

## How to Run

1. Open Snowflake SQL Worksheet
2. Copy entire code from `titanic_vistara_sql.sql`
3. Run all statements

## Tables Created
1. RAW_TITANIC - 891 records
2. FEATURES_BASIC - Basic features
3. FEATURES_AGGREGATED - Group stats
4. FEATURES_CLEANED - Missing values handled
5. FEATURES_ENCODED - Categorical encoding
6. FEATURES_NORMALIZED - Z-score normalized
7. FEATURE_STORE - 8 features stored
8. TRAIN_DATA - 713 records (80%)
9. TEST_DATA - 178 records (20%)

## Key SQL Concepts Used
- CREATE TABLE
- WITH (CTE) queries
- Window functions (MEDIAN OVER)
- CASE statements
- JOIN operations
- UNION queries

## Verification
Run `verify_project.sql` to confirm all tables created successfully.
