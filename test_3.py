import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.XPATH, "//select [@data-test='product_sort_container']")
filter.click()
print('Click filter')
time.sleep(5)
filter.send_keys(Keys.DOWN)
time.sleep(5)
filter.send_keys(Keys.RETURN)

time.sleep(3)
driver.quit()