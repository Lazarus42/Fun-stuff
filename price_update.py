# %%
import requests
import requests_html
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import time 

# %%
url = 'https://www.expedia.com/HotelCheckout?tripid=262491f1-c4be-5e5c-8fd1-edb917eab6cf&c=96b6454c-ff81-46f6-be99-d8c1d6de580b&swpApplied=false&searchId=0a1bb45b-acca-410e-8fa7-adb44fddc7c6'

# %%
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# %%
options = Options()
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--window-size=1920,1080")  # Set the window size
options.add_argument(f"user-agent={USER_AGENT}")  # Set the custom user agent
driver = uc.Chrome(headless=False)
driver.get(url)
time.sleep(1)
# Alternatively, to scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, 1500);")
time.sleep(1)
# Find the element with 'data-triptotal' and retrieve the attribute
# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'html.parser')
element = soup.find(attrs={"data-triptotal": True})
if element:
    triptotal = element['data-triptotal']
    with open('Desktop/san_juan_hotel_prices.txt', 'a') as f:
        f.write(str(triptotal) + '\n')
        f.close()
else:
    pass
# Close the browser
print("Performed task\n")
driver.quit()


