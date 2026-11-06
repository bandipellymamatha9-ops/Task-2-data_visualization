# Superstore Sales Data Visualization and Storytelling

## Project Overview
This project analyses a sample Superstore-style sales dataset using Python. It creates charts and business insights to explain sales trends, product category performance, regional performance, and the relationship between discounts and profit.

## Objective
To turn sales data into clear visualizations and useful business recommendations.

## Dataset
- File: `superstore_sales.csv`
- Records: 576
- Period: January 2024 to December 2025
- Main columns: Order_Date, Region, Category, Sub_Category, Segment, Quantity, Discount, Sales, Profit

This is a sample dataset created for this project. It is not an official company dataset.

## Tools and Libraries
- Python
- Pandas
- Matplotlib
- Pydroid 3 (Android) or any Python environment

## Project Files
- `superstore_sales.csv` — dataset used for the analysis.
- `superstore_visualization.py` — Python script that analyses the dataset and generates charts.
- `requirements.txt` — required Python libraries.
- `README.md` — project documentation.

## How to Run
1. Download or clone this repository.
2. Keep `superstore_sales.csv` and `superstore_visualization.py` in the same folder.
3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Python script:

   ```bash
   python superstore_visualization.py
   ```

5. Open the `visualization_output` folder created by the script.

### Running in Pydroid 3
1. Download all project files to the same folder on your phone.
2. Install `pandas` and `matplotlib` using Pydroid 3's Pip menu.
3. Open `superstore_visualization.py` in Pydroid 3 and tap Run.
4. Find the generated charts and report in `visualization_output`.

## Visualizations Generated
1. `01_monthly_sales_trend.png` — monthly sales trend.
2. `02_category_performance.png` — sales and profit by product category.
3. `03_regional_sales.png` — sales by region.
4. `04_discount_vs_profit.png` — relationship between discount and profit.
5. `05_kpi_dashboard.png` — key performance indicator dashboard.

The script also creates `business_insights.txt`, which summarizes findings and recommendations.

## Key Questions Explored
- Which month had the highest sales?
- Which product category generated the highest sales?
- Which region recorded the highest sales?
- How are discounts related to profit?
- What actions could help improve business performance?

## Conclusion
The project uses visual storytelling to communicate patterns in sales and profitability. It highlights the importance of reviewing both revenue and profit before making business decisions.
