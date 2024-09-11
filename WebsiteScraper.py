from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service('path_to_chromedriver')

driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'your_target_url'
driver.get(url)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    )
    page_source = driver.page_source
finally:
    driver.quit()

soup = BeautifulSoup(page_source, 'lxml')

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

print("HTML content saved to index.html")
