import time
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

'''INFO Product #1 (Инормация по продукту №1)'''
product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()
print('Select Product 1')

cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
cart.click()
print('Enter Cart')

'''INFO Cart Product 1 (Информация о первом товаре в корзине)'''
cart_product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1 # Сравнием название товара в каталоге и карзине
print('INFO Cart Product 1 GOOD')

price_cart_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1 # Сравнием цену товара в каталоге и карзине
print('INFO Cart Price Product 1 GOOD')

checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()
print('Click Checkout')

'''Select User INFO (Вводим информацию о пользователе)'''
first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
first_name.send_keys('Alex')
print('Input First Name')

last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
last_name.send_keys('Ivanov')
print('Input Last name')

zip = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
zip.send_keys('1234')
print('Input Zip')

button_continue = driver.find_element(By.XPATH, '//*[@id="continue"]')
button_continue.click()
print('Click Continue')

'''INFO Finish Product 1 (Информация о завершении)'''
finish_product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1 # Сравнием название товара в каталоге и заказе
print('INFO Finish Product 1 GOOD')

price_finish_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1 # Сравнием цену товара в каталоге и заказе
print('INFO Finish Price Product 1 GOOD')

summery_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_summery_price = summery_price.text
print(value_summery_price)

item_total = 'Item total: ' + value_finish_price_product_1
print(item_total)
assert value_summery_price == item_total # Сравниваем строку "финальная стоимость товара"
print('Total Summery price GOOD')

time.sleep(3)
driver.quit()