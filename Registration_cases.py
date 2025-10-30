from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up the Chrome WebDriver (make sure chromedriver is installed and in your PATH)
driver = webdriver.Chrome()

# Open the website
driver.get('https://invu.ge')


# Wait for the page to load
time.sleep(2)

# Click the login link
login_link = driver.find_element(By.XPATH, '//a[@href="/login"]')
login_link.click()


# Wait for the login page to load
time.sleep(3)


# Wait for the button to be clickable, then click it
wait = WebDriverWait(driver, 3)  # wait up to 3 seconds
login_button = wait.until(
	EC.element_to_be_clickable((By.XPATH, '//button[@class="font-medium transition-colors"]'))
)
login_button.click()


# Wait for the registration form to load
time.sleep(2)

# Enter 'Ana' into the first name input
first_name_input = driver.find_element(By.XPATH, '//input[@id="firstName"]')
first_name_input.send_keys('Ana')


# Enter 'Tatunashvili' into the last name input
last_name_input = driver.find_element(By.XPATH, '//input[@id="lastName"]')
last_name_input.send_keys('Tatunashvili')


# Enter email into the email input
email_input = driver.find_element(By.XPATH, '//input[@id="email"]')
email_input.send_keys('anitatunashvili96@gmail.com')


# Enter password into the password input
password_input = driver.find_element(By.XPATH, '//input[@id="password"]')
password_input.send_keys('Invu.ge1')


# Enter password into the confirm password input
confirm_password_input = driver.find_element(By.XPATH, '//input[@id="confirmPassword"]')
confirm_password_input.send_keys('Invu.ge1')


# Wait for the submit button to be clickable, then click it
submit_button = WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.XPATH, '//button[@class="w-full py-3 px-4 rounded-xl font-semibold focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"]'))
)
submit_button.click()

# Wait to observe the result
time.sleep(2)

# Close the browser
driver.quit()

