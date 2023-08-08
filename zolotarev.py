import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://www.provartesting.com/contact/"
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()


# button1 = browser.find_element(By.XPATH, '//*[@id="navbar"]/ul[1]/li[2]/a')
# button1.click()
# time.sleep(5)


select1 = Select(browser.find_element(By.XPATH, '//*[@id="input_11_10"]'))  #находим выпадающий список
select1.select_by_visible_text('Aruba')  # ищем элемент списка

# button = browser.find_element(By.XPATH, '/html/body/div[1]/form/button') #находим кнопку
# button.click() #кликаем кнопку

# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()