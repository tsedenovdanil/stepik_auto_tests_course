from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    option1 = browser.find_element(By.ID, "answer")
    option1.send_keys(y)
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option2.click()
    option3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option3.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
