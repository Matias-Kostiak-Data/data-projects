
# 📊 Investing.com Stock Data Scraper

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-informational)](https://www.selenium.dev/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Frames-yellowgreen)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Made by](https://img.shields.io/badge/Made%20by-Mat%C3%ADas%20Kostiak-black)](#-author)

A clean and professional Python scraper that extracts **current price, daily change, volume, and day range** from any stock page on **Investing.com**.  
It uses **Selenium (headless)** and **WebDriver Manager** to handle JavaScript-rendered content and saves everything in a **structured CSV file**.

---

## ✨ Features

- **Dynamic rendering support:** waits for JavaScript content with `WebDriverWait`.  
- **Headless operation:** runs without opening a visible browser window.  
- **Auto driver management:** `webdriver-manager` installs the right ChromeDriver automatically.  
- **Robust error handling:** safely skips missing or slow elements.  
- **Clean output:** exports a single-row CSV ready for data analysis.

---

## 🧰 Technology Stack

- **Python 3.8+**
- **Selenium**
- **Pandas**
- **Webdriver-Manager**
- **Google Chrome**

---

## 🚀 Installation


# 1. Create and activate a virtual environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt


⚙️ Usage
bash
Copiar código
python scraper.py

The script will:

Configure and launch a headless Chrome browser.

Navigate to the defined TARGET_URL.

Wait dynamically for page elements to load.

Extract 4 key stock metrics.

Save the data to investing_data_output.csv.

Close the browser automatically.

🧩 Configuration
Edit the configuration section at the top of scraper.py to scrape another stock:

# --- 1. CONFIGURATION ---
TARGET_URL = "https://es.investing.com/equities/YOUR-NEW-STOCK-URL-HERE"
OUTPUT_FILE = "investing_data_output.csv"
WAIT_TIMEOUT = 10

📤 Output Example
Current_Price	Daily_Change_Percent	Volume	Day_Range
213.07	+0.17%	27.94M	264.65 - 267.76

Example data only. Actual values depend on the stock locale and real-time market conditions.

🧠 Best Practices
Use a VPN or stable network to avoid temporary IP blocks.

If the page structure changes, update CSS or XPath selectors.

For multiple tickers, loop over URLs and append results to the same CSV.

🧪 Key Selectors (reference)

price        = '[data-test="instrument-price-last"]'
change_pct   = '[data-test="instrument-price-change-percent"]'
volume_xpath = "//dt[text()='Volumen']/following-sibling::dd[1]"
range_xpath  = "//dt[text()='Rango día']/following-sibling::dd[1]"

🧱 Folder Structure

projects/investing_basic_scraper/
├── scraper.py
├── requirements.txt
└── README.md

⚠️Disclaimer
This project is for educational purposes only.
Always review and comply with Investing.com’s Terms of Use before using scraped data for production or commercial purposes.

👤 Author
Matías Kostiak
💼 Data Engineer | Python Automation & Web Scraping Specialist
📧 matiaskostiak25@gmail.com
🌎 Paraguay
🔗 GitHub | LinkedIn | Upwork



