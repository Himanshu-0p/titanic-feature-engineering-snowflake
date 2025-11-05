# 📊 Results & Output Summary
## Project: Titanic Feature Engineering with Snowflake

---

## 👁️ Quick Overview
This section summarizes the key outputs generated after running all three project code files (SQL, Python, and Verification SQL). You’ll see exactly what the pipeline produced, what the numbers mean, and how to interpret the results—so anyone reviewing the repo can quickly understand what the project delivers.

---

## 📈 Core Outputs

### 1. Record Counts and Table Creations
* **Raw Titanic Records:** 891 (full dataset ingested)
* **Train Records:** 713
* **Test Records:** 178
* **Tables Created:** 10+ (including all feature versions, Feature Store, and analytics)

### 2. Feature Engineering Results
* **Key Features Engineered:** `FAMILY_SIZE`, `IS_ALONE`, `HAS_CABIN`, `TITLE`, `CLASS_SURVIVAL_RATE`, `SEX_SURVIVAL_RATE`, `AGE_NORMALIZED`, `FARE_NORMALIZED`, and more.
* **Feature Store:** 8 features available for re-use and ML modeling.

### 3. Statistical Overview
* **Survival Rate:** 38.38% (342 of 891 survived)
* **Group Rates:** `Class Survival` and `Sex Survival` group rates produced for analytics/feature use.

---

## 🔗 Feature Correlation with Survival
This table shows how strongly each feature is associated with the actual Titanic survival outcome—the higher the value (closer to 1), the more predictive the feature is for survival.

| Feature | Correlation | Meaning |
| :--- | :--- | :--- |
| `SURVIVED` | 1.000 | Target variable itself (control/reference) |
| `SEX_SURVIVAL_RATE` | 0.543 | **Strongest predictor:** Gender group survival rate |
| `CLASS_SURVIVAL_RATE` | 0.340 | **Next strongest:** 1st/2nd class much more likely |
| `HAS_CABIN` | 0.317 | Has a cabin ticket linked with higher survival |
| `FARE_NORMALIZED` | 0.257 | Higher fare increases chance of survival |
| `FAMILY_SIZE` | 0.017 | Very little effect |
| `AGE_NORMALIZED` | -0.047 | Slight negative: younger slightly more likely |
| `IS_ALONE` | -0.203 | **Negative impact:** Those alone less likely to live |

*(Values as produced by the pipeline's correlation analysis)*

---

## 🎯 What Do These Results Mean?
* **Gender matters most:** The pipeline confirms, just like in real Titanic history, that sex (female/male) and passenger class are the biggest factors in survival.
* **Good Feature Engineering:** Your use of group-based engineered features (e.g., `SEX_SURVIVAL_RATE`, `CLASS_SURVIVAL_RATE`) are more predictive than raw columns by themselves.
* **Why this is correct:** These results closely match credible public analyses (e.g. Kaggle solutions), so you can trust the numbers and trends.

---

## 📑 Sample Table Snapshots
* **Features Table:** `FEATURES_BASIC`, `FEATURES_AGGREGATED` (891 records each)
* **Enhanced Python Features:** `FEATURES_PYTHON_ENHANCED` (adds `FAMILY_SIZE_SQUARED` and interaction features)
* **Train/Test Datasets:** `TRAIN_DATA_PYTHON` (713 rows), `TEST_DATA_PYTHON` (178 rows)
* **Correlations Table:** `FEATURE_CORRELATIONS_PYTHON` (8 rows: see table above)

---

## 📚 How to Verify in Snowflake
1.  Open your SQL worksheet.
2.  Run the provided `verify_project.sql` file to immediately see:
    * Table sizes
    * Feature store status
    * Sample enhanced features
    * Correlations and split statistics

---

## 📊 Example Output (from Snowflake Console)
```text
+----------------------+-------------+
|     FEATURE          | CORRELATION |
+----------------------+-------------+
| SURVIVED             |    1.000000 |
| SEX_SURVIVAL_RATE    |    0.543351 |
| CLASS_SURVIVAL_RATE  |    0.339817 |
| HAS_CABIN            |    0.316912 |
| FARE_NORMALIZED      |    0.257306 |
| FAMILY_SIZE          |    0.016639 |
| AGE_NORMALIZED       |   -0.047255 |
| IS_ALONE             |   -0.203367 |
+----------------------+-------------+

## ✅ Conclusion: Pipeline Integrity
1.  All pipeline outputs are accurate and verified.
2. Results match both Titanic dataset history and leading ML/data science workflows.
3. All SQL/Python deliverables create exactly the expected data tables and results.
4. Your features and splits are ready for ML modeling, reporting, or company demo.