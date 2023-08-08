import time

import summary as summary
from selenium import webdriver
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
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Button")

"""INFO Produkt #1 (Информация по продукту 1)"""
produkt_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_produkt_1 = produkt_1.text
print(value_produkt_1)

price_produkt_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_produkt_1 = price_produkt_1.text
print(value_price_produkt_1)

select_product_1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print('Select Product 1')

cart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a/span")
cart.click()
print('Enter Cart')

'''INFO Cart Product 1 (Информация о первом товаре в корзине)'''
cart_produkt_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_cart_produkt_1 = cart_produkt_1.text
print(value_cart_produkt_1)
assert value_produkt_1==value_cart_produkt_1 #Сравниваем название товара в каталоге и корзине
print('INFO Cart Produkt 1 Good')

price_cart_produkt_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_cart_produkt_1 = price_cart_produkt_1.text
print(value_price_cart_produkt_1)
assert value_price_produkt_1==value_price_cart_produkt_1 #Сравниваем цену товара в каталоге и корзине
print('INFO Cart Price Produkt 1 Good')

checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()
print('Click Checkout')

'''Select User Info'''
first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
first_name.send_keys('Alex')
print('Input First Name')

last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
last_name.send_keys('Smith')
print('Input Last Name')

zip = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
zip.send_keys('1234')
print('Input ZIP')

button_continue = driver.find_element(By.XPATH, '//*[@id="continue"]')
button_continue.click()
print('Click Continue')

'''INFO Finish Product 1 (Информация о завершении)'''
finish_produkt_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_finish_produkt_1 = finish_produkt_1.text
print(value_finish_produkt_1)
assert value_produkt_1 == value_finish_produkt_1 #Сравниваем название товара в каталоге и заказе
print('INFO Finish Produkt 1 Good')

price_finish_produkt_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_finish_produkt_1 = price_finish_produkt_1.text
print(value_price_finish_produkt_1)
assert value_price_produkt_1 == value_price_finish_produkt_1 #Сравниваем цену товара в каталоге и заказе
print('INFO Finish Price Produkt 1 Good')

summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]")'
value_summary_price = summary_price.text
print(value_summary_price)
# assert value_produkt_1==value_finish_produkt_1 #Сравниваем название товара в каталоге и заказе
# print('INFO Finish Produkt 1 Good')
item_total = 'Item total: ' + value_price_finish_produkt_1
print(item_total)
assert value_summary_price==item_total #Сравниваем строку с финальной ценой
print('Total Summary Price Good')





time.sleep(3)
driver.quit()