from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name=firstname]")
    input1.send_keys("Danil")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name=lastname]")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name=email]")
    input3.send_keys("ivanov.danil@mail.ru")
    with open("file.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
