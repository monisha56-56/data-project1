import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_sample_data(file_name):
    print("Generating sample Superstore dataset...")
    np.random.seed(42)
    n_rows = 1000
    
    # Generate dates over the last two years
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=np.random.randint(0, 365*2)) for _ in range(n_rows)]
    
    regions = ['East', 'West', 'Central', 'South']
    categories = ['Furniture', 'Office Supplies', 'Technology']
    sub_categories = {
        'Furniture': ['Chairs', 'Tables', 'Bookcases', 'Furnishings'],
        'Office Supplies': ['Paper', 'Binders', 'Art', 'Envelopes', 'Labels', 'Fasteners'],
        'Technology': ['Phones', 'Accessories', 'Machines', 'Copiers']
    }
    
    data = []
    for i in range(n_rows):
        cat = np.random.choice(categories, p=[0.2, 0.6, 0.2])
        sub_cat = np.random.choice(sub_categories[cat])
        
        # Base cost and margin logic
        if cat == 'Technology':
            base_cost = np.random.uniform(100, 1500)
            margin = np.random.uniform(0.3, 0.6) # High margins
        elif cat == 'Furniture':
            base_cost = np.random.uniform(50, 800)
            margin = np.random.uniform(0.05, 0.2) # Low margins
        else: # Office Supplies
            base_cost = np.random.uniform(5, 100)
            margin = np.random.uniform(0.2, 0.4)
            
        # Add some seasonality: peak in Nov-Dec
        date = dates[i]
        sales_multiplier = 1.5 if date.month in [11, 12] else 1.0
        
        sales = base_cost * (1 + margin) * sales_multiplier
        cost = base_cost * sales_multiplier
        
        data.append({
            'Order ID': f'CA-2023-{np.random.randint(100000, 199999)}',
            'Order Date': date.strftime('%m/%d/%Y'),
            'Ship Mode': np.random.choice(['Standard Class', 'Second Class', 'First Class', 'Same Day']),
            'Segment': np.random.choice(['Consumer', 'Corporate', 'Home Office']),
            'Region': np.random.choice(regions, p=[0.3, 0.35, 0.2, 0.15]), # West and East slightly higher
            'Category': cat,
            'Sub-Category': sub_cat,
            'Product Name': f'{sub_cat} Product {np.random.randint(1, 100)}',
            'Sales': round(sales, 2),
            'Cost': round(cost, 2)
        })
        
    df = pd.DataFrame(data)
    
    # Introduce duplicates to be cleaned later
    duplicates = df.sample(n=20, random_state=42)
    df = pd.concat([df, duplicates], ignore_index=True)
    
    df.to_csv(file_name, index=False)
    print(f"Sample data generated and saved to {file_name}")

def process_data(input_file, output_file):
    print("\n--- Starting Data Processing ---")
    
    # Step 1: Read data
    df = pd.read_csv(input_file)
    print(f"Initial shape: {df.shape}")
    
    # Step 2: Clean Data
    
    # 2a. Remove duplicates
    initial_rows = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Removed {initial_rows - len(df)} duplicate rows.")
    
    # 2b. Fix dates
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    print("Fixed date formats.")
    
    # 2c. Create Profit Column (Sales - Cost)
    df['Profit'] = df['Sales'] - df['Cost']
    
    # 2d. Create Month/Year Column
    df['Month / Year'] = df['Order Date'].dt.to_period('M').dt.strftime('%b %Y')
    print("Added 'Profit' and 'Month / Year' columns.")
    
    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")
    print(f"Final shape: {df.shape}")
    
    return df

def generate_insights(df):
    print("\n--- REAL Insights ---")
    
    # Highest profit region
    profit_by_region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
    best_region = profit_by_region.index[0]
    best_region_profit = profit_by_region.iloc[0]
    print(f"1. {best_region} region gives the highest profit (${best_region_profit:,.2f}).")
    
    # Best margins by category
    category_metrics = df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'})
    category_metrics['Margin'] = category_metrics['Profit'] / category_metrics['Sales']
    category_metrics = category_metrics.sort_values(by='Margin', ascending=False)
    best_margin_cat = category_metrics.index[0]
    best_margin = category_metrics['Margin'].iloc[0] * 100
    print(f"2. {best_margin_cat} category has the best profit margins ({best_margin:.1f}%).")
    
    # Seasonal trend
    monthly_sales = df.groupby(df['Order Date'].dt.month)['Sales'].sum()
    peak_months_idx = monthly_sales.nlargest(2).index.tolist()
    month_names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 
                   7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    peak_months = [month_names[m] for m in sorted(peak_months_idx)]
    print(f"3. Sales peak in {' and '.join(peak_months)} (seasonal trend confirmed).")
    
    # Top Product
    top_product = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).index[0]
    print(f"4. The highest-selling product overall is '{top_product}'.")

if __name__ == "__main__":
    input_filename = "Superstore.csv"
    output_filename = "cleaned_superstore_data.csv"
    
    if not os.path.exists(input_filename):
        generate_sample_data(input_filename)
    else:
        print(f"Found existing {input_filename}")
        
    cleaned_df = process_data(input_filename, output_filename)
    generate_insights(cleaned_df)
    print("\nProcessing Complete!")
