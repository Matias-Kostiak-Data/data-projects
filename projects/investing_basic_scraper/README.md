# 📊 Investing.com Stock Data Scraper

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-informational)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Frames-yellowgreen)
![License](https://img.shields.io/badge/License-MIT-green)
![Made with Love](https://img.shields.io/badge/Made%20with-❤️-ff69b4)
![Author](https://img.shields.io/badge/Author-Matías%20Kostiak-black)

A **clean, professional, and fully automated** Python scraper for [Investing.com](https://www.investing.com), built to extract real-time stock data with reliability and precision.  
It leverages **Selenium** for dynamic JavaScript handling, **WebDriver Manager** for seamless driver setup, and **Pandas** for exporting clean CSV output.

---

## ✨ Features

- 🧠 **Dynamic Content Handling:** Extracts data from JavaScript-rendered pages using Selenium + WebDriverWait.  
- 🕶️ **Headless Operation:** Runs quietly in the background without opening a browser window.  
- ⚙️ **Automatic Driver Management:** Installs and manages ChromeDriver automatically.  
- 🛡️ **Robust Error Handling:** Gracefully manages missing or delayed elements.  
- 📁 **Clean CSV Output:** Saves extracted data in a structured and ready-to-analyze format.

---

## 📈 Data Extracted

This scraper is pre-configured to capture the following **key financial metrics**:

| Metric | Description |
| ------- | ------------ |
| 💰 **Current Price** | Latest stock price in real time |
| 📉 **Daily Change (%)** | Percentage variation in the current session |
| 🔁 **Volume** | Total traded volume for the day |
| 📊 **Day's Range** | Minimum and maximum prices reached during the day |

---

## 🧰 Tech Stack

| Tool | Purpose |
| ---- | -------- |
| 🐍 **Python 3** | Main programming language |
| 🌐 **Selenium** | Web automation and dynamic scraping |
| 📦 **Pandas** | Data manipulation and CSV export |
| 🧩 **Webdriver-Manager** | ChromeDriver installation and management |

---

## 🚀 Setup & Installation

### 1️⃣ Prerequisites

Make sure you have the following installed:

- **Python 3.8+**
- **Google Chrome**

---

### 2️⃣ Clone or Download the Project

Clone this repository (or download the files directly):

git clone [YOUR_REPOSITORY_URL_HERE]
cd [YOUR_PROJECT_DIRECTORY_NAME]
# 3️⃣ Create a Virtual Environment (Recommended)
python -m venv venv

# Activate it
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4️⃣ Install Dependencies
pip install -r requirements.txt

# ⚙️ Usage
python scraper.py

# The script will:
# 1. Configure and launch a headless Chrome browser.
# 2. Navigate to the defined TARGET_URL.
# 3. Wait dynamically for elements to load.
# 4. Extract 4 key stock metrics.
# 5. Save the output to investing_data_output.csv.
# 6. Close the browser automatically.

# 🧩 Configuration
# To scrape another stock page, edit the configuration section at the top of scraper.py:

# --- 1. CONFIGURATION ---
TARGET_URL = "https://es.investing.com/equities/YOUR-NEW-STOCK-URL-HERE"
OUTPUT_FILE = "investing_data_output.csv"
WAIT_TIMEOUT = 10

# 📤 Output Example
# When executed, the script generates a CSV file with this structure:
# Current_Price    Daily_Change_Percent    Volume    Day_Range
# 213,07           +0,17%                  27,94M    264,65 - 267,76

# 📝 Example data only. Values depend on the page’s locale and real-time market status.

# 🧠 Best Practices
# - Use a VPN or stable connection to avoid IP blocks.
# - If the site structure changes, update CSS/XPath selectors in the code.
# - For multiple pages or tickers, wrap the extraction in a loop and append to the same CSV.

---

## 👤 Author

**Matías Kostiak**  
💼 *Data Engineer | Python Automation & Web Scraping Specialist*  
📧 [matiaskostiak25@gmail.com](mailto:matiaskostiak25@gmail.com)  
🌎 Paraguay  
🔗 LinkedIn | Upwork | Fiverr

---

## 🏷️ License

This project is released under the **MIT License** — feel free to use and adapt it for your own portfolio or client projects.

---

⭐ **If you find this useful, give it a star on GitHub — it helps me grow my portfolio and reach more collaborators!**
