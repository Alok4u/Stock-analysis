# Stock-analysis
This repository contains the solution for a machine coding challenge focused on analyzing the volatility and performance of NIFTY 50 stocks to identify sector-wise momentum. The entire solution is self-contained within two Python scripts.
## 📝 Project Description: Indian Stock Market Sector Momentum Analysis

This repository contains the solution for a machine coding challenge focused on analyzing the volatility and performance of **NIFTY 50** stocks to identify sector-wise momentum. The entire solution is self-contained within two Python scripts.

---

### 🎯 Task & Objective

The primary objective was to non-hardcode the fetching of NIFTY 50 constituents and their historical data, and then apply business logic to determine the leading sector based on average daily percentage change for the last five trading sessions.

### 💻 Technical Implementation Details

The solution is divided into two parts as required:

#### 1. Script 1: Data Fetching (`script1_data_fetch.py`)

* **Data Source:** The script utilizes the **NSE India API endpoints** (via the `nsepython` library) and a robust **CSV fallback mechanism** to ensure the list of NIFTY 50 symbols and their corresponding sectors are dynamically retrieved, **not hardcoded**.
* **Data Retrieved:** Daily Open, High, Low, and Close prices for the **last 5 trading sessions** for all NIFTY 50 stocks.
* **Output:** Saves the consolidated stock, sector, and price data to a file named `nifty50_stock_data.csv`.
* **Robustness:** Includes **error handling** and a fallback routine to mitigate potential API or JSON structure changes.

#### 2. Script 2: Analysis & Output (`script2_analysis.py`)

* **Calculation:**
    * Calculates the **Daily Percentage Change** for every stock.
    * Groups the data by **Date** and **Sector**.
    * Calculates the **Average Daily Percentage Change** for each sector.
* **Momentum Identification:** Identifies the single sector with the **highest average momentum** (highest average daily percentage change) for each of the last five trading days.
* **Final Output:** Prints the final results to the console in the specified format.

---

### ⚙️ How to Run the Code

1.  **Dependencies:** Ensure Python 3 is installed. Install required packages:
    ```bash
    pip install nsepythonserver pandas
    ```
2.  **Step 1: Fetch Data** (Creates the necessary CSV file)
    ```bash
    python script1_data_fetch.py
    ```
3.  **Step 2: Analyze Data** (Prints the final momentum report)
    ```bash
    python script2_analysis.py
    ```
---

### ✅ Result 

Sector Momentum Analysis (Last 5 Trading Days) 🚀 --- Day 1: Oil & Gas (-0.95%) Day 2: Oil & Gas (-0.96%) Day 3: Oil & Gas (-0.97%) Day 4: Oil & Gas (-0.98%)
