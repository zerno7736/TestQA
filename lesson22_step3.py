import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num_1 = browser.find_element(By.XPATH, '//*[@id="num1"]').text
num_1 = int(num_1)
num_2 = browser.find_element(By.XPATH, '//*[@id="num2"]').text
num_2 = int(num_2)
value = str(num_1 + num_2)
print('num1 + num2 =', value)

select = Select(browser.find_element(By.TAG_NAME, "select")) #находим выпадающий список
select.select_by_visible_text(value) # ищем элемент списка

button = browser.find_element(By.XPATH, '/html/body/div[1]/form/button') #находим кнопку
button.click() #кликаем кнопку

# закрываем браузер после всех манипуляций
time.sleep(30)
browser.quit()