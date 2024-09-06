from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

zillow_url = "https://appbrewery.github.io/Zillow-Clone/"

# Keep Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(zillow_url)

# Give the page some time to load
time.sleep(2)

# Wait for the body of the page to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    print("Page body loaded")
except:
    print("Page body not loaded")

# Find all property cards containing both address and link
property_cards = driver.find_elements(By.CLASS_NAME, "StyledPropertyCardDataWrapper")

# Prepare lists for filtered links, addresses, and prices
links = []
addresses = []
prices = []

# Iterate over the property cards and extract links, addresses, and prices
for card in property_cards:
    # Find the link inside the property card
    link_element = card.find_element(By.TAG_NAME, 'a')
    href = link_element.get_attribute('href')
    links.append(href)

    # Extract the address text from the same card
    address_text = card.text.split("\n")[0]  # Get the first line of text as the address
    addresses.append(address_text)

    # Extract the price from the card by splitting the text and finding the line with "$"
    card_text_lines = card.text.split("\n")
    price = "Price not available"  # Default if no price is found

    for line in card_text_lines:
        if "$" in line:
            # Use regular expressions to extract just the price
            price_match = re.search(r'\$\d+(?:,\d+)?', line)
            if price_match:
                price = price_match.group(0)
            break

    prices.append(price)

# Print the filtered links, addresses, and prices
# print("Links:", links)
# print(len(links))
#
# print("Addresses:", addresses)
# print(len(addresses))
#
# print("Prices:", prices)
# print(len(prices))

g_form_url = YOUR GOOGLE FORM LINK

# Keep Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the driver
google_driver = webdriver.Chrome(options=chrome_options)
google_driver.get(g_form_url)

# Give the page some time to load
time.sleep(2)

# Wait for the body of the page to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    print("Page body loaded")
except:
    print("Page body not loaded")

for i in range(0, len(links)):
    # Locate the address input field using relative XPath (based on form layout)
    address_input = google_driver.find_element(by=By.XPATH,
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(addresses[i])

    # Locate the price input field using relative XPath (based on form layout)
    price_input = google_driver.find_element(by=By.XPATH,
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(prices[i])

    # Locate the link input field using relative XPath (based on form layout)
    link_input = google_driver.find_element(by=By.XPATH,
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(links[i])

    # Submit the form
    submit_button = google_driver.find_element(by=By.XPATH,
                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    # Wait for the form to be submitted and reload the form
    time.sleep(2)
    google_driver.get(g_form_url)
    time.sleep(2)
