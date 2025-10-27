<p align="center"> <img src="https://media.giphy.com/media/26xBzvH6sDLHbOZYU/giphy.gif" alt="Data Engineering GIF" width="600"/> </p> <h1 align="center">📊 Investing.com Stock Data Scraper</h1> <p align="center"> <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white"></a> <a href="https://www.selenium.dev/"><img src="https://img.shields.io/badge/Selenium-Automation-informational"></a> <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/Pandas-Data%20Frames-yellowgreen"></a> <a href="#"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a> <a href="#"><img src="https://img.shields.io/badge/Made%20by-Mat%C3%ADas%20Kostiak-black"></a> </p>

A professional and minimalist scraper that extracts Current Price, Daily Change (%), Volume, and Day’s Range from Investing.com
 using Selenium (headless) and WebDriver Manager, saving the results into a clean CSV file.

✨ Features

Handles dynamic JavaScript content via WebDriverWait

Runs headless (no visible browser)

Uses webdriver-manager for automatic driver installation

Built-in timeout & error handling

Outputs a ready-to-use CSV

🧰 Tech Stack

Python 3.8+, Selenium, Pandas, WebDriver Manager, Google Chrome

🚀 Installation

Create and activate a virtual environment

python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate


Install dependencies

pip install -r requirements.txt

⚙️ Usage
python scraper.py


The script will:

Launch a headless Chrome browser

Navigate to the defined TARGET_URL

Wait dynamically for required elements

Extract key financial metrics

Save results to investing_data_output.csv

Close the browser automatically

🧩 Configuration

To scrape another stock page, edit the configuration at the top of scraper.py:

# --- 1. CONFIGURATION ---
TARGET_URL = "https://es.investing.com/equities/YOUR-NEW-STOCK-URL-HERE"
OUTPUT_FILE = "investing_data_output.csv"
WAIT_TIMEOUT = 10

📤 Output Example
Current_Price	Daily_Change_Percent	Volume	Day_Range
213.07	+0.17%	27.94M	264.65 - 267.76

Example data only. Actual values depend on stock locale and real-time market.

🧠 Best Practices

Use a VPN or stable connection to prevent temporary IP blocks

If site structure changes, update CSS/XPath selectors

For multiple tickers, loop through URLs and append results to the same CSV

🧪 Key Selectors
price        = '[data-test="instrument-price-last"]'
change_pct   = '[data-test="instrument-price-change-percent"]'
volume_xpath = "//dt[text()='Volumen']/following-sibling::dd[1]"
range_xpath  = "//dt[text()='Rango día']/following-sibling::dd[1]"

🧱 Folder Structure
projects/investing_basic_scraper/
├── scraper.py
├── requirements.txt
└── README.md

⚠️ Disclaimer

This project is for educational purposes only.
Always review and comply with Investing.com’s Terms of Use before using scraped data for production or commercial use.

👤 Author

Matías Kostiak
💼 Data Engineer | Python Automation & Web Scraping Specialist
📧 matiaskostiak25@gmail.com

🌎 Paraguay
🔗 GitHub
 • LinkedIn
 • Upwork
