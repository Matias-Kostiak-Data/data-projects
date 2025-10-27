Investing.com Stock Data Scraper

A lightweight Python scraper that extracts current price, daily change, volume, and day range from any stock page on Investing.com
.
It uses Selenium in headless mode and WebDriver Manager for automatic driver installation.
All extracted data is stored in a clean, single-row CSV file.

Features

Handles dynamic JavaScript-rendered content with explicit waits (WebDriverWait).

Runs in headless mode (no visible browser window).

Automatic ChromeDriver management via webdriver-manager.

Graceful error handling for timeouts and missing elements.

Clean CSV output for quick data use.

Technology Stack

Python 3.8+

Selenium

Pandas

WebDriver Manager

Google Chrome
