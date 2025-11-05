import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col, when, avg, count, lit
import pandas as pd
import numpy as np

def main(session: snowpark.Session):
    
    print("="*60)
    print("TITANIC VISTARA PROJECT - Python Pipeline")
    print("="*60)
    
    session.use_database("TITANIC_VISTARA_PROJECT")
    session.use_schema("FEATURES")
    
    print("\n[STEP 1] Loading normalized features...")
    features_df = session.table("FEATURES_NORMALIZED")
    total_records = features_df.count()
    print(f"Loaded {total_records} records")
    
    print("\n[STEP 2] Creating additional features...")
    enhanced_df = features_df.with_column(
        "FAMILY_SIZE_SQUARED",
        col("FAMILY_SIZE") * col("FAMILY_SIZE")
    ).with_column(
        "AGE_FARE_INTERACTION",
        col("AGE_NORMALIZED") * col("FARE_NORMALIZED")
    ).with_column(
        "HIGH_CLASS_MALE",
        when((col("PCLASS") == 1) & (col("SEX_MALE") == 1), lit(1)).otherwise(lit(0))
    )
    
    print("Created: FAMILY_SIZE_SQUARED, AGE_FARE_INTERACTION, HIGH_CLASS_MALE")
    
    print("\n[STEP 3] Saving enhanced features...")
    enhanced_df.write.mode("overwrite").save_as_table("FEATURES_PYTHON_ENHANCED")
    print("Saved to FEATURES_PYTHON_ENHANCED")
    
    print("\n[STEP 4] Computing statistics...")
    stats_df = features_df.select(
        avg("AGE_NORMALIZED").alias("AVG_AGE"),
        avg("FARE_NORMALIZED").alias("AVG_FARE"),
        avg("SURVIVED").alias("SURVIVAL_RATE"),
        count("*").alias("TOTAL_RECORDS")
    )
    
    print("\nDataset Statistics:")
    stats_df.show()
    
    print("\n[STEP 5] Creating train/test split...")
    train_df = enhanced_df.filter(col("PASSENGERID") % 5 != 0)
    test_df = enhanced_df.filter(col("PASSENGERID") % 5 == 0)
    
    train_count = train_df.count()
    test_count = test_df.count()
    
    print(f"Train set: {train_count} records")
    print(f"Test set: {test_count} records")
    
    print("\n[STEP 6] Saving train/test data...")
    train_df.write.mode("overwrite").save_as_table("TRAIN_DATA_PYTHON")
    test_df.write.mode("overwrite").save_as_table("TEST_DATA_PYTHON")
    print("Saved TRAIN_DATA_PYTHON and TEST_DATA_PYTHON")
    
    print("\n[STEP 7] Feature analysis...")
    
    raw_df = session.table("RAW_TITANIC")
    
    print("\nSurvival Rate by Class:")
    class_analysis = raw_df.group_by("PCLASS").agg(
        avg("SURVIVED").alias("SURVIVAL_RATE"),
        count("*").alias("TOTAL")
    ).sort("PCLASS")
    class_analysis.show()
    
    print("\nSurvival Rate by Sex:")
    sex_analysis = raw_df.group_by("SEX").agg(
        avg("SURVIVED").alias("SURVIVAL_RATE"),
        count("*").alias("TOTAL")
    )
    sex_analysis.show()
    
    print("\n[STEP 8] Retrieving from Feature Store...")
    feature_store_df = session.table("FEATURE_STORE")
    store_count = feature_store_df.count()
    print(f"Feature Store has {store_count} feature records")
    
    unique_features = feature_store_df.select("FEATURE_NAME").distinct().count()
    print(f"Unique features: {unique_features}")
    
    print("\n[STEP 9] Converting to Pandas for analysis...")
    
    features_pandas = enhanced_df.select(
        "SURVIVED",
        "AGE_NORMALIZED",
        "FARE_NORMALIZED",
        "FAMILY_SIZE",
        "IS_ALONE",
        "HAS_CABIN",
        "CLASS_SURVIVAL_RATE",
        "SEX_SURVIVAL_RATE"
    ).to_pandas()
    
    print(f"Converted {len(features_pandas)} rows to Pandas")
    
    print("\n[STEP 10] Computing correlations...")
    
    correlations = features_pandas.corr()["SURVIVED"].sort_values(ascending=False)
    
    print("\nFeature Correlations with Survival:")
    print(correlations)
    
    print("\n[STEP 11] Saving correlations...")
    
    corr_df = pd.DataFrame({
        'FEATURE': correlations.index,
        'CORRELATION': correlations.values
    })
    
    session.create_dataframe(corr_df).write.mode("overwrite").save_as_table("FEATURE_CORRELATIONS_PYTHON")
    print("Saved to FEATURE_CORRELATIONS_PYTHON")
    
    print("\n[STEP 12] Summary statistics...")
    
    summary_stats = pd.DataFrame({
        'Total Records': [len(features_pandas)],
        'Survived': [features_pandas['SURVIVED'].sum()],
        'Survival Rate': [f"{features_pandas['SURVIVED'].mean()*100:.2f}%"]
    })
    
    print("\nDataset Summary:")
    print(summary_stats)
    
    print("\n" + "="*60)
    print("PIPELINE COMPLETED SUCCESSFULLY!")
    print("="*60)
    
    print("\nCreated Tables:")
    print("  1. FEATURES_PYTHON_ENHANCED")
    print("  2. TRAIN_DATA_PYTHON")
    print("  3. TEST_DATA_PYTHON")
    print("  4. FEATURE_CORRELATIONS_PYTHON")
    
    print("\nAvailable Tables for ML:")
    print("  - TRAIN_DATA_PYTHON (for model training)")
    print("  - TEST_DATA_PYTHON (for model evaluation)")
    
    return enhanced_df.limit(10)
