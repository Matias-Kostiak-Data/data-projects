import requests
from bs4 import BeautifulSoup
import pandas as pd

# ------------------------------
# CONFIGURATION
# ------------------------------
URL = "https://books.toscrape.com/"

# ------------------------------
# SCRAPING
# ------------------------------
response = requests.get(URL)
response.raise_for_status()  # Check if the request was successful

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# List to store product data
data = []

# Loop through product containers
# NOTE: Adjust selectors depending on target website
for product in soup.select("article.product_pod"):
    name = product.h3.a.get("title").strip()
    price_text = product.select_one("p.price_color").text.strip()
    availability_text = product.select_one("p.availability").text.strip()
    
    data.append({
        "Name": name,
        "Price": price_text,
        "Availability": availability_text
    })

# ------------------------------
# DATA VALIDATION & CLEANING
# ------------------------------
df = pd.DataFrame(data)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert price to float: remove currency symbol and any extra characters
df["Price"] = df["Price"].str.replace(r"[^\d\.]", "", regex=True).astype(float)

# Filter out rows with empty names or prices
df = df[df["Name"].notna() & df["Price"].notna()]

# Save cleaned data to CSV
df.to_csv("scraped_data.csv", index=False)

# ------------------------------
# SUMMARY STATISTICS
# ------------------------------
total_rows = len(df)
unique_products = df["Name"].nunique()
average_price = df["Price"].mean()

print(f"Total rows: {total_rows}")
print(f"Unique products: {unique_products}")
print(f"Average price: {average_price:.2f}")
