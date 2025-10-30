from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://invu.ge")



# Click the login link
from selenium.webdriver.common.by import By
login_link = driver.find_element(By.XPATH, '//a[@href="/login"]')
login_link.click()


# Wait for the login page to load and find the email input field
import time
time.sleep(2)
email_input = driver.find_element(By.XPATH, '//input[@id="email"]')
email_input.send_keys('annatatunashvili20@gmail.com')


# Find the password input field and enter the password
password_input = driver.find_element(By.XPATH, '//input[@id="password"]')
password_input.send_keys('Invu.ge11')


# Click the login button
login_button = driver.find_element(By.XPATH, '//button[@class="w-full py-3 px-4 rounded-xl font-semibold focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"]')
login_button.click()

# Wait for the page to load after login
time.sleep(3)


# Click the templates link
templates_link = driver.find_element(By.XPATH, '//a[@href="/templates"]')
templates_link.click()

# Wait for the templates page to load
time.sleep(2)


# Click the specified div
target_div = driver.find_element(By.XPATH, '//div[@class="w-full h-full bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center"]')
target_div.click()

# Wait for the input to be available
time.sleep(1)


# Enter 'Birthday Party' in the input field
input_field = driver.find_element(By.XPATH, '//input[@class="w-full px-3 py-2 bg-muted-50 border rounded-md focus:ring-2 focus:ring-amber-500 focus:border-transparent transition-colors text-sm border-red-300"]')
input_field.send_keys('Birthday Party')

# Wait for the textarea to be available
time.sleep(1)


# Enter 'Celebrate together' in the textarea
textarea = driver.find_element(By.XPATH, '//textarea[@class="w-full px-3 py-2 bg-muted-50 border rounded-md focus:ring-2 focus:ring-amber-500 focus:border-transparent transition-colors resize-none text-sm border-red-300"]')
textarea.send_keys('Celebrate together')

# Wait for the next input to be available
time.sleep(1)



# Enter 'Tbilisi.Lisi' in all input fields matching the class
inputs = driver.find_elements(By.XPATH, '//input[@class="w-full px-3 py-2 bg-muted-50 border rounded-md focus:ring-2 focus:ring-amber-500 focus:border-transparent transition-colors text-sm border-red-300"]')
for input_field in inputs:
	input_field.clear()
	input_field.send_keys('Tbilisi.Lisi')

# Enter '11.11.2025' in all input fields matching the date class


# Enter '11.11.2025' in all input fields matching the date class
date_inputs = driver.find_elements(By.XPATH, '//input[@class="w-full h-10 md:h-[42px] px-3 bg-muted-50 border rounded-md focus:ring-2 focus:ring-amber-500 focus:border-transparent transition-colors text-sm border-red-300"]')
for date_input in date_inputs:
	date_input.clear()
	date_input.send_keys('11.11.2025')

# Enter '19:00' in the second input field matching the same class (for time)
if len(date_inputs) > 1:
	date_inputs[1].clear()
	date_inputs[1].send_keys('19:00')


# Click the button with the specified class
button = driver.find_element(By.XPATH, '//button[@class="flex items-center px-4 py-2 bg-white text-gray-800 rounded-xl border-2 border-gray-200 hover:bg-gray-50 hover:border-gray-300 font-semibold shadow-sm transition-colors disabled:opacity-50 text-sm md:text-base"]')
button.click()

# Optionally, keep the browser open for a few seconds to see the result
time.sleep(15)

# Close the browser
driver.quit()




