# Exploratory Data Analysis (EDA) — Retail Sales

## Project Overview
This beginner-friendly project performs Exploratory Data Analysis on a retail sales dataset.

## Objectives
- Inspect the dataset structure
- Identify missing values and duplicate records
- Clean the data
- Generate descriptive statistics
- Analyze sales by product and region
- Study relationships between sales and business variables
- Create clear visualizations

## Dataset
The dataset is synthetic and created for educational/internship demonstration.

Columns:
- Date
- Product
- Region
- Customers
- Marketing_Spend
- Discount_Percent
- Avg_Product_Price
- Sales

## EDA Workflow
1. Load the dataset
2. Check shape, data types and missing values
3. Detect and remove duplicates
4. Fill missing numeric values using the median
5. Calculate descriptive statistics
6. Perform group-by analysis
7. Analyze correlations
8. Create visualizations
9. Save cleaned data and summary files

## Results
- Original rows: 121
- Rows after removing duplicates: 120
- Total sales: 319,257,470.18
- Average sales record: 2,660,478.92
- Highest-sales product: Laptop
- Highest-sales region: West

## How to Run
```bash
pip install -r requirements.txt
python src/eda_analysis.py
```

For the notebook:
```bash
jupyter notebook
```

Then open `notebooks/retail_sales_eda.ipynb`.

## Folder Structure
- `data/` — raw, cleaned and summary datasets
- `src/` — Python EDA script
- `notebooks/` — Jupyter notebook
- `visualizations/` — generated charts
- `requirements.txt` — required Python libraries
