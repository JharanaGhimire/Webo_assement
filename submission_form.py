

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()


wait = WebDriverWait(driver, 20)

driver.get("https://webo.digital/")
driver.maximize_window()
navs = wait.until(EC.visibility_of_any_elements_located((By.XPATH, "//a[@class='Nav_navItem__26bV0']")))
navs[-1].click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='primary-bttn']"))).click()

firstname = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='firstname']")))
lastname = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='lastname']")))
email = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='email']")))
ticketSubject = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='TICKET.subject']")))
select_box = Select(wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@name='TICKET.hs_ticket_priority']"))))
ticketContent = wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@name='TICKET.content']")))

firstname.send_keys("Jharana")
lastname.send_keys("Ghimire")
email.send_keys("Jharana@gmail.com")
ticketSubject.send_keys("Message for the issue")
select_box.select_by_value("LOW")
ticketContent.send_keys("Description about the issue message")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='submit']"))).submit()
print('DOne!!!!')