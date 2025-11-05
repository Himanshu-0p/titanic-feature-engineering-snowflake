# Titanic Dataset Information

## Source
**Kaggle:** https://www.kaggle.com/datasets/yasserh/titanic-dataset

## Dataset Statistics

| Property | Value |
|----------|-------|
| **Records** | 891 |
| **Features** | 12 |
| **Target** | Survived (0/1) |
| **File Size** | ~61 KB |
| **Format** | CSV |

## Columns

| Column | Type | Description | Missing |
|--------|------|-------------|---------|
| PassengerId | Integer | Unique passenger ID | 0% |
| Survived | Integer | Target (0=No, 1=Yes) | 0% |
| Pclass | Integer | Ticket class (1/2/3) | 0% |
| Name | String | Passenger name | 0% |
| Sex | String | Gender (male/female) | 0% |
| Age | Float | Age in years | 20% |
| SibSp | Integer | Siblings/Spouses | 0% |
| Parch | Integer | Parents/Children | 0% |
| Ticket | String | Ticket number | 0% |
| Fare | Float | Ticket price | 0% |
| Cabin | String | Cabin number | 77% |
| Embarked | String | Port (C/Q/S) | 0.2% |

## Distribution

- **Survived: 342 (38.38%)**
- **Did Not Survive: 549 (61.62%)**

## How to Download

1. Visit: https://www.kaggle.com/datasets/yasserh/titanic-dataset
2. Click "Download"
3. Extract `train.csv` (this is the dataset we use)
4. Upload to Snowflake stage

## Data Quality
- ~20% missing Age values (handled via median imputation)
- ~77% missing Cabin values (converted to Has_Cabin flag)
- Minimal missing values in other columns

## Size & Format
- Records: 891
- File: CSV format
- Size: ~61 KB
- Ready for ML processing after feature engineering
