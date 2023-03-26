# Import necessary libraries
from selenium import webdriver
import time

# Set up the driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://webo.digital/")
driver.maximize_window
# Wait for the page to load
time.sleep(2)

# Find the "Support" link and click it
support_link = driver.find_element_by_partial_link_text("Support")
support_link.click()

# Wait for the page to load
time.sleep(2)

# Print the current URL
print(driver.current_url)

# Close the driver
driver.close()
