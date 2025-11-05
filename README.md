# Titanic Vistara Project - Feature Engineering with Snowflake

![GitHub](https://img.shields.io/badge/GitHub-Titanic%20Vistara-blue)
![Snowflake](https://img.shields.io/badge/Snowflake-SQL%20%26%20Python-5DADE2)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## 📋 Project Overview

This project demonstrates a complete **feature engineering pipeline** for the Titanic dataset using **Snowflake** and **Feature Stores**. The goal is to predict passenger survival by transforming raw data into meaningful features through multiple engineering stages.

**Assignment:** Vistora AI - AI/ML Feature Engineering with Snowflake

---

## 📊 Dataset

**Source:** [Kaggle - Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)

**Details:**
- **Records:** 891 passengers
- **Features:** 12 columns (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)
- **Target Variable:** Survived (0 = No, 1 = Yes)
- **Survival Rate:** 38.38%

**Download:**
https://www.kaggle.com/datasets/yasserh/titanic-dataset


---

## 🏗️ Architecture & Technology Stack

### Technologies Used
| Component | Technology |
|-----------|-----------|
| **Database** | Snowflake |
| **Data Processing** | SQL, Snowpark Python |
| **Feature Store** | Snowflake Feature Store |
| **Languages** | SQL, Python 3.11 |
| **Libraries** | pandas, numpy, scikit-learn |

### Infrastructure

Raw Data (CSV)
↓
Snowflake RAW_TITANIC Table
↓
Feature Engineering Pipeline (6 stages)
├── FEATURES_BASIC
├── FEATURES_AGGREGATED
├── FEATURES_CLEANED
├── FEATURES_ENCODED
└── FEATURES_NORMALIZED
↓
Feature Store
↓
Train/Test Data Ready for ML


---

## 📂 Project Structure

### **SQL Pipeline** (`SQL/titanic_vistara_sql.sql`)
Complete SQL implementation with 10 steps:

| Step | Table | Purpose |
|------|-------|---------|
| 1 | RAW_TITANIC | Load CSV data (891 records) |
| 2 | FEATURES_BASIC | Create basic features (Family Size, Title, Cabin) |
| 3 | FEATURES_AGGREGATED | Add group statistics (Class/Sex survival rates) |
| 4 | FEATURES_CLEANED | Handle missing values (Age, Fare, Embarked) |
| 5 | FEATURES_ENCODED | Convert text to numbers (One-hot encoding) |
| 6 | FEATURES_NORMALIZED | Z-score normalization |
| 7 | FEATURE_STORE | Centralized feature repository (8 features) |
| 8 | FEATURE_RETRIEVAL (VIEW) | Retrieve features from store |
| 9 | TRAIN_DATA | 80% training data (713 records) |
| 10 | TEST_DATA | 20% test data (178 records) |

### **Python Pipeline** (`PYTHON/titanic_vistara_python.py`)
Snowpark Python implementation with 12 steps:

| Step | Purpose |
|------|---------|
| 1 | Load normalized features |
| 2 | Create additional features |
| 3 | Save enhanced features |
| 4 | Compute statistics |
| 5 | Create train/test split |
| 6 | Save train/test data |
| 7 | Feature analysis (Class/Sex) |
| 8 | Retrieve from Feature Store |
| 9 | Convert to Pandas |
| 10 | Compute correlations |
| 11 | Save correlations |
| 12 | Summary statistics |

---

## 🎯 Feature Engineering Techniques

### **1. Feature Creation**
- `FAMILY_SIZE` = SibSp + Parch + 1
- `IS_ALONE` = (SibSp + Parch == 0)
- `HAS_CABIN` = (CABIN IS NOT NULL)
- `TITLE` = Extracted from Name field

### **2. Aggregated Features**
- `CLASS_SURVIVAL_RATE` - Avg survival by passenger class
- `SEX_SURVIVAL_RATE` - Avg survival by gender
- `TITLE_SURVIVAL_RATE` - Avg survival by title
- `CLASS_AVG_FARE` - Avg fare by class

### **3. Encoding**
- **One-Hot Encoding:** Sex, Embarked, Title, Pclass
- **Binary Encoding:** Is_Alone, Has_Cabin

### **4. Normalization**
- **Z-Score:** (X - Mean) / Std Dev
- Applied to: Age, Fare, Family Size

### **5. Feature Interactions**
- `FAMILY_SIZE_SQUARED` = Family Size²
- `AGE_FARE_INTERACTION` = Age × Fare
- `HIGH_CLASS_MALE` = (Pclass=1 AND Sex=Male)

---

## 📊 Key Findings

### **Feature Correlations with Survival**

| Feature | Correlation | Strength |
|---------|-------------|----------|
| **SEX_SURVIVAL_RATE** | 0.543 | ⭐⭐⭐⭐⭐ **STRONGEST** |
| **CLASS_SURVIVAL_RATE** | 0.334 | ⭐⭐⭐⭐ |
| **HAS_CABIN** | 0.317 | ⭐⭐⭐⭐ |
| **FARE_NORMALIZED** | 0.257 | ⭐⭐⭐ |
| **FAMILY_SIZE** | 0.017 | ⭐ |
| **AGE_NORMALIZED** | -0.047 | ⭐ Negative |
| **IS_ALONE** | -0.203 | ⭐⭐ Negative |

### **Survival Insights**
- **Most Important:** Gender (sex) is the strongest predictor
- **Second:** Passenger class matters significantly
- **Third:** Cabin information availability
- **Age Effect:** Younger passengers slightly more likely to survive
- **Traveling Alone:** Reduces survival chances

### **Dataset Statistics**
- Total Records: 891
- Training Data: 713 (80%)
- Test Data: 178 (20%)
- Survived: 342 (38.38%)
- Did Not Survive: 549 (61.62%)

---

## 🚀 How to Run

### **Prerequisites**
- Snowflake account
- SQL Worksheet access
- Python Worksheet access
- CSV file: `Titanic-Dataset.csv`

### **SQL Pipeline**

1. **Open Snowflake SQL Worksheet**
   - Go to: **Worksheets** → **+ SQL Worksheet**

2. **Set Context**
   - Database: `TITANIC_VISTARA_PROJECT`
   - Schema: `FEATURES`
   - Warehouse: `COMPUTE_WH`

3. **Upload Dataset**
   - Data → Databases → TITANIC_VISTARA_PROJECT → FEATURES → Stages → DATA_STAGE → Upload Files
   - Select: `Titanic-Dataset.csv`

4. **Run SQL Code**
   - Copy code from `SQL/titanic_vistara_sql.sql`
   - Paste into SQL Worksheet
   - Click: **Run All**

### **Python Pipeline**

1. **Open Snowflake Python Worksheet**
   - Go to: **Worksheets** → **+ Python Worksheet**

2. **Set Context** (same as SQL)

3. **Run Python Code**
   - Copy code from `PYTHON/titanic_vistara_python.py`
   - Paste into Python Worksheet
   - Click: **Run**

### **Verification**

Run SQL verification queries:
-- From SQL/verify_project.sql
SELECT * FROM FEATURE_CORRELATIONS_PYTHON ORDER BY CORRELATION DESC;


---

## 📋 Files & Descriptions

### **SQL Files**
- **`titanic_vistara_sql.sql`** - Complete 10-step SQL pipeline
- **`verify_project.sql`** - Verification and testing queries

### **Python Files**
- **`titanic_vistara_python.py`** - Complete 12-step Snowpark pipeline

### **Documentation**
- **`PROJECT_SUMMARY.md`** - Detailed project metrics
- **`FEATURE_ANALYSIS.md`** - Feature engineering details
- **`ARCHITECTURE.md`** - System design and flow
- **`DATASET_INFO.md`** - Dataset specifications

---

## 🎓 Learning Outcomes

After this project, you will understand:

1. **Feature Engineering Techniques**
   - Normalization & Scaling
   - Encoding & Transformation
   - Aggregation & Composition
   - Feature Interactions

2. **Snowflake Capabilities**
   - Data ingestion via stages
   - SQL transformations
   - Window functions
   - Feature store patterns

3. **Snowpark Python**
   - Snowpark DataFrame operations
   - Integration with Snowflake
   - Feature computation in Python

4. **ML Preparation**
   - Train/test data splitting
   - Correlation analysis
   - Feature importance assessment

---

## 📊 Project Metrics

| Metric | Value |
|--------|-------|
| **Total Records** | 891 |
| **Training Records** | 713 (80%) |
| **Test Records** | 178 (20%) |
| **Tables Created** | 11 |
| **Features in Store** | 8 |
| **Feature Engineering Stages** | 6 |
| **Survival Rate** | 38.38% |
| **Primary Predictor** | Sex (0.543) |

---

## 🔗 Connections & Integrations

### **Snowflake**
- **Database:** TITANIC_VISTARA_PROJECT
- **Schema:** FEATURES
- **Warehouse:** COMPUTE_WH
- **File Format:** CSV_FORMAT
- **Stage:** DATA_STAGE

### **Data Pipeline**
CSV → Snowflake Stage → RAW_TITANIC → Feature Engineering → Feature Store


---

## 📚 References

### **Kaggle Dataset**
- [Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)

### **Snowflake Documentation**
- [Snowflake Feature Store](https://docs.snowflake.com/en/user-guide/ml-functions)
- [Snowpark Python](https://docs.snowflake.com/en/developer-guide/snowpark/python)
- [SQL Reference](https://docs.snowflake.com/en/sql-reference)

### **Feature Engineering**
- Feature scaling & normalization techniques
- Categorical encoding methods
- Statistical aggregations

---

## ✅ Project Checklist

- [x] Raw data loaded (891 records)
- [x] Feature engineering pipeline (6 stages)
- [x] Feature store created (8 features)
- [x] Missing values handled
- [x] Features normalized
- [x] Train/test split (80/20)
- [x] Correlation analysis completed
- [x] SQL code tested and verified
- [x] Python code tested and verified
- [x] Documentation complete

---

## 👨‍💻 Author & Contact

**Project:** Titanic Vistara - Feature Engineering with Snowflake  
**Assignment:** Vistora AI - AI/ML Engineering  
**Date:** November 2025

---

## 📄 License

This project is for educational and assignment purposes.

---

## 🎉 Summary

This project successfully demonstrates:
- ✅ Complete feature engineering pipeline
- ✅ Snowflake integration and usage
- ✅ Feature store implementation
- ✅ Data transformation best practices
- ✅ ML-ready dataset preparation

**Status:** ✅ **COMPLETE AND READY FOR PRODUCTION**

---

For more details, see individual documentation files in `DOCS/` folder.
