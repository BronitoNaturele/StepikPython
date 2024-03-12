from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

browser.implicitly_wait(5)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    # Находим кнопку book
    book = browser.find_element(By.XPATH, "/html/body/div/div/div/button[@id='book']").click()
    
    # Находим кнопку submit
    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button[@type='submit']")
    
    # Скроллим футер
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    # Находим и считываем значение х
    x_element = browser.find_element(By.XPATH, "/html/body/form/div/div/div/label/span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    
    # Находим поле ввода и вводим значение
    input1 = browser.find_element(By.XPATH, "/html/body/form/div/div/div/input[@id='answer']")
    input1.send_keys(y)
    
    button.click()

finally:

    time.sleep(3)
    browser.quit()