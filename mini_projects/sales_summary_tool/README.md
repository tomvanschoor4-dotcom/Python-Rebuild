# Sales Summary Tool

A simple Python project that reads sales data from a CSV file, calculates revenue, summarizes performance by product, and exports the results to a new CSV.

## What it does
- Reads `sales.csv`
- Creates a revenue column using price × quantity
- Groups sales by product
- Sums revenue and units sold
- Sorts products by highest revenue
- Exports a clean summary to `sales_summary.csv`

## Files
- `main.py` → main analysis script
- `sales.csv` → input data
- `sales_summary.csv` → exported summary output

## Skills used
- Python
- pandas
- CSV file handling
- groupby aggregation
- sorting and exporting data

## How to run
```bash
python main.py