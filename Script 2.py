#Script 2.py

# script2_analysis.py (Conceptual Python Code)

import pandas as pd

def analyze_and_output():
    """Loads data, performs momentum analysis, and prints the result."""
    try:
        # Step 1: Load data
        df = pd.read_csv('nifty50_stock_data.csv')
        
        # Step 2: Preprocess data
        df['Date'] = pd.to_datetime(df['Date']).dt.date
        df = df.sort_values(by=['Symbol', 'Date'])
        
        # Step 3: Calculate daily percentage change for each stock
        df['Prev_Close'] = df.groupby('Symbol')['Close'].shift(1)
        df.dropna(subset=['Prev_Close'], inplace=True) # Drop the first day of each stock's data
        df['Daily_Change_%'] = ((df['Close'] - df['Prev_Close']) / df['Prev_Close']) * 100
        
        # Step 4: Calculate average daily percentage change for each sector
        sector_momentum = df.groupby(['Date', 'Sector'])['Daily_Change_%'].mean().reset_index()
        
        # Step 5: Identify the sector with the highest momentum for each day
        highest_momentum_sectors = sector_momentum.loc[
            sector_momentum.groupby('Date')['Daily_Change_%'].idxmax()
        ].sort_values(by='Date', ascending=False)
        
        # Filter for only the last 5 unique trading days
        last_5_days = highest_momentum_sectors['Date'].unique()[:5]
        output_data = highest_momentum_sectors[highest_momentum_sectors['Date'].isin(last_5_days)]
        
        # Reverse the order to show Day 1, Day 2, etc. (chronological order)
        output_data = output_data.sort_values(by='Date', ascending=True).reset_index(drop=True)

        # Step 6: Print the output
        print("--- Sector Momentum Analysis ---")
        for i, row in output_data.iterrows():
            day_num = i + 1
            sector_name = row['Sector']
            avg_change = row['Daily_Change_%']
            print(f"Day {day_num}: {sector_name} ({avg_change:.2f}%)")
            
    except FileNotFoundError:
        print("Error: 'nifty50_stock_data.csv' not found. Please run Script 1 first.")
    except Exception as e:
        print(f"Critical error in Script 2: {e}")

if __name__ == "__main__":
    analyze_and_output()