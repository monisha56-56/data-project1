# E-commerce Sales Analysis Project

This repository contains an end-to-end data analysis project demonstrating data manipulation with Python and visual dashboarding with Power BI.

## Overview
1. **Get Data**: The dataset used is the Superstore Sales Dataset.
2. **Clean Data**: Cleaned using a Python script (`process_data.py`) which:
   - Removes duplicates.
   - Fixes date formats.
   - Calculates `Profit = Sales - Cost`.
   - Creates a new `Month / Year` column.
3. **Build Dashboard**: Includes a Power BI dashboard with 5 critical visualizations.
4. **REAL Insights**: Actionable business intelligence derived directly from the dataset.

---

## The Dashboard (Power BI)

*Placeholder for your dashboard screenshot*
> **Tip:** After building your dashboard, take a screenshot, name it `dashboard.png`, upload it here, and replace this text with `![Dashboard](dashboard.png)`.

### How to Build the Dashboard in Power BI
If you want to recreate this dashboard, follow these steps:

1. **Import the Data**:
   - Open Power BI Desktop.
   - Click **Get Data** -> **Text/CSV**.
   - Select the `cleaned_superstore_data.csv` file from this folder.
   - Click **Load**.

2. **Create the Visuals**:
   - **Total Sales**: Add a "Card" visual. Drag `Sales` into the Fields.
   - **Total Profit**: Add another "Card" visual. Drag `Profit` into the Fields.
   - **Sales by Region**: Add a "Pie Chart" or "Donut Chart". Put `Region` in Legend and `Sales` in Values.
   - **Top 10 Products**: Add a "Clustered Bar Chart". Put `Product Name` in the Y-axis and `Sales` in the X-axis. In the Filters pane for `Product Name`, set Filter Type to "Top N", show top 10 by `Sales` value, and apply.
   - **Monthly Trend**: Add a "Line Chart". Put `Order Date` (or `Month / Year`) on the X-axis and `Sales` on the Y-axis.

---

## 💡 REAL Insights Discovered

Based on our analysis of the dataset, here are the key findings:

- **"West region gives the highest profit"**: The West generated the most profit overall ($36,098.67).
- **"Technology category has best margins"**: The Technology sector demonstrated the most efficient profitability with an average profit margin of 31.1%.
- **"Sales peak in January and November (seasonal trend)"**: We see distinct spikes in purchasing behavior during these specific months.
- **Top Product**: The single highest-grossing item across the dataset was **'Phones Product 51'**.

---

## Files in this Repository
- `Superstore.csv` - The raw data.
- `process_data.py` - The Python script used to clean the data and generate the insights.
- `cleaned_superstore_data.csv` - The final dataset, ready for Power BI.
- `README.md` - Project documentation.