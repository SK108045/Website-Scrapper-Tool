#This code contains includes the driver manager package just incase there is a mismatch between the chrome driver version and the chrome browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the WebDriver using ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Set up the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the URL
url = 'website_url'
driver.get(url)

# Wait for a specific element to be present to ensure the page is loaded
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    )
    # Get the page source
    page_source = driver.page_source
finally:
    # Close the WebDriver
    driver.quit()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(page_source, 'lxml')

# Save the prettified HTML to a file
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

print("HTML content saved to index.html")
