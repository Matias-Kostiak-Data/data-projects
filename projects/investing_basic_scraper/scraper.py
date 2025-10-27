import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# --- 1. CONFIGURATION ---
TARGET_URL = "https://es.investing.com/equities/apple-computer-inc"
OUTPUT_FILE = "investing_data_output.csv"
WAIT_TIMEOUT = 10 # Maximum seconds to wait for an element to appear

# --- 2. ROBUST EXTRACTION HELPER FUNCTION ---

def get_element_text(driver: webdriver.Chrome, by: By, selector: str, timeout: int) -> str:
    """
    Explicitly waits for an element to be visible and extracts its text.
    Handles errors if the element is not found after the timeout.
    
    Args:
        driver: The Selenium driver instance.
        by: The selection method (By.CSS_SELECTOR, By.XPATH, etc.).
        selector: The selector string.
        timeout: Maximum wait time in seconds.

    Returns:
        The element's text (.strip()) or 'N/A' if not found.
    """
    try:
        # 1. Wait for the element to be visible
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, selector))
        )
        # 2. Extract and clean text
        return element.text.strip()
    
    except TimeoutException:
        print(f"  Error (Timeout): Element not found or visible -> {selector}")
        return "N/A"
    except Exception as e:
        print(f"  Error extracting '{selector}': {e}")
        return "Error"

# --- 3. MAIN SCRIPT ---

def main():
    """
    Main function that runs the scraper.
    """
    
    # --- 3.1. CONFIGURE SELENIUM (HEADLESS MODE) ---
    print("Configuring Selenium driver in headless mode...")
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") # New headless mode
    chrome_options.add_argument("--disable-notifications") # Disable notifications
    chrome_options.add_argument("--window-size=1920,1080") # Define window size
    chrome_options.add_argument("--log-level=3") # Reduce console logs
    chrome_options.add_argument("--disable-gpu") # Often necessary in headless
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")


    # Use webdriver_manager to install/manage the driver automatically
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("Driver configured successfully.")
    except Exception as e:
        print(f"Critical error initializing WebDriver: {e}")
        print("Ensure Google Chrome is installed.")
        return

    # Dictionary to store extracted data
    data = {}

    try:
        # --- 3.2. OPEN URL ---
        print(f"Opening URL: {TARGET_URL}")
        driver.get(TARGET_URL)
        
        # Optional: Short pause to allow initial JS to settle
        # time.sleep(1) 

        # --- 3.3. DATA EXTRACTION WITH EXPLICIT WAITS ---
        print("Starting key data extraction...")

        # A. Current Price
        price = get_element_text(driver, By.CSS_SELECTOR, '[data-test="instrument-price-last"]', WAIT_TIMEOUT)
        data['Current_Price'] = price
        print(f"  Current Price: {price}")

        # B. Daily Change (%)
        change_perc = get_element_text(driver, By.CSS_SELECTOR, '[data-test="instrument-price-change-percent"]', WAIT_TIMEOUT)
        data['Daily_Change_Percent'] = change_perc
        print(f"  Daily Change (%): {change_perc}")

        # C. Volume (Using XPath for 'following-sibling')
        volume = get_element_text(driver, By.XPATH, "//dt[text()='Volumen']/following-sibling::dd[1]", WAIT_TIMEOUT)
        data['Volume'] = volume
        print(f"  Volume: {volume}")

        # D. Day's Range (Using XPath for 'following-sibling')
        day_range = get_element_text(driver, By.XPATH, "//dt[text()='Rango día']/following-sibling::dd[1]", WAIT_TIMEOUT)
        data['Day_Range'] = day_range
        print(f"  Day's Range: {day_range}")

        # --- 3.4. SAVE DATA TO CSV ---
        print("\nExtraction complete. Saving to CSV...")
        
        # Create Pandas DataFrame from the dictionary (single row)
        # Use [data] to create a list of a single dictionary
        df = pd.DataFrame([data])
        
        # Save to CSV
        df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')
        print(f"Data saved successfully to '{os.path.abspath(OUTPUT_FILE)}'")

    except Exception as e:
        print(f"An unexpected error occurred in the main process: {e}")
    
    finally:
        # --- 3.5. CLEANUP ---
        if 'driver' in locals():
            driver.quit()
            print("Browser closed cleanly.")

if __name__ == "__main__":
    main()