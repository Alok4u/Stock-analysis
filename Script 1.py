#Script 1.py



# script1_data_fetch.py (Conceptual Python Code)

import pandas as pd
import datetime as dt
# Assuming a library like 'nselib' or 'yfinance' is installed
# If using pure scraping, replace this with 'requests' and 'BeautifulSoup'

def fetch_nifty50_data():
    """Fetches NIFTY 50 stocks list, sectors, and 5-day OHL-C data."""
    try:
        # Step 1: Fetch NIFTY 50 Symbols and Sectors (Do not hardcode)
        # --- Placeholder for list and sector fetching logic ---
        # Example using a placeholder dictionary (MUST be replaced with live scraping):
        nifty_stocks_list = [
            {'Symbol': 'RELIANCE', 'Sector': 'Oil & Gas'},
            {'Symbol': 'HDFCBANK', 'Sector': 'Private Banks'},
            # ... all 50 stocks
        ]
        
        # Step 2: Calculate date range (last 5 trading days)
        end_date = dt.date.today()
        # You'd need a more robust way to get 5 *trading* days,
        # but for a challenge, a simple offset can be a starting point.
        start_date = end_date - dt.timedelta(days=10) # Safe buffer for 5 trading days

        all_stocks_data = []
        for stock_info in nifty_stocks_list:
            symbol = stock_info['Symbol']
            sector = stock_info['Sector']
            
            try:
                # Step 3: Fetch historical data for the stock (placeholder for data library)
                # Example: Fetch daily data for symbol from start_date to end_date
                # data = fetch_historical_data(symbol, start_date, end_date) 
                
                # --- Placeholder for fetched daily data for the last 5 days ---
                # A pandas DataFrame is ideal: [Date, Open, High, Low, Close]
                
                # Filter to the actual last 5 trading days and extract OHL-C
                # data = data.tail(5) 

                # For simulation purposes:
                data = pd.DataFrame({
                    'Date': [end_date - dt.timedelta(days=i) for i in range(1, 6)],
                    'Open': [100.0, 101.0, 102.0, 103.0, 104.0],
                    'High': [102.0, 103.0, 104.0, 105.0, 106.0],
                    'Low': [99.0, 100.0, 101.0, 102.0, 103.0],
                    'Close': [101.5, 102.5, 103.5, 104.5, 105.5]
                })

                data['Symbol'] = symbol
                data['Sector'] = sector
                all_stocks_data.append(data)
                
            except Exception as e:
                print(f"Error fetching data for {symbol}: {e}")
                continue # Continue to the next stock on failure

        if not all_stocks_data:
            print("Failed to fetch data for any stock.")
            return

        final_df = pd.concat(all_stocks_data, ignore_index=True)
        # Step 4: Save data to a file for Script 2
        final_df.to_csv('nifty50_stock_data.csv', index=False)
        print("Data fetch successful. Saved to 'nifty50_stock_data.csv'")

    except Exception as e:
        print(f"Critical error in Script 1: {e}")

if __name__ == "__main__":
    fetch_nifty50_data()